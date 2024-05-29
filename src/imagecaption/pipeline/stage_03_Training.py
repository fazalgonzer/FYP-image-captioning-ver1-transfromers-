from imagecaption.config.configuration import ConfigurationManger
from imagecaption.components.training import Train
from imagecaption.logging import logger




class DataTrainingPipeline:
    def __init__(self) :
        pass 

    def main(self):
        
        config= ConfigurationManger()
        data_pretrain_config=config.get_dataset_pretrain()
        training=Train(data_pretrain_config)