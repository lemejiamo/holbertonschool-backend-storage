#!/usr/bin/env python3
""" Python function that returns the list
    of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list filter by specific topic
    """
    documents = mongo_collection.find()
    by_topic = [doc for doc in documents if topic in doc.get('topics')]
    return by_topic
