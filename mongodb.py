import datetime
import os

from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()

class MongoDB:
    def __int__(self):
        mongo_user = os.getenv("MONGO_USER")
        mongo_pass = os.getenv("MONGO _PASSWORD")
        self.collection = os.getenv("COLLECTION_NAME")
        mongo_hostname = os.getenv("MONGO_HOSTNAME")

        uri = f"mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_hostname}/?retryWhites=true&w=majority"
