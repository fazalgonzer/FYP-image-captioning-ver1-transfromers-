from imagecaption.config.configuration import ConfigurationManger
from imagecaption.components.data_transformation import DataTransfromation
from imagecaption.logging import logger



class DatatarnsfromationTrainingPipeline:
    def __init__(self) :
        pass 

    def main(self):
        
        config= ConfigurationManger()
        data_transfromation_config=config.get_data_transformation()
        data_transfromation= DataTransfromation(config=data_transfromation_config)
        data_transfromation.datatransfromation()