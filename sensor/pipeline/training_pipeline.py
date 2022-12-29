from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.exception import SensorException
import sys, os
from sensor.logger import logging


class TrainPipeline:

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Starting Data Ingestion")
            logging.info("Data Ingestion Completed")

        except Exception as e:
            raise SensorException(e, sys)


    def run_pipeline(self):
        try:
            self.start_data_ingestion()

        except Exception as e:
            raise SensorException(e, sys)