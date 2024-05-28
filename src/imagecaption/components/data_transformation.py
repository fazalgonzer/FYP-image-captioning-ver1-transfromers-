import os 
from imagecaption.logging import logger 
from transformers import AutoProcessor
from imagecaption.entity import Data_transformation_config
from torch.utils.data import Dataset, DataLoader
import pickle
from io import open as io_open
from datasets import load_from_disk

class ImageCaptionDataset(Dataset):
           def __init__(self,dataset,processor):
            self.dataset=dataset
            self.processor=processor
           def __len__(self):
             return len(self.dataset)

           def __getitem__(self, idx):
                item = self.dataset[idx]
                encoding = self.processor(images=item["image"], text=item["prompt"], padding="max_length", return_tensors="pt")
                # Remove batch dimension
                encoding = {k: v.squeeze() for k, v in encoding.items()}
                return encoding
class DataTransfromation():
    def __init__(self, config:Data_transformation_config):
         self.config=config 
    
    def datatransfromation(self):
       
       processor=AutoProcessor.from_pretrained(self.config.dataset_processor)
       dataset=load_from_disk(self.config.reading_data)
       
       

       train_dataset=ImageCaptionDataset(dataset['train'],self.config.dataset_processor) 
       valid_dataset = ImageCaptionDataset(dataset['test'], self.config.dataset_processor)
       
       with io_open(self.config.saving_data_train, 'wb') as  file:
          pickle.dump(train_dataset,file) 

       with io_open(self.config.saving_data_test, 'wb') as  file:
          pickle.dump(valid_dataset,file) 