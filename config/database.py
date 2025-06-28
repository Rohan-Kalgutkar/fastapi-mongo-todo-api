# from pymongo import MongoClient

# client=MongoClient("mongodb+srv://ronkalgutkar38:dbzY9vwIuGjbXzgK@cluster0.mldyac3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


# db=client.todo_db

# collection_name = db["todo_collection"]


from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client= MongoClient(MONGO_URI)

try:
    client.admin.command("ping")
    print("✅ Connected to MongoDB successfully.")
except Exception as e:
    print("❌ Could not connect to MongoDB:", e)

db = client.todo_db
collection_name = db["todo_collection"]
