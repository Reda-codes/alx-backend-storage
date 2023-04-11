#!/usr/bin/env python3
""" 8-all: Python function that lists all documents in a collection """


def list_all(mongo_collection):
    ''' list_all function'''
    cursor = mongo_collection.find()
    return list(cursor)
