from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging #    import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        logging.info("Starting data ingestion process.")
        trainingpipelineconfig = TrainingPipelineConfig()  # Initialize the training pipeline configuration
        # Initialize DataIngestionConfig with appropriate parameters
        data_ingestion_config = DataIngestionConfig(trainingpipelineconfig)  # Pass the training pipeline config to DataIngestionConfig
        
        # Create an instance of DataIngestion
        data_ingestion = DataIngestion(data_ingestion_config)
        
        # Initiate the data ingestion process
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        
        logging.info(f"Data ingestion completed successfully. Artifact: {data_ingestion_artifact}")
        print(data_ingestion_artifact)  # Print the artifact details
        
    except Exception as e:
        logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
        raise NetworkSecurityException(e, sys)  # This will raise the custom exception with the error details