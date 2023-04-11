#!/usr/bin/env python3
""" Python script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(collection.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(collection.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(collection.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(collection.count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(collection.count_documents({"method": "DELETE"})))
    print("{} status check".format(collection.count_documents({"path": "/status"})))
    print("IPs:")
    print("\t172.31.63.67: {}".format(collection.count_documents({"ip": "172.31.63.67"})))
    print("\t172.31.2.14: {}".format(collection.count_documents({"ip": "172.31.2.14"})))
    print("\t172.31.29.194: {}".format(collection.count_documents({"ip": "172.31.29.194"})))
    print("\t69.162.124.230: {}".format(collection.count_documents({"ip": "69.162.124.230"})))
    print("\t64.124.26.109: {}".format(collection.count_documents({"ip": "64.124.26.109"})))
    print("\t64.62.224.29: {}".format(collection.count_documents({"ip": "64.62.224.29"})))
    print("\t34.207.121.61: {}".format(collection.count_documents({"ip": "34.207.121.61"})))
    print("\t47.88.100.4: {}".format(collection.count_documents({"ip": "47.88.100.4"})))
    print("\t45.249.84.250: {}".format(collection.count_documents({"ip": "45.249.84.250"})))
    print("\t216.244.66.228: {}".format(collection.count_documents({"ip": "216.244.66.228"})))
