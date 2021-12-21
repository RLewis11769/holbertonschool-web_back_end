#!/usr/bin/env python3
""" Holds function for inserting new document into collection """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts new document into collection based on kwargs
    Returns id of new document

    Args:
        mongo_collection: pymongo.collection.Collection instance
        **kwargs: keyword arguments
    """
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.insert_one(kwargs).inserted_id
