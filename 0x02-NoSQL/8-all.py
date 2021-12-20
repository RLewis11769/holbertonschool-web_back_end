#!/usr/bin/env python3
""" Holds function for listing all documents in a collection """
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Returns all documents in a collection

    Args:
        mongo_collection: pymongo.collection.Collection instance
    """
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.find()
