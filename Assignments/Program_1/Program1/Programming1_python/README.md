# README

Program1 should be first and the program 2, because program 1 start first it will delete the whole thing in the mongodb. Just make sure the result will be the same. 

Some information about mongodb and python I used: 

Mongodb:

VERSION: 5.0.13
REGION: AWS N. Virginia (us-east-1)
CLUSTER TIER: M0 Sandbox (General)


Python 3.9.6

## Program 1

The `restaurant.csv`

```csv
Top Tier Restaurant,Houston,TX
McD,Dallas,TX
Eating Good,Dallas,GA
```



The `match.csv`

```
McD,Supplier 1,Chicken,USA
Eating Good,Great Foods,Orange,Mexico
McD,Supplier 1,Egg,Canada
Eating Good,This supplier,Orange,Mexico
```



The `supplier.csv`

```
Supplier 1,Houston,TX,3,Chicken,USA,Egg,Canada,Chicken,China
This supplier,Dallas,TX,2,Orange,Mexico,Avocado,Mexico
Great Foods,Seattle,WA,6,Orange,Mexico,Orange,USA,Banana,Panama,Banana,Italy,Frog legs,Hong Kong,Frog legs,France
```



**In the program 1**

`result_Bingying_Liang.txt`

```txt
[
    {
    
        "_id": {
            "$oid": "63530b26c8d4b3cf42b18478"
        },
        "restaurant_name": "Top Tier Restaurant",
        "city": "Houston",
        "state": "TX"
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b18479"
        },
        "restaurant_name": "McD",
        "city": "Dallas",
        "state": "TX"
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847a"
        },
        "restaurant_name": "Eating Good",
        "city": "Dallas",
        "state": "GA"
    }
]
-----------------------------
[
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847b"
        },
        "restaurant_name": "McD",
        "supplier_name": "Supplier 1",
        "food": "Chicken",
        "country": "USA"
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847c"
        },
        "restaurant_name": "Eating Good",
        "supplier_name": "Great Foods",
        "food": "Orange",
        "country": "Mexico"
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847d"
        },
        "restaurant_name": "McD",
        "supplier_name": "Supplier 1",
        "food": "Egg",
        "country": "Canada"
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847e"
        },
        "restaurant_name": "Eating Good",
        "supplier_name": "This supplier",
        "food": "Orange",
        "country": "Mexico"
    }
]
-----------------------------
[
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847f"
        },
        "supplier_name": "Supplier 1",
        "supplier_city": "Houston",
        "supplier_state": "TX",
        "supplier_number": "3",
        "supplier_food": [
            {
                "food": "Chicken",
                "country": "USA"
            },
            {
                "food": "Egg",
                "country": "Canada"
            },
            {
                "food": "Chicken",
                "country": "China"
            }
        ]
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b18480"
        },
        "supplier_name": "This supplier",
        "supplier_city": "Dallas",
        "supplier_state": "TX",
        "supplier_number": "2",
        "supplier_food": [
            {
                "food": "Orange",
                "country": "Mexico"
            },
            {
                "food": "Avocado",
                "country": "Mexico"
            }
        ]
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b18481"
        },
        "supplier_name": "Great Foods",
        "supplier_city": "Seattle",
        "supplier_state": "WA",
        "supplier_number": "6",
        "supplier_food": [
            {
                "food": "Orange",
                "country": "Mexico"
            },
            {
                "food": "Orange",
                "country": "USA"
            },
            {
                "food": "Banana",
                "country": "Panama"
            },
            {
                "food": "Banana",
                "country": "Italy"
            },
            {
                "food": "Frog legs",
                "country": "Hong Kong"
            },
            {
                "food": "Frog legs",
                "country": "France"
            }
        ]
    }
]
```



## Program 2

The `command.csv`, I use the following expamles.

```csv
0,McD,Supplier 2,Apple,USA
0,McD,Supplier 1,Chicken,USA
1,McD,Supplier 2,Apple,USA
1,McD,Supplier 2,Apple,USA
2,Top Tier Restaurant
2,Ha tea
2,McD
2,Eating Good
3,Chicken
3,Tea
```

