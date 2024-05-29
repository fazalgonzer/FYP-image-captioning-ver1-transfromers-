from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    save_path:Path


@dataclass
class Data_transformation_config:
    reading_data: Path
    saving_data_train : Path
    saving_data_test : Path
    dataset_processor: str 
    

from dataclasses import dataclass
from pathlib import Path
@dataclass
class Data_pretrain_config:
    model: str
    n_accumulate : int 

    
    scheduler: str
    training_batch_size: int
    valid_batch_size: int
   
    
    
    #itni dair baad weights update hongay