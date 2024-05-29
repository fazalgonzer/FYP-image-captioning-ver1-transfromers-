import os 
from imagecaption.logging import logger 
import torch
from torch.utils.data import  DataLoader
import tqdm
import numpy as np
import time 
import copy
from transformers import BlipForConditionalGeneration
from collections import defaultdict

from imagecaption.entity import Data_pretrain_config


class Pretrain():
    def __init__(self, config:Data_pretrain_config) :
        self.config=config
        self.model = BlipForConditionalGeneration.from_pretrained(self.config.model)

#pixel_values (torch.FloatTensor of shape (batch_size, num_channels, height, width)) — Pixel values. Padding will be ignored by default should you provide it. Pixel values can be obtained using BlipImageProcessor. See BlipImageProcessor.call() for details.
#output_attentions (bool, optional) — Whether or not to return the attentions tensors of all attention layers. See attentions under returned tensors for more detail.
#output_hidden_states (bool, optional) — Whether or not to return the hidden states of all layers. See hidden_states under returned tensors for more detail.
#return_dict (bool, optional) — Whether or not to return a ModelOutput instead of a plain tuple.
#interpolate_pos_encoding (bool, optional, defaults to False) — Whether to interpolate the pre-trained position encodings.
  
    def train_one_epoch(self,model,optimizer,scheduler,dataloader,device,epoch):
        model.train()
        dataset_size=0
        running_loss=0.0
        bar=tqdm(enumerate(dataloader),total=len(dataloader))
        for step,data in bar:
            input_ids=data['input_ids'].to(device)
            pixel_values =data['pixel_values'].to(device)
            batch_size=input_ids.size(0)
            outputs= model(input_ids=input_ids,pixel_values=pixel_values,labels=input_ids)

            loss =outputs.loss
            loss=loss / self.config.n_accumulate
            loss.backward()

            if (step +1 )% self.config.n_accumulate ==0:
                optimizer.step()
                # zero the parameter gradients
                optimizer.zero_grad()

                if scheduler is not None:
                    scheduler.step()
            running_loss += (loss.item() * batch_size)
            dataset_size += batch_size

            epoch_loss = running_loss / dataset_size

            bar.set_postfix(Epoch=epoch, Train_Loss=epoch_loss,
                        LR=optimizer.param_groups[0]['lr'])
       

        return epoch_loss
    @torch.no_grad()
    def valid_one_epoch(self,model,dataloader,device,epoch, optimizer):
        model.eval()
        dataset_size=0
        running_loss=0.0

        bar= tqdm(enumerate(dataloader), total=len(dataloader))
        for step , data in bar :
            input_ids=data['input_ids'].to(device)
            pixel_values=data['pixel_values'].to(device)

            batch_size=input_ids.size(0)
            outputs=model(input_ids=input_ids,pixel_values=pixel_values,labels=input_ids)
            loss=outputs.loss
            running_loss += (loss.item() * batch_size)
            dataset_size += batch_size

            epoch_loss = running_loss / dataset_size

            bar.set_postfix(Epoch=epoch, Valid_Loss=epoch_loss,
                        LR=optimizer.param_groups[0]['lr'])
        return epoch_loss


    def run_training(self,model,optimizer,scheduler, device, num_epochs ):

        if torch.cuda.is_available():
             print("[INFO] Using GPU: {}\n".format(torch.cuda.get_device_name()))   
        start=time.time()
        best_model_wtd=copy.deepcopy(model.state_dict())
        best_epoch_loss=np.inf
        history=defaultdict(list)

        for epoch in range(1,num_epochs+1):
            train_epoch_loss=self.train_one_epoch(model,optimizer,scheduler, dataloader=train_loader,device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu"))
            val_epoch_loss=self.valid_one_epoch(model=model,optimizer=optimizer, dataloader=valid_loader, device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu"))
            

            history['Train Loss'].append(train_epoch_loss)
            history['Valid Loss'].append(val_epoch_loss)

            if val_epoch_loss<=best_epoch_loss:
                print(f"Validation Loss Improved ({best_epoch_loss} ---> {val_epoch_loss})")
                best_epoch_loss = val_epoch_loss
                best_model_wts = copy.deepcopy(model.state_dict())
                PATH = f"BestLoss.bin"
                torch.save(model.state_dict(), PATH)
                end = time.time()
        time_elapsed = end - start
        print('Training complete in {:.0f}h {:.0f}m {:.0f}s'.format(
        time_elapsed // 3600, (time_elapsed % 3600) // 60, (time_elapsed % 3600) % 60))
        print("Best Loss: {:.4f}".format(best_epoch_loss))

        # load best model weights
        model.load_state_dict(best_model_wts)

        return model, history