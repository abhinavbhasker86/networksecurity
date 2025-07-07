from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging #    import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig
import sys

if __name__ == "__main__":
    try:
        logging.info("Starting data ingestion process.")
        trainingpipelineconfig = TrainingPipelineConfig()  # Initialize the training pipeline configuration
        
        # Initialize DataIngestionConfig with appropriate parameters
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)  # Pass the training pipeline config to DataIngestionConfig
        # Create an instance of DataIngestion
        data_ingestion = DataIngestion(dataingestionconfig)
        # Initiate the data ingestion process
        logging.info("Initiate Data Ingestion")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        
        logging.info(f"Data ingestion completed successfully. Artifact: {data_ingestion_artifact}")
        print(data_ingestion_artifact)  # Print the artifact details
        
        # Initialize DataValidationConfig with appropriate parameters
        data_validation_config= DataValidationConfig(trainingpipelineconfig)
        # Create an instance of DataValidation
        data_validation=DataValidation(dataingestionconfig,data_validation_config)
        # Initiate Data Validatiion
        logging.info("Initiate Data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_ingestion_artifact)
        
    except Exception as e:
        logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
        raise NetworkSecurityException(e, sys)  # This will raise the custom exception with the error details