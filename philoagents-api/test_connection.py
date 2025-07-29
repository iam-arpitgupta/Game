from pymongo import MongoClient
from src.philoagents.config import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB_NAME]
print(db.list_collection_names())
