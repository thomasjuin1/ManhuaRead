from pymongo import MongoClient
import os
from os import environ as env
import logging

def get_database():

   CONNECTION_STRING = ('mongodb://root:password@mongo:27017/?authMechanism=DEFAULT')
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   if (CONNECTION_STRING == None):
      print("No connection string")
      return None

   client = MongoClient(CONNECTION_STRING)
   if (client == None):
      print("No client")
      return None

   # Create the database for our example (we will use the same database throughout the tutorial
   print("Database connected")
   return client['ManhuaDB']

if __name__ == "__main__":

   # Get the database
   dbname = get_database()