#!/usr/bin/env python3
""" Funtion that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    return an empty list if no documento in the collection
    """
    documents = mongo_collection.find()
    documents_list = [doc for doc in documents]
    if documents_list.count == 0:
        return []
    return documents_list
