from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = FastAPI()

conn = MongoClient("mongodb+srv://jatinkalwar:shifaanam@mbomb.ghtntua.mongodb.net")


@app.get("/num/verify/{mobn}")
async def root(mobn):

    try:
        return conn.masbom.protect.find_one({"mob": int(mobn)} , {"mob": 1 , 'status': 1 , '_id': 0})

    except Exception as e:
        print(e)
