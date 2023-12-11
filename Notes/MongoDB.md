Example: MongoDB

* Document-based database system

* Basic unique of storage: Document
  * Very similar to JSON
  * With some additional data type support (e.g. data, binary data, code)
  * Each document need to have an "_id" field (can be auto-generated)
  * Each document have a size limit : 16 MB (in Mongo DB 4.0)
* Collection: A group of Documents
  * No requirement that each document have the same schema
  * But there are advantages (in terms of implementation, and potential efficiency)
  * One can name sub-collections of a collection
* Database: A group of collections
  * Typically an application will use one database



# How to install MongoDB



Community Edition

Local MongoDB instance on Default port 

Run mongoose without any command-line options to connect to a MongoDB instance running on your local host with default port 27017;



Which means when you input the 

```shell
mongosh
```

in your terminal, and the MongoDB start.



Now when input web browser

```
http://localhost:27017/
```

you will see the 

![Screen Shot 2022-08-31 at 16.03.05](MongoDB.assets/Screen%20Shot%202022-08-31%20at%2016.03.05.png)

which means it is successful.



## How to start

mongod --config /usr/local/etc/mongod.conf --fork



## How to create a new database and collection

```shell
use myNewDatabase
db.myCollection.insertOne( { x: 1 });
```



![Screen Shot 2022-08-31 at 16.14.32](MongoDB.assets/Screen%20Shot%202022-08-31%20at%2016.14.32.png)



## MongoDB: Insert

* Insertions:

  `db.collection.insertOne({...})`

  `db.collection.insertMany([{...}, {...}, ..., {...}])`

* Notice that the only automatic check is unique `_id`

  * No notion of referential integrity

  * No checking of name of keys (since we do not assume any scheme [even within a collection])

  * It's the (virtually all) developer's responsibility to ensure everything works.

    



### How to insert a single document

To inset a single document, use `db.collection.insertOne()`. 

This means inserting a single document into a collection.

The `insertOne` method has the following syntax:

```sh
db.collection.insertOne(
	<document>,
	{
		writeConcern: <document>
	}
)
```

