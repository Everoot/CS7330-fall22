# connect mongodb
import csv
import json

import pymongo
from bson.json_util import dumps
from pymongo import MongoClient


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
# print(dbname.list_collection_names())

restaurant = dbname['restaurant']
match = dbname['match']
supplier = dbname['supplier']
# print(restaurant.find_one())
# print(dumps(restaurant.find_one(), indent=2))

with open("command.csv", "r") as cf:
    reader = csv.reader(cf)
    command = []
    for i in reader:
        command.append(i)
    # print(command)
# print(command[0][1])

length = len(command)
# print(length)  # 8
savePath = 'result2_Bingying_Liang.txt'
f = open(savePath, 'w')
for i in range(length):  # i 0, 1 , 2, 3,
    if int(command[i][0]) == 0:
        if match.count_documents({"restaurant_name": command[i][1],
                                  "supplier_name": command[i][2],
                                  "food": command[i][3],
                                  "country": command[i][4]}) == 0:
            match.insert_one({"restaurant_name": command[i][1],
                              "supplier_name": command[i][2],
                              "food": command[i][3],
                              "country": command[i][4]})
            print("Successful insertion" + "\n")
            f.write("Successful insertion" + "\r\n")
        else:
            #   dbname["match"].collection.update_one(command[0][1], upsert= True)
            print("Info already exists" + "\n")
            f.write("Info already exists" + "\r\n")

    if int(command[i][0]) == 1:
        if match.count_documents({"restaurant_name": command[i][1],
                                  "supplier_name": command[i][2],
                                  "food": command[i][3],
                                  "country": command[i][4]}) == 0:
            print("Info does not exist" + "\n")
            f.write("Info does not exists" + "\n")
        else:
            match.delete_one({"restaurant_name": command[i][1],
                              "supplier_name": command[i][2],
                              "food": command[i][3],
                              "country": command[i][4]})
            print("Successful Deletion" + "\n")
            f.write("Successful Deletion" + "\n")

    if int(command[i][0]) == 2:
        if restaurant.count_documents({"restaurant_name": command[i][1]}) == 0:
            print("Not found" + "\n")
            f.write("Not found" + "\r\n")
        else:
            # first
            restaurant_detail = restaurant.find({"restaurant_name": command[i][1]})
            restaurant_detail = (list(restaurant_detail))[0]
            city = restaurant_detail["city"]
            state = restaurant_detail["state"]
            print(command[i][1])
            print(city + " " + state + "\t")
            f.write(command[i][1] + "\r\n")
            f.write(city + " " + state + "\r\n")

            # second
            if match.count_documents({"restaurant_name": command[i][1]}) == 0:
                print("Not found" + "\n")
                f.write("Not found" + "\r\n")

            else:
                match_restaurant = list(match.find({"restaurant_name": command[i][1]}))  # match中查找相应餐馆 返回
                food_number = len(match_restaurant)  # 符合条件的餐馆数 即 记录数
                # diff food or diff supplier
                # when same food just put the suppliers in the same line
                food_set = set()
                for i in range(0, food_number):
                    food = (match_restaurant[i])["food"]  # 对应的食物
                    if food in food_set:
                        continue
                    else:
                        # print(food)
                        # 在supplier 中寻找提供这种食物的供应商
                        supplier_foodlist = list(supplier.find({"supplier_food": {"$elemMatch": {"food": food}}}))
                        supplier_sum = len(supplier_foodlist)
                        print(food + " ", end="")
                        f.write(food + " ")
                        for j in range(0, supplier_sum):
                            supplierfoodname = (supplier_foodlist[j])["supplier_name"]
                            print(supplierfoodname + " ")
                            f.write(supplierfoodname + " ")
                        f.write("\r\n")
                    food_set.add(food)
                print("\n")

    if int(command[i][0]) == 3:
        if match.count_documents({"food": command[i][1]}) == 0:
            print("Not found" + "\n")
            f.write("Not found" + "\n")
        else:
            match_detail = list(match.find({"food": command[i][1]}))[0]
            restaurant_name = match_detail["restaurant_name"]

            restaurant_detail = list(restaurant.find({"restaurant_name": restaurant_name}))[0]
            city1 = restaurant_detail["city"]
            state1 = restaurant_detail["state"]
            print(restaurant_name + " " + city1 + " " + state1 + "\n")
            f.write(restaurant_name + " " + city1 + " " + state1 + "\n")

    f.write("-----------------------------" + "\r\n")

# read in mongodb and write in the txt

restaurant_details = restaurant.find()
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
match_details = match.find()
match_result = dumps(match_details, indent = 4)
print(match_result)
f.write(match_result + "\r\n")
# for item in list(match_details):
#     print(item)
#     f.write(str(item) + '\n')
#
# f.write('\n')  # 华丽分割线

f.write("-----------------------------" + "\r\n")
supplier_details = supplier.find()
supplier_result = dumps(supplier_details, indent = 4)
print(supplier_result)
f.write(supplier_result + "\r\n")
# for item in list(supplier_details):
#     print(item)
#     f.write(str(item) + '\n')

f.close()
