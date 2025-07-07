from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging #    import logging

## Configuration for data ingestion
from networksecurity.entity.config_entity import DataIngestionConfig

from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os
import sys
import numpy as np
import pymongo 
import pandas as pd
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            logging.info(f"MongoDB client created with URL: {MONGO_DB_URL}")
        except Exception as e:
            logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
            raise NetworkSecurityException(e, sys)
        
    def export_collection_as_dataframe(self):
        """ 
        Read from MondoDB and converts it to a pandas DataFrame.
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection= self.mongo_client[database_name][collection_name]
            
            df = pd.DataFrame(collection.find()) # Fetching the collection as a DataFrame)

            if "_id" in df.columns.to_list(): #
                df.drop(columns=["_id"], axis=1)

            df.replace({"na": np.nan}, inplace=True) #  Replacing 'na' with NaN values

            return df   


        except Exception as e:
            logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
            raise NetworkSecurityException(e, sys)
        
    def export_data_into_feature_store(self,dataframe: pd.DataFrame):
        """
        Export the data into a feature store.
        """
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)  # Ensure the directory exists
            logging.info(f"Directory created for feature store: {dir_path}")
            logging.info(f"Exporting data to feature store at: {feature_store_file_path}")
            

            dataframe.to_csv(feature_store_file_path, index=False,header=True)  # Exporting the DataFrame to a CSV file
            logging.info(f"Data exported to feature store at: {feature_store_file_path}")

            return dataframe
        
        except Exception as e:
            logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
            raise NetworkSecurityException(e, sys)

    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        """
        Split the DataFrame into training and testing sets.
        """
        try:
            train_test_split_ratio = self.data_ingestion_config.train_test_split_ratio
            train_set, test_set = train_test_split(dataframe, test_size=train_test_split_ratio, random_state=42)
            logging.info(f"Data split into train set with shape: {train_set.shape} and test set with shape: {test_set.shape}")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)  # Ensure the directory exists

            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            logging.info(f"Train set saved to: {self.data_ingestion_config.training_file_path}")
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
            logging.info(f"Test set saved to: {self.data_ingestion_config.testing_file_path}")

            #return train_set, test_set
        
        except Exception as e:
            logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
            raise NetworkSecurityException(e, sys)
    
    def initiate_data_ingestion(self):
        try:
            logging.info("Starting data ingestion process.")
            dataframe = self.export_collection_as_dataframe()  # Fetching the collection as a DataFrame
            dataframe =self.export_data_into_feature_store(dataframe) # Fetching the collection as a DataFrame
            logging.info(f"Data fetched from MongoDB collection: {self.data_ingestion_config.collection_name}")
            
            self.split_data_as_train_test(dataframe)  # Splitting the DataFrame into train and test sets

            dataingetionafract = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )  # Creating an artifact for data ingestion
            
            logging.info("Train and test datasets saved successfully.")
            return dataingetionafract  # Returning the artifact
        
        except Exception as e:
            logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
            raise NetworkSecurityException(e, sys)

