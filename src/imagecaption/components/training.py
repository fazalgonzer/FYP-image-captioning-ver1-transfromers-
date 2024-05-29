import pickle
from io import open as io_open
from torch.optim import lr_scheduler
from transformers import  AdamW
import torch
from imagecaption.entity import Data_pretrain_config
from transformers import BlipForConditionalGeneration
from collections import defaultdict
from torch.utils.data import  DataLoader
from imagecaption.components.data_pretrain import Pretrain

class Train():
    def __init__(self,config:Data_pretrain_config):
        self.config=config
        self.model = BlipForConditionalGeneration.from_pretrained(self.config.model)
        with io_open('artifacts/transformed_data_train', 'rb') as file:
            self.train_data = pickle.load(file)
        with io_open('artifacts/transformed_data_test', 'rb') as file:
            self.test_data = pickle.load(file)
    def fetch_scheduler(self,optimizer):
        sc= self.config.scheduler

        if sc == 'CosineAnnealingLR':
            scheduler = lr_scheduler.CosineAnnealingLR(optimizer,T_max=500,
                                                   eta_min=1e-6)
        elif sc == 'CosineAnnealingWarmRestarts':
            scheduler = lr_scheduler.CosineAnnealingWarmRestarts(optimizer,
                                                             eta_min=1e-6)
        elif sc == None:
            return None

        return scheduler
    def training(self):
        train_loader=DataLoader(self.train_data,shuffle=True, batch_size=4)
        valid_loader = DataLoader(self.test_data, shuffle=False, batch_size=8)
        model=self.model
        model.to(torch.device("cuda:0" if torch.cuda.is_available() else "cpu"))
        optimizer = AdamW(model.parameters(), lr=1e-4 , weight_decay=1e-6)
        scheduler = self.fetch_scheduler(optimizer)
        obj=Pretrain()

        model, history = obj.run_training(model, optimizer, scheduler,
                              device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu"),
                              num_epochs=5)

        torch.save(model.state_dict(), 'artifacts/saving_trained_model')
        del model, history, train_loader, valid_loader
