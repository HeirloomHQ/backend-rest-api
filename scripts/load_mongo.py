from pymongo import MongoClient
from pathlib import Path
from bson import json_util

print("connecting to database...")
client = MongoClient('mongodb://localhost:27017/heirloom')
db = client.heirloom
users_collection = db.user
roles_collection = db.role
memorials_collection = db.memorial
memoir_collection = db.memoir
print("connected to database")

mongo_init_dir = str(Path(__file__ + "/../mongo_init").resolve())

print("loading users...")
with open(mongo_init_dir + "/users.json", 'r') as file:
    data = json_util.loads(file.read())
    users_collection.insert_many(data)
    print("loaded users")

print("loading roles...")
with open(mongo_init_dir + "/roles.json") as file:
    data = json_util.loads(file.read())
    roles_collection.insert_many(data)
    print("loaded roles")

print("loading memorials...")
with open(mongo_init_dir + "/memorials.json") as file:
    data = json_util.loads(file.read())
    memorials_collection.insert_many(data)
    print("loaded memorials")

print("loading memoirs...")
with open(mongo_init_dir + "/memoir.json") as file:
    data = json_util.loads(file.read())
    memoir_collection.insert_many(data)
    print("loaded memoirs")

client.close()
