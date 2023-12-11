# Programming Homework 1 – MongoDB

Due: 10/28 (Thu) 11:59pm

You are to implement a small database via Mongo DB.

***Restaurants, food and suppliers***

You want to store restaurants in the database. For each restaurant you record its (unique) name, and the city and state where the restaurant is located. (city name is unique within a state only).

Each restaurant will need multiple types of food to be create dishes. Notice that a type of food can come from different countries, and we also record the country of origins. For example, a restaurant may want chicken that comes from Canada, but not chicken comes from USA.

Each restaurant will need to get the food it needs from certain suppliers. For each supplier, we record its (unique) name, and the city and state where the supplier is located.

Notice that a restaurant can get the same kind of food from multiple suppliers. For instance the restaurant can obtain “chicken from Canada” from both supplier1 and supplier2. Also a restaurant can obtain multiple food from the same supplier. For instance, the restaurant can get “chicken from Canada”, “chicken from Guatemala” and “egg from Canada” from supplier1.



**Task 1 – Initialization**

For the first task, you are to read in a set of csv files that contains information to be stored, and then store them in MongoDB.

The first file is named “restaurant.csv”. Each line contains the name of a restaurant, the city and the state that it is in. Here is an example:

“Top Tier Restaurant”, “Houston”, “TX”

“McD”, “Dallas”, “TX”

“Eating Good”, “Dallas”, “GA”

The second file is named “supplier.csv”. It listed all the suppliers. Each line contains information of a supplier. The line is formatted as follows:

* The first field is the name of the supplier
* The second field is the city of the supplier
* The third field is the state of the supplier
* The fourth field is the number of food supplied by this supplier  
* Then each of the next two field correspond to a food that it supplies.

An example of the file is below:

“Supplier 1”, “Houston”, “TX”, 3, “Chicken”, “USA”, “Egg”, “Canada”, “Chicken”, “China”

“This supplier”, “Dallas”, “TX”, 2, “Orange”, “Mexico”, “Avocado”, “Mexico”

“Great Foods”, “Seattle”, “WA”, 6, “Orange”, “Mexico”, “Orange”, “USA”, “Banana”, “Panama”, “Banana”, “Italy”, “Frog legs”, “Hong Kong”, “Frog legs”, “France”

The third file is named “match.csv”. It contains information about which supplier is suppling what food to which restaurant. Each line contains the name of the restaurant, followed by the name of the supplier, followed by one food that is being supplied from that supplier to that restaurant. Notice that if a restaurant gets more than one food from a supplier, each food will be listed in a separate line. An example of the file is below:

“McD”, “Supplier 1”, “Chicken”, “USA”

“Eating Good”, “Great Foods”, “Orange”, “Mexico”

“McD”, “Supplier 1”, “Egg”, “Canada”

“Eating Good”, “This supplier”, “Orange”, “Mexico”

You are to write a program that read in the three files, and then create a database in MongoDB that store the data. At the end, your program should output all documents in the database into a text file named “result_<your last_name>_<your first name>.txt”, and then exit the program

Task 2: Modifying the database

You are to read the database that you created from MongoDB (you are NOT allowed to reread the 3 files you read from task 1). Then you will read a csv file “command.csv”, which will tell you either the modify the file and/or answer the query. Each line has the following format:

• The first field is a number which denote the command. If the number is

o

o

o

0: the rest of the line is formatted the same way as a line in “match.csv”. You are to insert the information into the database. If the insertion is successful, you should print “Successful insertion”. If not (i.e. if the information is already in the database), then print “Info already exists”.

1: the rest of the line is formatted the same way as a line in “match.csv”. You are to delete the information into the database. If the insertion is successful, you should print “Successful Deletion”. If not (i.e. if the information is already in the database), then print “Info dos not exist”.

2: the next field is the name of a restaurant. You are to output the information about the restaurant in the following format 



The first line print the name of the restaurant, followed by the city and state is it in (with every field separated by a space)

Each subsequent line will first list a food that it obtained by suppliers, and then (in the same line) list the name (only) of all the suppliers that order the food. Every word should be separated by a space.

o

o

3: the next two fields described a food. You need to print restaurants that supply that food. Each line you should print a restaurant, starting from its name, and followed by the city that it is in.

For 2 and 3, if the query return nothing, then print “Not found”.

Notice that you should execute each line immediately after reading it and before you read the next line. Also the commands can come in any order in the file.

At the end, your program should output all documents in the database into a text file named “result2_<your last_name>_<your first name>.txt”, and then exit the program.

Notes on the program

Your can choose to use either python or Java to implement your program. You are responsible to learn how to use the API for these language, and for installing it so it will work.

You SHOULD NOT implement a GUI for your programs. Each program should just read in the data and output the results either to standard output or to the file that I specified.