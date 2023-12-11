# Chapter 14 Indexing

## Practice Exercises

**14.1 Indices speed query processing, but it is usually a bad idea to create indices on every attribute, and every combination of attributes, that are potential search keys. Explain why.**

My answer: 1. Space waste. Because not every combiantion of attributes are useful, some of them acually useless, which means if we index some useless attribute will waste a lot of space. 

2. time waste. some useless index when we are doing some seaching, we have to check all of them. Some of them are not helpful.

Answer:

Reasons for not keeping indices on every attribute include:

* Every index requires addtional CPU time and disk I/O overhead during inserts and deletions.
* Indices on non-primary keys might have to be changed on updates, althought an index on the primary key might not (this is because updates typically do not modify the primary-key attributes).
* Each extra index requires additional storage space.
* For queries which involve conditions on several search keys, efficientcy might not be bad even if only some of the keys have indices on them. Therefore, database performance is improved less by adding indices when many indices already exist.

---

**14.2 Is it possible in general to have two clustering indices on the same relation for different search keys? Explain your answer.**

My answer: Yes, because the search keys of clustering indices do not need the primary keys, others  key is ok. ❌

Answer: In general, it is not possible to have two primary indices on the same relation for different keys because the tuples in a realtion would have be stored in different order ot have the same values stored together. We could accomplish this by storing the relation twice and duplicating all values, but for a centralized system, this is not efficient.

----

**14.3 Construct a $B^+$ -tree for the following set of key values:**
$$
(2, 3, 5, 7, 11, 17, 19, 23, 29, 31)
$$
**Assume that the tree is initially empty and values are added in ascending order. Construct $B^+$-trees for the cases where the number of pointers that will fit in one node is as follows:**

**a. Four**

**b. Six**

**c. Eight**

-----

**14.4 For each $B^+$-tree of Exercise 14.3, show the form of the tree after each of the following series of operations:** 

**a. Insert 9.**
**b. Insert 10.**
**c. Insert 8.**
**d. Delete 23.**
**e. Delete 19**



