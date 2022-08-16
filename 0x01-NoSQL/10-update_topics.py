#!/usr/bin/env python3
""" Python function that changes all
topics of a school document based on the name:
"""


def update_topics(mongo_collection, name, topics):
    """
    Returns the new _id
    """
    query = {"name": name}
    doc_update = {"$set": {"topics": topics}}
    id = mongo_collection.update_many(query, doc_update)
    return id
