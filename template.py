import os 
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name= "imagecaption"


list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "test.py"
    "Dockerfile"






]

for file_path in list_of_files:
    file_path=Path(file_path)
    filedir,filename=os.path.split(file_path)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info("created all the files{filedir}")
    if (not os.path.exists(file_path) or os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass 
            logging.info(f"created empty file as {file_path}")
    else:
        logging.info(f"{filename} is already exist at {file_path}") 