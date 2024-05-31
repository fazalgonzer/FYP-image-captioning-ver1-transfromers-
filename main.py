

from imagecaption.logging import logger
from imagecaption.pipeline.stage_01_data_ingestion import DataingestionConfigTrainingPipeline
from imagecaption.pipeline.stage_02_data_transformation import DatatarnsfromationTrainingPipeline
from imagecaption.pipeline.stage_03_Training import DataTrainingPipeline
from imagecaption.pipeline.predict import PredictionPipeline

STAGE_NAME="Data Ingestion Config"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion=DataingestionConfigTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> {STAGE_NAME} Completed ")
except Exception as e:
    raise e


STAGE_NAME="Data Transfromation "
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion=DatatarnsfromationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> {STAGE_NAME} Completed ")
except Exception as e:
     raise e


#STAGE_NAME="Data Training"
#try:
 #   logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
  #  data_ingestion=DataTrainingPipeline()
   # data_ingestion.main()
    #logger.info(f">>>> {STAGE_NAME} Completed ")
#except Exception as e:
 #    raise e



