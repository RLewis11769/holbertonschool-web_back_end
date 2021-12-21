#!/usr/bin/env python3
""" Returns list of school with specific topic """
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ Returns list of schools with specific topic in topics document """
    if mongo_collection is None:
        return []
    else:
        return mongo_collection.find({'topics': topic})
