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

"""
Data Ingestion constanst start with DATA_INGESTION

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
#PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
