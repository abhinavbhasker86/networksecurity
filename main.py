from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging #    import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig
import sys

if __name__ == "__main__":
    try:
        
        trainingpipelineconfig = TrainingPipelineConfig()  # Initialize the training pipeline configuration
       
        logging.info("Initiate Data Ingestion")
        # Initialize DataIngestionConfig with appropriate parameters
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)  # Pass the training pipeline config to DataIngestionConfig
        # Create an instance of DataIngestion
        data_ingestion = DataIngestion(dataingestionconfig)
        # Initiate the data ingestion process        
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info(f"Data ingestion completed successfully. Artifact: {dataingestionartifact}")
       
        
        logging.info("Initiate Data Validation")
        # Initialize DataValidationConfig with appropriate parameters
        data_validation_config= DataValidationConfig(trainingpipelineconfig)
        # Create an instance of DataValidation
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        # Initiate Data Validatiion
        data_validation_artifact=data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("Data Validation Completed")

        logging.info("Initiate Data Transformation")
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Completed Data Transformation")

        
    except Exception as e:
        logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
        raise NetworkSecurityException(e, sys)  # This will raise the custom exception with the error details