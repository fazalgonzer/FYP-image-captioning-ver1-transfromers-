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
    