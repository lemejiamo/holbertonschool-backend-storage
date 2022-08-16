#!/usr/bin/env python3
""" Funtion that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    return an empty list if no documento in the collection
    """
    documents = mongo_collection.find()
    quantity = 0
    documents_list = []
    # int (type(documents))
    for document in documents:
        # int(document)
        documents_list.append(document)
        quantity = quantity + 1
    if quantity == 0:
        return []
    return documents_list
