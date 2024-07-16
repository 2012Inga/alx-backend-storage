#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError
from pymongo.collection import Collection

def insert_documents(collection: Collection, documents: list):
    """Inserts documents into the MongoDB collection if they do not already exist."""
    for doc in documents:
        try:
            collection.insert_one(doc)
            print(f"Inserted document: {doc}")
        except DuplicateKeyError:
            print(f"Document {_id} already exists.")

def list_all(mongo_collection):
    """Lists all documents in a collection."""
    return [doc for doc in mongo_collection.find()]

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.my_db
    school_collection = db.school

    # Define the documents to insert if they do not exist
    initial_documents = [
        {"_id": ObjectId("5a8f60cfd4321e1403ba7ab9"), "name": "Holberton school"},
        {"_id": ObjectId("5a8f60cfd4321e1403ba7aba"), "name": "UCSD"}
    ]

    # Insert documents if they are not already present
    insert_documents(school_collection, initial_documents)

    # Retrieve and print all documents in the collection
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
