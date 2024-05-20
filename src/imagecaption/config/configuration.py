from imagecaption.constants import * 
from imagecaption.utils.common import read_yaml , create_directories
from imagecaption.entity import DataIngestionConfig

class ConfigurationManger:
    def __init__(self,config_file_path=config_file_path,params_file_path=params_file_path):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion(self) -> DataIngestionConfig:
        config=self.config.data_ingestion  
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            save_path= config.root_dir
        )
     
        return data_ingestion_config
