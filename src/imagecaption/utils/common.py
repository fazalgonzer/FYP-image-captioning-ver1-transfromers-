import os 
import yaml
from box.exceptions import BoxValueError
from imagecaption.logging import logger
from box import ConfigBox
from typing import Any
from ensure import ensure_annotations
from pathlib import Path


@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:

            content =yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} laoded sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at :{path} ")


@ensure_annotations            
def get_size(path:Path)->str:
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


    
        