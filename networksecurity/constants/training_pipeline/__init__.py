import os
import sys
import numpy as np
import pandas as pd

"""
Constants for the training pipeline of the network security project.
This module defines constants used throughout the training pipeline, including file paths,
data processing parameters, and model configuration.
"""
TARGET_COLUMN = "Result"  # The target column in the dataset
PIPELINE_NAME = "NetworkSecurity"  # Name of the training pipeline
ARTIFACT_DIR = "Artifacts"  # Directory to save pipeline artifacts
FILE_NAME = "phisingData.csv"  # Name of the dataset file


TRAIN_FILE_NAME = "train.csv"  # Name of the training data file 
TEST_FILE_NAME = "test.csv"  # Name of the test data file

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")  # Path to the schema file

SAVED_MODEL_DIR =os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"




"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME = "NetworkData"  # Name of the MongoDB collection for data ingestion
DATA_INGESTION_DATABASE_NAME = "AB_NetworkSecurity"  # Name of the MongoDB database for data ingestion
DATA_INGESTION_DIR_NAME = "data_ingestion"  # Path to save data ingestion artifacts
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"  # Directory for feature store artifacts
DATA_INGESTION_INGESTED_DIR = "ingested"  # Directory for ingested data
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO = 0.2  # Ratio for splitting data into training and testing sets

"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

## kkn imputer to replace nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}
DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"


"""
Model Trainer ralated constant start with MODE TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD: float = 0.05

TRAINING_BUCKET_NAME = "networksecurityab"