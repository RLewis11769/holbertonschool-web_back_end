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
        # Update_one meaning only one document will be updated
        # Matched_count meaning how many updated (happens to each)
        return mongo_collection.update_one(
            {'name': name},
            {'$set': {'topics': topics}}
        )