| Parameter      | Type     | Description                                                  |
| -------------- | -------- | ------------------------------------------------------------ |
| `document`     | document | A document to insert into the collection.                    |
| `writeConcern` | document | Optional. A document expressing the write concern. Omit to use the default write concern. <br /> Do not explicitly set the write concern for the operation if run in a transaction. To use write concern with transactions, see [Transactions and Write Concern](https://www.mongodb.com/docs/manual/core/transactions/#std-label-transactions-write-concern) |

```shell
myNewDatabase> use sample_mflix
switched to db sample_mflix
sample_mflix> db.movies.insertOne()
sample_mflix> db.movies.insertOne({ title: "The Favourite", genres: [ "Drama", "History"], runtime: 121, rate: "R", year: 2018, directors: [ "yorgos Lanthimos"], cast: ["Olivia Colman", "Emma Stone", "Rachel Weisz"], type: "movie"})
{
  acknowledged: true,
  insertedId: ObjectId("630fd59f1b00413b25d74bba")
}
sample_mflix> show dbs
admin           40.00 KiB
config         108.00 KiB
local           40.00 KiB
myNewDatabase   40.00 KiB
sample_mflix    40.00 KiB
sample_mflix> db.movies.find( { title: "The Favourite" } )
[
  {
    _id: ObjectId("630fd59f1b00413b25d74bba"),
    title: 'The Favourite',
    genres: [ 'Drama', 'History' ],
    runtime: 121,
    rate: 'R',
    year: 2018,
    directors: [ 'yorgos Lanthimos' ],
    cast: [ 'Olivia Colman', 'Emma Stone', 'Rachel Weisz' ],
    type: 'movie'
  }
]

```



![Screen Shot 2022-08-31 at 16.46.26](MongoDB.assets/Screen%20Shot%202022-08-31%20at%2016.46.26.png)



Returns: 

```shell
{
  acknowledged: true,
  insertedId: ObjectId("630fd59f1b00413b25d74bba")
}
```

* A boolean `acknowledged` as `true` if the operation ran with write concern or `false` if write concern was disabled.
* A field `insertedId` with the `_id` value of the inserted document.

`id` field

If the document does not specify an `_id` field, then `mongod` will add the `_id` field and assign a unique `ObjectId()` for the document before inserting. Most drivers create an Objectld and insert the `_id` field, but the `mongod` will create and populate the `_id` if the driver or application does not. If the document contains an `_id` field, the `_id` value must be unique within the collection to avoid duplicate key error.





### Insert Multiple Documents

`db.collection.insertMany()` can insert multiple documents into a collection.

```shell

sample_mflix> db.movies.insertMany([ { title: "Jurassic World: Fallen Kingdom", genres: [ "Action", "Sci-Fi" ], runtime: 130, rated: "PG-13", year: 2018, directors: [ "J. A. Bayona"], cast: ["Chris Pratt", "Bryce Dallas Howard", "Rafe Spall"], type: "move" }, { title: "Tag", genres: [ "Comedy", "Action" ], runtime: 105, rated: "R", year: 2018, directors: [ "Jeff Tomsic" ], cast: ["Annabelle Wallis", "Jeremy Renner", "Jon Hamm" ], type: "movie" } ])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId("631004cc1b00413b25d74bbb"),
    '1': ObjectId("631004cc1b00413b25d74bbc")
  }
}
sample_mflix> db.movies.find( {} )
[
  {
    _id: ObjectId("630fd59f1b00413b25d74bba"),
    title: 'The Favourite',
    genres: [ 'Drama', 'History' ],
    runtime: 121,
    rate: 'R',
    year: 2018,
    directors: [ 'yorgos Lanthimos' ],
    cast: [ 'Olivia Colman', 'Emma Stone', 'Rachel Weisz' ],
    type: 'movie'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbb"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'move'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbc"),
    title: 'Tag',
    genres: [ 'Comedy', 'Action' ],
    runtime: 105,
    rated: 'R',
    year: 2018,
    directors: [ 'Jeff Tomsic' ],
    cast: [ 'Annabelle Wallis', 'Jeremy Renner', 'Jon Hamm' ],
    type: 'movie'
  }
]
sample_mflix> 
```

![Screen Shot 2022-08-31 at 20.04.13](MongoDB.assets/Screen%20Shot%202022-08-31%20at%2020.04.13.png)



## MongoDB: Query -- selection

* Basic method: find()
* `db.collection.find( {<selection>}. {<projection>} )`
  * Describe the documents to be retrieved
  * Each of this has the same format as a document (but without the_id).
* `db.collection.find({})`
  * Return all documents in the collection
* `db.collection.find({"name" : "john doe", "age" : 30})`
  * Return all documents that have BOTH key value pairs
  * Logical And
* Note:
  * Value in the key/value pair in find must be a constant.
  * Need other constructs to relate different documents from the same/different collections



### Read All Documents in a Collection

`db.collection.find()` method in the MongoDB shell to query documents in a collection.

To return all documents from the `sample_mflix.movies` collection:

``` shell
use sample_mflix
do.movies.find()
```

This operation is equivalent to the following SQL statement:

```sql
SELECT * FROM movies
```



```shell
sample_mflix> use sample_mflix
already on db sample_mflix
sample_mflix> db.movies.find()
[
  {
    _id: ObjectId("630fd59f1b00413b25d74bba"),
    title: 'The Favourite',
    genres: [ 'Drama', 'History' ],
    runtime: 121,
    rate: 'R',
    year: 2018,
    directors: [ 'yorgos Lanthimos' ],
    cast: [ 'Olivia Colman', 'Emma Stone', 'Rachel Weisz' ],
    type: 'movie'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbb"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'move'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbc"),
    title: 'Tag',
    genres: [ 'Comedy', 'Action' ],
    runtime: 105,
    rated: 'R',
    year: 2018,
    directors: [ 'Jeff Tomsic' ],
    cast: [ 'Annabelle Wallis', 'Jeremy Renner', 'Jon Hamm' ],
    type: 'movie'
  }
]
sample_mflix> 
```



![Screen Shot 2022-08-31 at 22.01.58](MongoDB.assets/Screen%20Shot%202022-08-31%20at%2022.01.58.png)



e.g. 

```shell
sample_mflix> db.movies.find({directors: "J. A. Bayona"})
[
  {
    _id: ObjectId("631004cc1b00413b25d74bbb"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'move'
  }
]
sample_mflix> 
```

![Screen Shot 2022-09-02 at 16.59.48](MongoDB.assets/Screen%20Shot%202022-09-02%20at%2016.59.48.png)



### Specify Equality Condition

To select documents which match an equality condition, specify the condition as a `<field> : <value> ` pair in the query filter document.



To return all movies where the `titile` equals `Titanic` from the `sample_mflix.movies` collection:

```shell
use sample_mflix

db.movies.find( { "title": "Titanic"} )
```

This operation corresponds to the following SQL statement:

```sql
SELECT * FROM moives WHERE title = "Titanic"
```



```shell
sample_mflix> db.movies.find({ title: "The Favourite"})
[
  {
    _id: ObjectId("630fd59f1b00413b25d74bba"),
    title: 'The Favourite',
    genres: [ 'Drama', 'History' ],
    runtime: 121,
    rate: 'R',
    year: 2018,
    directors: [ 'yorgos Lanthimos' ],
    cast: [ 'Olivia Colman', 'Emma Stone', 'Rachel Weisz' ],
    type: 'movie'
  }
]
sample_mflix> db.movies.find({ runtime: 130})
[
  {
    _id: ObjectId("631004cc1b00413b25d74bbb"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'move'
  }
]
sample_mflix> db.movies.find({ directors: "jeff Tomsic"})
```

P.S must be this way`<field>: <value>` , if not, it would not jump out any thing llike the last line above.



![Screen Shot 2022-08-31 at 22.33.50](MongoDB.assets/Screen%20Shot%202022-08-31%20at%2022.33.50.png)



### Specify Conditions Using Query Operators

Use query operatros in a query filter document to perform more complex comparisons and evaluations. Query operators in a query filter document have the following form:

```shell
{ <field>: { <operator1>: <value>}, ...}
```



To return all movies from the `sample_mflix.movies` collection which are either reted`PG` or `PG-13`:

```shell
use sample_mflix
db.movies.find( { rated: { $in: [ "PG", "PG-13"] } } )
```

This operation corresponds to the following SQL statement:

```sql
SELECT * FROM movies WHERE rated in ("PG", "PG-13")
```

NOTE: Although you can express this query using the `$or ` operator, use the `$in` operator rather than the `$or` operator when performing equality checks on the same field.

```shell
sample_mflix> db.movies.find( { rated: { $in: [ "PG", "PG-13"] } } )
[
  {
    _id: ObjectId("631004cc1b00413b25d74bbb"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'move'
  }
]

```



![Screen Shot 2022-08-31 at 23.32.29](MongoDB.assets/Screen%20Shot%202022-08-31%20at%2023.32.29.png)



### Sepcify Logical Operators (`AND`/`OR`)

A compound query can specify conditions for more than one field in the collection's documents. Implicitly, a logical `AND` conjunction connects the clauses of a compound query so that the query selects the documents in the collection that match all the conditions.



To return movies which were in 2018 **and** have an runtime at least 122:

```shell
sample_mflix> db.movies.find( { year: 2018 })
[
  {
    _id: ObjectId("630fd59f1b00413b25d74bba"),
    title: 'The Favourite',
    genres: [ 'Drama', 'History' ],
    runtime: 121,
    rate: 'R',
    year: 2018,
    directors: [ 'yorgos Lanthimos' ],
    cast: [ 'Olivia Colman', 'Emma Stone', 'Rachel Weisz' ],
    type: 'movie'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbb"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'move'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbc"),
    title: 'Tag',
    genres: [ 'Comedy', 'Action' ],
    runtime: 105,
    rated: 'R',
    year: 2018,
    directors: [ 'Jeff Tomsic' ],
    cast: [ 'Annabelle Wallis', 'Jeremy Renner', 'Jon Hamm' ],
    type: 'movie'
  }
]
sample_mflix> db.movies.find( { year: 2018, "runtime": { $gte: 122} })
[
  {
    _id: ObjectId("631004cc1b00413b25d74bbb"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'move'
  }
]
sample_mflix> 
```

![Screen Shot 2022-09-02 at 16.47.54](MongoDB.assets/Screen%20Shot%202022-09-02%20at%2016.47.54.png)



Use the `or` operator to specify a compound query that joins each clause with a logical `OR` conjunction so that the query selects the documents in the collection that match at least one condition.

```shell
sample_mflix> db.movies.find({
... year: 2018,
... $or: [{"runtime": {$gte: 122}}, {genres: "Drama"}]
... })
[
  {
    _id: ObjectId("630fd59f1b00413b25d74bba"),
    title: 'The Favourite',
    genres: [ 'Drama', 'History' ],
    runtime: 121,
    rate: 'R',
    year: 2018,
    directors: [ 'yorgos Lanthimos' ],
    cast: [ 'Olivia Colman', 'Emma Stone', 'Rachel Weisz' ],
    type: 'movie'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbb"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'move'
  }
]
sample_mflix> 
```



![Screen Shot 2022-09-02 at 16.53.16](MongoDB.assets/Screen%20Shot%202022-09-02%20at%2016.53.16.png)





## MongoDB: Query -- projection

* `db.collection.find({"name": "john doe"},{"name":1, "age": 1})` 
  * Return all documents that have key value pair (name: John doe), and output the name and the age 
* `db.collection.find({"name": "john doe",{"name":0, "age": 1}})`
  * Return all documents that have key value pair (name: John doe), and output age, but not the name
* Note: 
  * `_id` : is output by default
  * Can suppress it by including `{"_id":0}` in the projection clause



## MongoDB: Query -- selection clauses 

* `db.collection.find({"name": "john doe", "age": {"$gte": 18}})`
  * Return all documents have name John doe, and is at least 18 years old (gte = greater than or equal to)
  * Clause: a document, the key is a reserved word starting with`$`, to denote special condition or functions
* `db.collection.find({"name": "john doe", "age": {"Sgte":18, "$lte": 22}})`
  * Return all documents that have name John Doe, and is between 18 and 22 (lte = less than or equal to)



## MongoDB: Query -- OR/ NOT

* `db.collection.find({"dept": "CS", {$or, [{"age": {"$gte": 18}}, {"gpa": 4.0} ] } })`
  * Return all documents that have dept = "CS" and either age is >= 18, or age = 4.0
  * Notice that the term following or is an list (array) of conditions.
* `db.collection.find({"dept": "CS", {$not, {"gpa": 4.0}}})`
  * Return all documents that have dept = "CS" and gpa $\neq$4.0 



## MongoDB: Query -- NULL values

* BE VERY CAREFUL!
* Suppose your collection has the following docutments:
  * `{"_id": "1", "name": "john doe", "phone": null}`
  * `{"_id": "2", "name": "jack doe", "age": 28}`
* `db.collection.find({"phone": null})` will return BOTH documents
  * Null matches either "having the value null", and "no such key exists in the document"
  * Use the "$exists" clause to compensate



## MongoDB: Query -- Arrays



## MongoDB: Query -- Embedded documents



## MongoDB: Query -- More complicated issues



## MongoDB: Updates and Delete

* `db.collection.updateOne()`
* `db.collection.updateAll()`
* `db.collection.replaceOne()`
* `db.collection.replaceAll()`
  * Two parameters
    * First one is the query conditon to specify which document(s) in the collection is to be updated
    * Second one specify how the document is to be updated/ or what to replace the document with
    * For replacement, the "_id" will not change, but everything else will be replaced
    * Also an "upsert" option: try to update, if the document to be updated is not found, then insert a new document.



The MongoDB shell provides the following methods to update documents in a collection:

* To update a single document, use 

  `db.collection.updateOne()`

* To update multiple document, use

  `db.collection.updateMany()`

* To replace a document, use

  `db.collection.replaceOne()`





### Update Operator Syntax

To update a document, MongoDB provides update operators, such as `$set`, to modify field values.

To use the update operators, pass to the update methods an update document of the form:

``` shell
{
	<update operator>: { <field1>: <value1>, ...},
	<update operator>: { <field2>: <value2>, ...},
	...
}
```

Some update operators, such as `$set`, create the field if the field does not exist.



### Update a Single Document

Use the `db.collection.updateOne()` method to update the first document that matches a specified filter.

Note: MongoDB preserves a natural sort order for documents. This ordering is an internal implementation feature, and you should not rely on any particular structure within it.

**Example**: To update the first document in the `sample_mflix.movies` collection where `title` equals `Tag`.

```shell
sample_mflix> db.movies.updateOne( { title: "Tag" }, { $set: { plot: "One month every year, five highly competitive friends hit the ground running for a no-holds-barred game of tag"}} )
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
sample_mflix> db.movies.find()
[
  {
    _id: ObjectId("630fd59f1b00413b25d74bba"),
    title: 'The Favourite',
    genres: [ 'Drama', 'History' ],
    runtime: 121,
    rate: 'R',
    year: 2018,
    directors: [ 'yorgos Lanthimos' ],
    cast: [ 'Olivia Colman', 'Emma Stone', 'Rachel Weisz' ],
    type: 'movie'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbb"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'move'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbc"),
    title: 'Tag',
    genres: [ 'Comedy', 'Action' ],
    runtime: 105,
    rated: 'R',
    year: 2018,
    directors: [ 'Jeff Tomsic' ],
    cast: [ 'Annabelle Wallis', 'Jeremy Renner', 'Jon Hamm' ],
    type: 'movie',
    plot: 'One month every year, five highly competitive friends hit the ground running for a no-holds-barred game of tag'
  }
]
sample_mflix> 

```

![Screen Shot 2022-09-02 at 18.39.31](MongoDB.assets/Screen%20Shot%202022-09-02%20at%2018.39.31.png)



### Update Multiple Documents

Use the `db.collection.update.Many()` to update all documents that match a specified filter.

Example: To update all documents in the `sample_mflix.movies` collection to update where `year` is less than 2019

```shell
sample_mflix> db.movies.updateMany({year: {$lt: 2019 }}, {$set: {timetype: "old"}})
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 3,
  modifiedCount: 3,
  upsertedCount: 0
}
sample_mflix> db.movies.find()
[
  {
    _id: ObjectId("630fd59f1b00413b25d74bba"),
    title: 'The Favourite',
    genres: [ 'Drama', 'History' ],
    runtime: 121,
    rate: 'R',
    year: 2018,
    directors: [ 'yorgos Lanthimos' ],
    cast: [ 'Olivia Colman', 'Emma Stone', 'Rachel Weisz' ],
    type: 'movie',
    timetype: 'old'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbb"),
    title: 'Jurassic World: Fallen Kingdom',
    genres: [ 'Action', 'Sci-Fi' ],
    runtime: 130,
    rated: 'PG-13',
    year: 2018,
    directors: [ 'J. A. Bayona' ],
    cast: [ 'Chris Pratt', 'Bryce Dallas Howard', 'Rafe Spall' ],
    type: 'move',
    timetype: 'old'
  },
  {
    _id: ObjectId("631004cc1b00413b25d74bbc"),
    title: 'Tag',
    genres: [ 'Comedy', 'Action' ],
    runtime: 105,
    rated: 'R',
    year: 2018,
    directors: [ 'Jeff Tomsic' ],
    cast: [ 'Annabelle Wallis', 'Jeremy Renner', 'Jon Hamm' ],
    type: 'movie',
    plot: 'One month every year, five highly competitive friends hit the ground running for a no-holds-barred game of tag',
    timetype: 'old'
  }
]
sample_mflix> 
```



![Screen Shot 2022-09-02 at 18.53.49](MongoDB.assets/Screen%20Shot%202022-09-02%20at%2018.53.49.png)



### Replae a Document

To replace the entire content of a document except for the `_id` field, pass on entirely new document as the second argument to `db.collection.replaceOne()`.

When replacing a document, the replacement document must contain only field/value pairs. Do not include update operators expressions.

The replacement document can have different fields from the original document. In the replacement document, you can omit the `_id` field since the `_id` field is immutable; however, if you do include the `_id` field, it must have the same value as the current value.





## Other aspects



### P.S 

`_id` can not be duplicated 

![Screen Shot 2022-09-02 at 17.12.37](MongoDB.assets/Screen%20Shot%202022-09-02%20at%2017.12.37.png)

1. 