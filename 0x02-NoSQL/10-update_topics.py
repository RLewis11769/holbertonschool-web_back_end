#!/usr/bin/env python3
""" Holds function for changing all topic of document """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of document based on name

    Args:
        mongo_collection: pymongo.collection.Collection instance
        name: school name to be updated
        topics: list of strings of topics to add to document with name
    """
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.update_many(
            {'name': name},
            { '$set': {'topics': topics} }
        )
