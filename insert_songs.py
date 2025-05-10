import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.songs_db
songs_collection = db.songs

# Open the songs.json file and load the data
with open('songs.json') as file:
    songs = json.load(file)
    songs_collection.insert_many(songs)

print("Data inserted successfully")

