import pymongo
import certifi
import os

ca = certifi.where()

mongo_db_url = os.getenv("MONGODB_URL")
client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
try:
    client.admin.command('ping')
    print("MongoDB connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
