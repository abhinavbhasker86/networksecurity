import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
            raise NetworkSecurityException(e, sys)
    
    def csv_to_json_convertor(self, file_path):
        try:
            logging.info(f"Reading CSV file from path: {file_path}")
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            logging.info("CSV file read successfully. Converting to JSON format.")
            records = list(json.loads(data.T.to_json()).values())
            logging.info("CSV file successfully converted to JSON format.")
            return records
        except Exception as e:
            logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database # Name of the database in MongoDB
            logging.info(f"Connecting to MongoDB database: {database}") 

            self.collection = collection # Name of the collection in MongoDB
            self.records = records # List of records to be inserted
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL) # Create a MongoDB client

            self.database=self.mongo_client[database]  # Access the database
            self.collection=self.database[collection] # Access the collection
            logging.info(f"MongoDB connection established to database: {database}, collection: {collection}")

            self.collection.insert_many(self.records)
            
            return (len(self.records)) # Return the number of records inserted

        except Exception as e:
            logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
            raise NetworkSecurityException(e, sys)
        
if __name__ == '__main__':
    try:
        file_path = 'Network_Data\phisingData.csv'  # Path to the CSV file containing network data
        logging.info(f"Starting data extraction from file: {file_path}")
        database = 'AB_NetworkSecurity'
        collection = 'NetworkData'

        networkobj  = NetworkDataExtract()
        records = networkobj.csv_to_json_convertor(file_path)  # Convert CSV to JSON format
        print(records)
        no_of_records = networkobj.insert_data_mongodb(records,database,collection) # Insert records into MongoDB
        print(no_of_records)

        logging.info(f"Inserted {no_of_records} records into MongoDB collection '{collection}' in database '{database}'.")

    except Exception as e:
        logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
        raise NetworkSecurityException(e, sys)
        