And the result should be like the following

`0,McD,Supplier 2,Apple,USA`

```
Successful insertion
```



`0,McD,Supplier 1,Chicken,USA`

```
Info already exists
```



`1,McD,Supplier 2,Apple,USA`

```
Successful Deletion
```



`1,McD,Supplier 2,Apple,USA`

```
Info does not exists
```



`2,Top Tier Restaurant`

```
Top Tier Restaurant
Houston TX
Not found
```



`2,Ha tea`

```
Not found
```



`2,McD`

```
McD
Dallas TX
Chicken Supplier 1 
Egg Supplier 1
```



`2,Eating Good`

```
Eating Good
Dallas GA
Orange This supplier Great Foods
```



`3,Chicken`

```
McD Dallas TX
```



`3,Tea`

```
Not found
```



At the last, the output all the ducuments.



**In the program2** 

`result2_Bingying_Liang.txt`

```txt
Successful insertion
-----------------------------
Info already exists
-----------------------------
Successful Deletion
-----------------------------
Info does not exists
-----------------------------
Top Tier Restaurant
Houston TX
Not found
-----------------------------
Not found
-----------------------------
McD
Dallas TX
Chicken Supplier 1 
Egg Supplier 1 
-----------------------------
Eating Good
Dallas GA
Orange This supplier Great Foods 
-----------------------------
McD Dallas TX
-----------------------------
Not found
-----------------------------
[
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b18478"
        },
        "restaurant_name": "Top Tier Restaurant",
        "city": "Houston",
        "state": "TX"
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b18479"
        },
        "restaurant_name": "McD",
        "city": "Dallas",
        "state": "TX"
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847a"
        },
        "restaurant_name": "Eating Good",
        "city": "Dallas",
        "state": "GA"
    }
]
-----------------------------
[
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847b"
        },
        "restaurant_name": "McD",
        "supplier_name": "Supplier 1",
        "food": "Chicken",
        "country": "USA"
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847c"
        },
        "restaurant_name": "Eating Good",
        "supplier_name": "Great Foods",
        "food": "Orange",
        "country": "Mexico"
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847d"
        },
        "restaurant_name": "McD",
        "supplier_name": "Supplier 1",
        "food": "Egg",
        "country": "Canada"
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847e"
        },
        "restaurant_name": "Eating Good",
        "supplier_name": "This supplier",
        "food": "Orange",
        "country": "Mexico"
    }
]
-----------------------------
[
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b1847f"
        },
        "supplier_name": "Supplier 1",
        "supplier_city": "Houston",
        "supplier_state": "TX",
        "supplier_number": "3",
        "supplier_food": [
            {
                "food": "Chicken",
                "country": "USA"
            },
            {
                "food": "Egg",
                "country": "Canada"
            },
            {
                "food": "Chicken",
                "country": "China"
            }
        ]
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b18480"
        },
        "supplier_name": "This supplier",
        "supplier_city": "Dallas",
        "supplier_state": "TX",
        "supplier_number": "2",
        "supplier_food": [
            {
                "food": "Orange",
                "country": "Mexico"
            },
            {
                "food": "Avocado",
                "country": "Mexico"
            }
        ]
    },
    {
        "_id": {
            "$oid": "63530b26c8d4b3cf42b18481"
        },
        "supplier_name": "Great Foods",
        "supplier_city": "Seattle",
        "supplier_state": "WA",
        "supplier_number": "6",
        "supplier_food": [
            {
                "food": "Orange",
                "country": "Mexico"
            },
            {
                "food": "Orange",
                "country": "USA"
            },
            {
                "food": "Banana",
                "country": "Panama"
            },
            {
                "food": "Banana",
                "country": "Italy"
            },
            {
                "food": "Frog legs",
                "country": "Hong Kong"
            },
            {
                "food": "Frog legs",
                "country": "France"
            }
        ]
    }
]
```



