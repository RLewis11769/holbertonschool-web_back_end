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
    - Number of documents for top 10 most present IP addresses
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

    print("IPS:")
    # Find top 10 most present IP addresses
    top_ips = collection.aggregate([
        {
            # Group by IP address
            "$group":
            {
                "_id": "$ip",
                # Count number of documents with that IP address
                "count": {"$sum": 1}
            }
        },
        {
            # Sort by count
            "$sort": {"count": -1}
        },
        {"$limit": 10}
    ])
    # For each IP address, print number of documents with given IP address
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    stats()
