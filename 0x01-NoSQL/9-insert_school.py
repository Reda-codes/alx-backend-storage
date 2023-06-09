#!/usr/bin/env python3
""" insert_school: Python function that inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    ''' insert_school function'''
    newDict = {key: value for key, value in kwargs.items()}
    _id = mongo_collection.insert_one(newDict)
    return _id.inserted_id
