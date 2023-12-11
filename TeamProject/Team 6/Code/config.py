DATABASE = 'Project6'
USERNAME = 'localhost'
PASSWORD = '27017'
MONGO_URI = "mongodb://{}:{}/{}".format(USERNAME, PASSWORD, DATABASE)
#
# from pymongo import MongoClient
# cli = MongoClient()

# import pymongo
# from pymongo.server_api import ServerApi
#
# client = pymongo.MongoClient("mongodb+srv://localhost:27017123456@cluster0.dx6kiep.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
# #db2 = client.test
# # MONGO_URI = "mongodb+srv://localhost:27017123456@cluster0.dx6kiep.mongodb.net/?retryWrites=true&w=majority"
# #print(db2)
