from imagecaption.constants import * 
from imagecaption.utils.common import read_yaml , create_directories
from imagecaption.entity import DataIngestionConfig, Data_transformation_config ,Data_pretrain_config
from datasets import load_from_disk


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
    

    def get_data_transformation(self)->Data_transformation_config:
        config= self.config.data_transformation
        
   

        data_transformation_config= Data_transformation_config(
            reading_data=config.reading_data,
            saving_data_train=config.saving_data_train,
            saving_data_test=config.saving_data_test,

            dataset_processor=self.params.TrainingArguments.model_name



        )

        return data_transformation_config
    




    def get_dataset_pretrain(self)->Data_pretrain_config:
        config=self.config.pre_training

        data_pretrain_config=Data_pretrain_config(
            model=self.params.TrainingArguments.model_name,
            n_accumulate=self.params.TrainingArguments.n_accumulate,
            
          
            scheduler=self.params.TrainingArguments.scheduler,
            training_batch_size=self.params.TrainingArguments.training_batch_size,
            valid_batch_size=self.params.TrainingArguments.valid_batch_size,
         
         




        )


        return data_pretrain_config


