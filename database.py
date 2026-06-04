from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["moodDB"]
collection = db["history"]

def save_data(data):
    collection.insert_one(data)