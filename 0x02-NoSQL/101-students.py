#!/usr/bin/env python3
""" Holds function for listing all students in document, ordered """
from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students in a collection
    Orders by average score on key = averageScore

    Args:
        mongo_collection: Collection instance
    """
    if mongo_collection is None:
        return []
    else:
        unwind = [
            # Break topics into individual documents
            {"$unwind": "$topics"},
            # Group  by student name
            {
                "$group":
                {
                    # idk why it's this ugly syntax but requires "_id" to group
                    # Actually grouping on name - no, there is no first name
                    "_id": "$_id",
                    "name": {"$first": "$name"},
                    # Average score for each student
                    "averageScore":
                        {"$avg": "$topics.score"}
                }
            },
            # Sort by average score
            {
                "$sort": {"averageScore": -1}
            },
        ]
        # Return students collection grouped by average score
        return mongo_collection.aggregate(unwind)
