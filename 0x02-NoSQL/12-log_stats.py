#!/usr/bin/env python3
""" Provide stats about Nginx log files stored in MongoDB """
from pymongo import MongoClient


def stats():
    """
    Count documents in collection with:
    - Database: logs
    - Collection: nginx

    Print:
    - Total number of documents in given collection
    - Number of documents with method ["GET", "POST", "PUT", "PATCH", "DELETE"]
    - Number of documents with method=GET and path=/status
    """
    # Connect to MongoDB
    client = MongoClient()
    # Get logs database
    db = client.logs
    # Get Nginx collection from logs database
    collection = db.nginx

    # Print number of total documents in the collection
    print(f"{collection.count_documents({})} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # For each method, print number of documents with that method
    for method in methods:
        print(f"\tmethod {method}: " +
              f"{collection.count_documents({'method': method})}")

    # Print number of documents with method=GET and path=/status
    print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})} \
status check")


if __name__ == "__main__":
    stats()
