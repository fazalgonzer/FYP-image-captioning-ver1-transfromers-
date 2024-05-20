from imagecaption.config.configuration import ConfigurationManger
from imagecaption.components.data_ingestion import DataIngestion
from imagecaption.logging import logger




class DataingestionConfigTrainingPipeline:
    def __init__(self) :
        pass 

    def main(self):
        
       config= ConfigurationManger()
       data_Ingestion_config=config.get_data_ingestion()
       data_ingestion=DataIngestion(config=data_Ingestion_config)
       data_ingestion.LoadingData()
