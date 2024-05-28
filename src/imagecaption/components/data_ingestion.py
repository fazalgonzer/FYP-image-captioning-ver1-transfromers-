import os 
import urllib.request as requset
import zipfile
from imagecaption.logging import logger
from imagecaption.utils.common import get_size
from datasets import load_dataset
from imagecaption.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config= config

 
    def LoadingData(self):
         #this if condition will be remove for first time after running the code  2nd time add this if condition becuase of docker file config .
         #run it after removing if first time then add it again so data is loaded correctly 
         if not os.path.exists(self.config.save_path):
            dataset= load_dataset('poloclub/diffusiondb', '2m_first_5k')
            dataset = dataset['train']
            dataset = dataset.filter(lambda example: example["step"] == 50)
            dataset = dataset.train_test_split(test_size=0.1)
            dataset.save_to_disk(self.config.save_path)
            logger.info(f" file created at this loc -> {self.config.save_path}")
            

        
            