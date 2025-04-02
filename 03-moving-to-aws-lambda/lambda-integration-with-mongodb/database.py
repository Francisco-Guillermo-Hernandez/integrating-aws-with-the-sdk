import os
from urllib.parse import quote_plus

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class MongoDB:

    def __init__(self, databaseName):
        # Get environment variables
        AWS_ACCESS_KEY_ID = quote_plus(os.getenv('AWS_ACCESS_KEY_ID'))
        AWS_SECRET_ACCESS_KEY = quote_plus(os.getenv('AWS_SECRET_ACCESS_KEY'))
        AWS_SESSION_TOKEN = quote_plus(os.getenv('AWS_SESSION_TOKEN'))

        # Format MongoDB URI
        MONGODB_URI = f'mongodb+srv://{AWS_ACCESS_KEY_ID}:{AWS_SECRET_ACCESS_KEY}@cluster.gwsit.mongodb.net/?authSource=%24external&authMechanism=MONGODB-AWS&retryWrites=true&w=majority&authMechanismProperties=AWS_SESSION_TOKEN:{AWS_SESSION_TOKEN}&appName=Cluster'
        self.client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

        try:
            self.client.admin.command('ping')
            print('You successfully connected to MongoDB!')
            self.db = self.client[databaseName]
        except Exception as e:
            print(e)


    def close(self):
        self.client.close()
    

    def use_collection(self, collection_name):
        return self.db[collection_name]
        
        
