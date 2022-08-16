#!/usr/bin/env python3
""" Funtion that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    return an empty list if no documento in the collection
    """
    documents = mongo_collection.find()
    quantity: int = 0
    for document in documents:
        quantity = quantity + 1
    if quantity == 0:
        return []
    return documents
