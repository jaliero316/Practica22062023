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

        uri = f"mongodb+srv://{mongo_user}:{mongo_pass}@{mongo_hostname}/?retryWrites=true&w=majority"
        # Crea un nuevo cliente y conecta hacia el servidor#
        self.client = MongoClient(uri)
        # Envia un ping de confirmacion de que se ha logrado la conexion #
        try:
            self.client.admin.command('ping')
            print("Pinged your deployement. You succesfully connected to MongoDB!")
        except Exception as e:
            print(e)


def insert_wikipedia_text(self, title: str, text: str):
    eig_db = self.client.get_database("eig")
    col = eig_db.get_co