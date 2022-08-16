#!/usr/bin/env python3
""" Python function that inserts a
    new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Returns the new _id
    """
    if kwargs is not None:
        id = mongo_collection.insert_one(kwargs)
        return id
    return None
