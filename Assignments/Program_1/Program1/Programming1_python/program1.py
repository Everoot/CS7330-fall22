import csv
import json
# connect mongodb
from pymongo import MongoClient
from bson.json_util import dumps
import bson
def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://eve2022:abcd1234@cluster0.xvxhn6q.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['homework']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database
    dbname = get_database()

dbname = get_database()
dbname["restaurant"].drop()
dbname["match"].drop()
dbname["supplier"].drop()
collection_name1 = dbname["restaurant"]
collection_name2 = dbname["match"]
collection_name3 = dbname["supplier"]


# restaurant json
with open("restaurant.csv", "r") as rf:
    reader = csv.reader(rf)
    restaurant = []
    for row in reader:
        restaurant.append({"restaurant_name": row[0], "city": row[1], "state": row[2]})

with open("restaurant.json", "w") as rf:
    json.dump(restaurant, rf, indent=4)

# match json
with open("match.csv", "r") as mf:
    reader = csv.reader(mf)
    match = []
    for row in reader:
        match.append({"restaurant_name": row[0], "supplier_name": row[1], "food": row[2], "country": row[3]})

with open("match.json", "w") as mf:
    json.dump(match, mf, indent=4)

# supplier json
with open("supplier.csv", "r") as sf:
    reader = csv.reader(sf)
    supplier = []
    for row in reader:
        data = []
        x = int(row[3])  # 3
        i = 0
        while i < x:
            data.append({"food": row[4 + 2 * i], "country": row[4 + 2 * i + 1]})
            i = i + 1

        supplier.append({"supplier_name": row[0], "supplier_city": row[1], "supplier_state": row[2],
                         "supplier_number": row[3], "supplier_food": data})

with open("supplier.json", "w") as sf:
    json.dump(supplier, sf, indent=4)

# write in mongodb
with open("restaurant.json", 'r') as rf:
    restaurant_data = json.load(rf)
collection_name1.insert_many(restaurant_data)

with open("match.json", 'r') as mf:
    match_data = json.load(mf)
collection_name2.insert_many(match_data)

with open("supplier.json", 'r') as sf:
    supplier_data = json.load(sf)
collection_name3.insert_many(supplier_data)

# read in mongodb and write in the txt
savePath = 'result_Bingying_Liang.txt'
f = open(savePath, 'w')

# restaurant_details = collection_name1.find()
# res = list(restaurant_details)
#
# for item in res:
#     print(item)
#     f.write(str(item)+'\n')
#
# f.write('\n')    # 华丽分割线
#
# match_details = collection_name2.find()
# for item in list(match_details):
#     print(item)
#     f.write(str(item)+'\n')
#
#
# f.write('\n')   # 华丽分割线
#
# supplier_details = collection_name3.find()
# for item in list(supplier_details):
#     print(item)
#     f.write(str(item)+'\n')

restaurant_details = collection_name1.find()
restaurant_result = dumps(restaurant_details, indent=4)
print(restaurant_result)
f.write(restaurant_result + "\r\n")
# res = list(restaurant_details)
#
# for item in res:
#     print(item)
#     f.write(str(item) + '\n')

# 华丽分割线
f.write("-----------------------------" + "\r\n")
match_details = collection_name2.find()
match_result = dumps(match_details, indent = 4)
print(match_result)
f.write(match_result + "\r\n")

# 华丽分割线
f.write("-----------------------------" + "\r\n")
supplier_details = collection_name3.find()
supplier_result = dumps(supplier_details, indent = 4)
print(supplier_result)
f.write(supplier_result + "\r\n")

f.close()
