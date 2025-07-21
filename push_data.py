# to push local file to atlas cloud mongodb
import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# to ensure a valid request to mongbd- to make secure https connection
ca = certifi.where()


class NetworDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    # Aim to read data and convert it to Json File
    def cv_to_json_converter(self, file_path):
        try:
            # read in data
            data = pd.read_csv(file_path)
            # drop the index column
            data.reset_index(drop=True, inplace=True)
            # converting df to json
            records = list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)


# test wether data has been push to atlass cloud
if __name__ == "__main__":
    FILE_PATH = "network_data\phisingData.csv"
    DATABASE = "network_security_db"
    Collection = "NetworkData"
    networkobj = NetworDataExtract()
    records = networkobj.cv_to_json_converter(file_path=FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)
