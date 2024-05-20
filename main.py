

from imagecaption.logging import logger
from imagecaption.pipeline.stage_01_data_ingestion import DataingestionConfigTrainingPipeline

STAGE_NAME="Data Ingestion Config"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion=DataingestionConfigTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> {STAGE_NAME} Completed ")
except Exception as e:
    raise e
