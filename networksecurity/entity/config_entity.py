from datetime import datetime
import os
from networksecurity.constants import training_pipeline

print(training_pipeline.DATA_INGESTION_DIR_NAME)
print(training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR)
print(training_pipeline.ARTIFACT_DIR)
print(training_pipeline.PIPELINE_NAME)

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.timestamp: str = timestamp

class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        self.data_ingestion_dir:str = os.path.join(
            training_pipeline_config.artifact_dir, training_pipeline.DATA_INGESTION_DIR_NAME
            ) # Directory for data ingestion artifacts
        
        self.feature_store_file_path:str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
            ) # Path to save the feature store file
        
        self.training_file_path:str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_NAME
            ) # Path to save the training data file
            

        self.testing_file_path:str = os.path.join(
            self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_NAME
            ) # Path to save the training data file
        

        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME # Name of the MongoDB database for data ingestion
        self.collection_name = training_pipeline.DATA_INGETION_COLLECTION_NAME # Name of the MongoDB collection for data ingestion
        self.train_test_split_ratio = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO # Ratio for splitting data into training and testing sets