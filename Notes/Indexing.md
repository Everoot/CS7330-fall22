# Indexing

## Indexing

> So you can only order by one attribute if you really want to order the file. But it doesn't mean that you can. But then it will love your search for more than one attribute. So how do we make this process faster for multiple attributes?
>
> So let's say you have a table call student, right.
>
> ```sql
> student(ID
>        name
>        age
>        height
>        gpa)
> ```
>
> Now you can order the tuples, pick an attribute you want to order to post based on. Let's say you pick an ID so you can store the files such that pupils are older by ID. Now searching for IDs. Probably. First, the binary search, whatever. But then if it turns out that a lot of your queries are based on gpa. Now, does that order help you to search based on GPA? Yes or no? NO
>
> But if I tell you your your GPA equal to I.D.Divided by 10,000. And then you like it at first like that.



> So I do have records just for the GPA. And they pointed to that record in the table that have that GPA that correspond to that student. I can order this whatever way I want and I can serve this whatever way I want, and I can.
>
> What you need to store in your index. The GPA and any pointer to the object rate debt will most likely be much smaller than a tuple.  So maybe the price is not too big to pay. There's no free lunch, but there's at least a reasonable lunch



> And as I say it, the good news, the values index always tends to be much smaller than your table, because the table where each tuple of 25 attributes, And as I say it, the good news, the values index always tends to be much smaller than your table, because the table where each tuple of 25 attributes, the index is always 1 to 1 that could build and some sort of upon the putting to the object, there is not going to be very expensive. 

> ![Screen Shot 2022-09-24 at 15.38.39](Indexing.assets/Screen%20Shot%202022-09-24%20at%2015.38.39.png)

* So far storage discussed
  * Heap file : no ordering, easy to maintain, but provide no help (speedup) in queries
  * Sequential file : help in some cases, but can be tricky to maintain, also sorting from scratch 

* Need to have something that help searching but without too much overhead to maintain

* Indices (plural for index)



* Assume we have a table

* An index is defined by a search key

  * Typically an attribute of the table
    * Denote it as the key (attribute)

  * Does <u>NOT have to be unique</u> (e.g. one can index on salary)

    > if you really want, maybe an index on gender

* An index (file) ==consists of index entries: (search key, pointer)== 

  * Search key: the value of the attribute
  
  * <u>Pointer: pointer to the next location to access the record</u>
  
    > Noctice that I'm writing it somewhat cryptically, but I do need what you want![IMG_6FC16376161D-1](Indexing.assets/IMG_6FC16376161D-1.jpeg)





* Index structure assume the tuples in a file is on secondary storage (hard drive/SSD)

* They also make no assumption on how large the index is
  * The index structure is designed such that it can be stored on secondary storage also
  
  * Or some portion of it on storage while others in main memory
  
    > Even though I say index typically much smaller than table, but itself can be pretty large. Because your original table have 10 trillion tuples, then your index might do have a lot of entries. And even though each entry small, it adds up. So moving that structure in the database context have to think about ways that I can store the index in the main memory as well as on the disk. So when we build an index, we have to keep that in mind.
  
* Since secondary storage is used, a page is a basic unit of storage and reference
  * E.g: pointer to a tuple typically only point to the page that store the data

![IMG_0454](Indexing.assets/IMG_0454.jpg)



* Two types of data structure used for indexing (called index structure)
  * Hash-based
    * Hash function is used to group data
    
    * Tuples are NOT sorted (since <u>hash function does not guarantee to maintain order</u>)
    
    * However, tuples that have the same key value will be grouped togethe
    
      > what is hash table? 
      >
      > <img src="Indexing.assets/2560px-Hash_table_3_1_1_0_1_0_0_SP.svg.png" alt="img" style="zoom: 25%;" />
      >
      >  let's say you you you want to be indexed on GPA.  you put the GPA, you do a high function. I'll put the location of. I'll put a unique value.  I'll put a value. It doesn't have to be unique. Let's say let's say I thought ten decimal well, five decimal point GPA. How many unique values are there. We are talking about 10,000 unique values. Are you going to have 10,000 buckets. Two different values, two different GPA. When you put all the hash for rate, new hash, the same number you do on the body. you will find out the unavoidable and debris system I will build will be but will will spend time on hash structure later on,
    
      > ```sql
      > select * 
      > from student
      > where id > "1234567"
      > ```
      >
      > How often do you think people will ask this query? Not very often. 
      >
      > How many of you have query tell me your I.D. My I.D. is larger than your ID, so I'm a better student than you. If more than my idea, you should buy me lunch. Now, this might happen in high school, but it. It happened here. Right. This is a joke, right? Nobody is going to do this in real life.
    
      > in so far as to build a hazard based structure is perfectly good enough.
      >
      > Now there are some attributes that are older and the ordinary is important right now.
    
  * Ordered
    * Key attributes can be ordered
    * Tuples in the table (file) are ordered via the key (like a sequential file)
    * The index structure exists to enable fast query while not being penalized for updates
    * Typically tree-based (but not binary search tree!)
    
    > ```sql
    > select * 
    > from student
    > where gpa > 3.4
    > ```
    >
    > This will be a very often occurring in this case. And in this case order is important. So that means we do need in structure that somehow order the indexing attribute. 
    >
    > Binary search tree turns out to be very lousy structure for this. So we will look at different structures for those
    
    >  Whenever I insert a couple, I'll need to update the index too. So there's always an extra cost. And your hope is that remember to maintain the order. It can be costly. You have to find a location number. And then you can you have to create a space in the middle to put this in. Your index is not careful this a very costly. So you want to build systems like that. Do you still have to really go that far?
    >
    > To give you a preview. This is typically done by something called the B plus three. There is a difference between the B tree and the B-plus tree. 
    
    

* Two ways of generating index record
* Dense index
  * Each distinct value of key have at least one index record
    * Recall for secondary index, each tuple will have one record

* Sparse index
  * Some values of key do not have any index record
    * Mostly for ordered index
    * Location of the tuples with such key can be inferred



### Dense index (example)

![image-20220922232915404](/Users/eve/Library/Application%20Support/typora-user-images/image-20220922232915404.png)

>  So let's say we want to do an index on the I.D. In this case, there is no choice because it is unique. Well, there's actually a choice. But for now, we think that there's no choice in this case.



![image-20220922232922136](/Users/eve/Library/Application%20Support/typora-user-images/image-20220922232922136.png)

> We actually assume tuples based on the department. If I do that, then my index can look something like this.
>
> These are the biology student. This is the first of the computer science students. And then. The computer science students they are more than welcome to science students buy only one key for a computer science value. If we are willing to assume that the main table is actually started by the department, you still need a valuable computer science. So this what we call a dense index.
>
> Basically every unique value. Of the indexing attribute has to have an index record.
>
>  Now the question is, does it have to be this way? If we are willing to guarantee that this is thwarted by the department, do we really need to keep each record? Index for each value?
>
> <img src="Indexing.assets/Screen%20Shot%202022-09-24%20at%2020.40.52.png" alt="Screen Shot 2022-09-24 at 20.40.52" style="zoom: 25%;" />
>
> I only have two index work in biology and history. Can I still search for things? If I look for computer science, what do I have to do? Computer science is after biology, but before history. So that means if I start from this, I will eventually hit computer science before I hit this record. Let's say physics. Physics is after history. So do I need to go full to first record? No. I can go strictly to the history and look down. Now, obviously, we are trading things here, right?
>
> But remember we are talking about a disk. We are talk about datastore tuple storing the disk and each page typically store at least a few tuples.  let's say this four tuples store in the first page. And then this five tuples in the next page and then this three tuples in the third page.
>
> <img src="Indexing.assets/Screen%20Shot%202022-09-24%20at%2020.45.02.png" alt="Screen Shot 2022-09-24 at 20.45.02" style="zoom: 50%;" />
>
> every time I go to access data from this, I'm going to access on the unit page. So every time I go to read those five people see the main memory anyway. if I don't have the computer science record, I search for biology. I'm still going to only read one page. I'm not going to read more just because a computer science record is not there. So you are not gaining anything by having the computer science record in the index.

### Sparse index (example)

![image-20220922232937289](/Users/eve/Library/Application%20Support/typora-user-images/image-20220922232937289.png)





* Two different ways for tuples to be organized under an index 
  * The tuples are ordered exactly like the search key (==**clustering index / primary index**==)
    * The tuples themselves are typically ordered by the search key 
      * For hash tables, it is not sorted, but tuples that have the same key values are typically stored together in same/adjacent page/s
    
  * The tuple are not ordered as the search key (non-clustering index / secondary index)
    * Need to have an index file,
    
      > Essentially you have to have an index file. The index file will basically be P pointer, T pointer, so on, so forth
      >
      > <img src="Indexing.assets/Screen%20Shot%202022-09-24%20at%2021.15.11.png" alt="Screen Shot 2022-09-24 at 21.15.11" style="zoom:25%;" />
      >
      > And this itself said will be organized order or some some other way. This is important. This therm is of utmost importance in database systems. What is a primary and actually a secondary index? As I say, primary and clustering here are basically interchangeable terms. When I say cluster index, I mean primary index, but I mean non cluster index I mean secondary index. 
    
    * For each tuple in the table, have a index record (key, pointer), 
    
    * key value of the key attribute for that tuple
    
    * pointer points to where the tuple is (typically the page # of the page where the tuple resides
    
    * An index is then build on the index record
    
    >  if I have in this case. I want to now build an index on department. Now I have no choice.  because everything is getting around. So literally, each tuples, I will have to have a separate record pointing to it. So I will actually do a dense index, say biology. Ponting too here sees Ponting through here.
    >
    > So in this case, which is called secondary index. We also current dense index
    >
    > <img src="Indexing.assets/Screen%20Shot%202022-09-24%20at%2021.09.51.png" alt="Screen Shot 2022-09-24 at 21.09.51" style="zoom:33%;" />
    >
    > Q: Question. Keeping the table. How many primary indexing we have?
    >
    > A: One
    >
    > But I will bet 99.9% of all the databases build your primary index based on your primary key. So most of the debate is done when you declare a primary key. They will automatically be an index. Based on this behind the scenes.





### Secondary index (example)

![image-20220922233205193](/Users/eve/Library/Application%20Support/typora-user-images/image-20220922233205193.png)

Notice that **<u>secondary index have to be dense</u>** (why?)



## Clustering vs. Non-clustering index

* What’s the significant difference between the two?
* Consider the case
  * Instructor table of 20,000 tuples
  * Assume each page can store 100 tuples
  * If there is no empty space, 200 pages
* Case 1: a clustered ordered index on salary
* Notice that the tuples are sequentially ordered by salary
* Case 2: an unclustered ordered index on salary





* Now consider the following query:

  ```sql
  SELECT * FROM instructor where salary > 100,000
  ```

* Case 1, for the clustered order index

  * First use the index to find all the page that have tuple that have the smallest salary > 100,000

  * Then read all the pages from that page onwards

  * Let say k tuples satisfies the query 

  * ==Then the number of pages read = $\frac{k}{100}$==

    * Cannot be larger than the size of the table

    > Why?
    >
    > Why can I be so sure if k over hundred. Remember, the index is cluster. On salary.
    >
    > the cluster here It's very important because the cluster index. The tuples are order by salary.  So once you find the list salary, let's say this page, unless it is all the way this order. All I have to do is read all these subsequent page and I am done. Every tuple in all subsequent pages will satisfy the query.



* Now consider the following query:

  ```sql
  SELECT * FROM instructor where salary > 100,000
  ```

* Case 2, for the unclustered order index

  * First use the index to find the page for each tuple that have the salary > 100,000
  * Then read all the pages from that page onwards
  * Let say k tuples satisfies the query 
  * Then the number of pages read = k in the worst case
  * **If k = 2, then at worst 2 page read fine**
  * **If k = 200, then worst case one have to read the whole table**
    * The index is useless

  > It depends on different situation.
  >
  > Anybody see a chicken and egg problem here? You still tell me what the chicken and egg problem is.
  >
  > You need to know the to know the best way to execute a query. You have to know how many tuples you return, in order to know how many pupils to return. You better execute a query. Isn't there a chicken and egg? That is the overwhelming question that face database people all of these tech. so people have been spending like five decades trying to solve this problem.





## Fundamental problem in query execution/optimization

* Whether you want to use an index or not depend on the size of the result of a query

But

* You do not know the size of the result unless you run the query, which you will have to decide whether to use the index

> Wheneve you want to use an index or not, depend on the size of result the query. The query return two tuples then you say a non-clustering index is perfectly okay. If you return 2000 tuples then you want to think twice before you do it. However, the problem is that you don't know the size, number of tuples to return until you actual execute a code. So that's essentially kind of a chicken and egg problem. You have to decide on how to do the query based on the size of the output. But you cannot get the size of the output and that you can execute it too.
>
> But at least I do want you to have some sense about this is the problem that we are facing that database.



## Index structures

* Two most commonly used index structure for databases
  * B+-trees
    * Modification of B-trees for databases
    * Good for ordered data
  * Hash tables
    * Modification of main memory hashing function
    * Good for exact queries (WHERE attribute = value)



> But even nowadays in relational database system, this type of using these indexes is kind of stand the test of time.
>
> One: these things might be stored on the disk
>
> And one of the biggest thing we didn't thing about when we dealing storing data is that every time we read, we are reading how much data was the basic unit of access? It's a page.
>
> A page might not be just one byte or a few byte. Typically, as we mentioned, older systems page is 256 bytes and newer system might be four or take kilobytes. So your index structure has to take advantage of the fact that, hey, I'm going to read a bunch of bugs anyway. And if you think about let's compare to a binary tree, it might be turned to every time we actually read five nodes anyway. So how does it affect the best way of using the index becoming an interesting question. So that's why you see the adaptation of these index to a display set up is one of the main reasons that we are reading an writing to and from this. And each unit of access is not a bit or a single note but a page.



> 1 Byte = 8 bit
>
> 1 KB = 1024 B
>
> 1 MB = 1024 KB
>
> 1 GB = 1024 MB
>
> 1 TB = 1028 GB



### B+-tree

![image-20220924153233452](Indexing.assets/image-20220924153233452.png)

> this is a picture of $B^+$-tree.
>
> Because it's a sencondary index, right. So the leaf have to start index record basically key and pointer to the tuple. 
>
> This is not a binary tree.
>
> So B and $B^+$ tree do not stand for binary. They stand for balance. 
>
> So what does it mean that trees will be balanced? All the leaves are at the same level.

>Next question: Is there any key that is duplicated in the tree? Do you see any string to appear more than one thing in the tree? 
>
>Yes: "Mozart", "Einstein", "Gold"
>
>Some of you may have B-trees. So in something is simliar, but it's one key difference in B-tree and $B^+$-tree is that B-tree every nodes is only store once. B-tree there's no such duplication between modes that only appear once every leaves, every tuple.

>Some leaf have two records  some leaf have three records. For these three, we assume a node can hold a free record.
>
>Here things are a little bit tricky. So Notice that we also consider the root is not internal nodes.
>
>Can you tell me what does it internal look have? It has parents and children.
>
>What do you think the relation between the children? 
>
>one key two groups. Two keys three groups.

> root. one key. and how many children does it have?  one key two children.

> So does it give you a sense what the internal node and key value are use. Now a binary tree only have one number in the node and it divides things into left and right. $B^+$-tree allows you to have multiple key values. And as you say, we cut the list of things into multiple consecutively and pointers will tell you where you go to. So in this sense, there are some similarities with the binary tree. But we take advantage of not just having one item in the left index, not just have one key value.

> Notice that $B^+$ tree is a ordered tree. It is ordered based on attribute you use to index. So in this case, before and after had nothing to do with the location of this table, having to do with what the alphabetical order offers. But it's not order by what's on the table. It's it's order by the value of the key.
>
> Now, I'm not telling you how we come up with this tree. I just want you to make sure. I just want to make sure if you see a $B^+$-tree, you know what's going on. How do we come up with this tree? We'll talk about it as we go along. Notice that the tree is balance. And when I say balance, I do not mean both subtree have the same number of elements.
>
> ![IMG_0463](Indexing.assets/IMG_0463.jpg)



> Why do you think we want everybody not to be at the same level? What's so good about balance tree?
>
> e.g. if there are 4 people in the room, tell you the average people is 25. It's can be 92, 2, 2, 2
>
> Stable
>
> If I guarantee the tree to balance the tree, the height of a tree will have to be logarithmic. you're guaranteed to have logarithmic height. If the tree is not balance what the worst that linear height. So a one of the main basically all the everything you see involving the $B^+$-tree has one overriding goal making sure the treat balance period.



* Tree-based structure
* Tree is made up of nodes
  * Typically each node corresponds to a page on secondary storage

* Data are stored at leaves only
  * Different from B-tree
  * If primary index, then tuples themselves are stored
  * If secondary index, then store index records (key, pointer)

> people can use both as a primary index or as a secondary index. If we use $B^+$-tree as a primary index, we might as well actually store the tuples in the leaf for the $B^+$-tree. Each node can store a few tuples. If it is a secondary index, then you just store the index record for each tuple, like for example, key and pointer. So at the least level. Each of them is actually the Brant and the pointer to the location where Grant actually stole
>
> ![Untitled Notebook-1](Indexing.assets/Untitled%20Notebook-1.jpg)
>
> If you use a primary index, you don't have to worry about whether you should use the index. You should pretty much always use as long as the query involved at. If you a secondary index that go back to the fundamental chicken egg problem. So just because you need to store a lot more things that are probably index doesn't mean you should not use the primary index.

> ![Untitled Notebook-2](Indexing.assets/Untitled%20Notebook-2.jpg)



* Each node can store multiple items
  * Assume a page has 1000 bytes
  
  * Now if a tuple is 100 bytes, then a leaf can store 10 tuples
  
    > $\frac{1000}{100} = 10 \ tuples$
  
  * Now if the $B^+$-tree is used as secondary index, each node will store `key + pointer`, typically around 20-25 bytes total. So each leaf can store 40-50 records
  
    > $\frac{1000}{20}=50 \ records$
    >
    > $\frac{1000}{25} = 40 \ records$



* Internal node:

  ![image-20220924153351270](Indexing.assets/image-20220924153351270.png)

  * $K_i$ are the search-key values 
  * $P_i$ are pointers to children (for non-leaf nodes) or pointers to records or buckets of records (for leaf nodes).

* The search-keys in a node are ordered 

    $K_1 < K_2 < K_3 < . . . < K_{n–1}$

> Pointers are pointing to the children, to the child nodes
>
> If we use $B^+$-tree as a primary index, then the leaf node will actually store the whole tuple, but the internal node will be unchanged. The internal note will only store that key that you used to index it. So if you change from a binary tree as a $B^+$- tree for primary index versus a $B^+$-tree for a secondary index. The ==only difference== is what is being stored in the leaf, not the internal node will not follow the tuples. Once again, that's the key difference between B-tree and $B^+$-tree.





* Internal node:

  ![Screen Shot 2022-09-24 at 15.36.26](Indexing.assets/Screen%20Shot%202022-09-24%20at%2015.36.26.png)

Interpretation: 

* All data that is stored under the subtree pointed by $P_j$ has $K_{j-1}$ ≤ key value < $K_j$
  * All data under $P_1$ is < $K_1$
  * All data under $P_n$ is >= $K_{n-1}$
  * equal sign can shift from left to right
  * If duplicates are allowed (e.g. secondary index on non key attributes), it is possible for equal sign to be on both sides

> ![Untitled Notebook-3](Indexing.assets/Untitled%20Notebook-3.jpg)



#### B+-tree: Query

* Query is just like any tree search
* To find the tuple/index record with key value x
* Then starting at the root node, 
  * For each internal node, find j such that $K_{j-1} \leqslant x < K_j$
  * Then follow the pointer of $P_{j-1}$ to the next internal node
  * Repeat the process until a leaf node is reached
  * Search the leaf node to see if the tuple/index record is present
  * Boundary cases, when $x < K_1$ and $x \geqslant K_{n-1}$ (go to $P_1$ and $P_n$ respectively)

> ```c
> function find(v)
>   /* Assumes no duplicate keys, and returns pointer to the record with 
>   * search key value v if such a record exists, and null otherwise */
>   Set C = root node
>   while(C is not a leaf node) begin
>     Let i = smallest number such that v<=C.Ki
>     if there is no such number i then begin
>       Let Pm = last non-null pointer in the node
>       Set C = C.Pm
>     end
>     else if (v = C.Ki) then Set C = C.P_{i+1}
> 		else Set = C.Pi /* v < C.Ki */
>   end
>   /* C is leaf node */
>   if for some i, Ki = v
>     then return Pi
>     else return null; /* No record with key value v exists*/
> ```
>
> ![Untitled Notebook-4](Indexing.assets/Untitled%20Notebook-4.jpg)





* Similar case for a range query
* Find all tuples with key value between a and b
* For each internal node, check if the range ($K_{j-1}$, $K_j$) intersect with the range (a, b); if so, continue on pointer $P_{j-1}$.
  * Once again, consider boundary cases ($K_1 < a$, $b < K_{n-1}$)

* Also, often the leaf nodes are either stored as a sequential file, or have links connected them in order
  * Then only need so search for a, and then follow the order / links

* Query time (not counting time to retrieve the data) is proportional to the height of the tree



#### $B^+$-tree: Structure

* Recall all data are store in the leaves
  * Internal nodes’ key value are used to guide the search

* Goal of updates, to maintain two conditions

  * The tree remain balanced (i.e. all the leaf nodes are at the same level)

    > Make sure that stable of log height tree

  * Ever<u>y node (except the root) has to be at least half full</u>

    > If your node can hold nine items, your tree has to be at least four items.
    >
    > So if internal node can have at most ten children, then basically each internal look have to hold at least five children, except the root. The root can hold as little as two children.

* The two conditions combined <u>ensure the height of the tree to be logarithmic to the number of items</u>

  > That means search can be done very efficiently. So that requires that every node has to be at least half full.
  >
  > 
  >
  > So the price you are paying for all kind of the main price to pay for all these is that you made waste of space. You need to store $B^+$-tree



#### $B^+$-tree: Insertion

* Suppose one want to insert a tuple (or record, same below) of key value x
* First, run a query to find the leaf node where x would have been located
* If that leaf node is not full, then insert the tuple into the leaf node, and insertion is done
* What if the node is already full?

![Untitled Notebook-5](Indexing.assets/Untitled%20Notebook-5.jpg)

![Untitled Notebook-6](Indexing.assets/Untitled%20Notebook-6.jpg)

![Untitled Notebook-7](Indexing.assets/Untitled%20Notebook-7.jpg)

* If the node is full
  * Need more space to store the data
  * Create a new node
  * Distribute the data evenly across both nodes, in order
  * Now the new node also need to be referenced
  * So the original node’s parent need to create a new entry 



**Example:**

* assume leaf node can hold 5 records, internal nodes can hold 5 pointers & 4 numbers

* Leaf node contain tuple/index records that are not shown

![image-20220928143016120](Indexing.assets/image-20220928143016120.png)



* What if the parent is full?
  * Need more space for the parent
  * Create a new internal node
  * Distribute the (key, pointers) evenly
  * Need to create a new entry for the parent’s parent to insert

* <u>Essentially the same code for the leaf split</u>

* The split will continue propagate upwards if necessary

* When the propagation reaches the root, the root is split, and a new root is build on top to be the parent of the two nodes
  * This is where the tree grows in height
  * This is also the reason why the root may be less than half full



**Example:**

![image-20220928144002341](Indexing.assets/image-20220928144002341.png)







#### $B^+$-tree: Deletion

* Similar approach
* First find the leaf node storing the item to be deleted
* Then remove it
* If the node still is at least half-full, then done

* Otherwise:
  * Examine the node’s neighbor
  * If anyone of its neighbor has is more than half-full, then move some data around to fill all the nodes to half-full
    * Will need to <u>update the parent’s key value to maintain the correctness</u>
  * Otherwise (all the neighbors are exactly half-full), merge the node with one of its neighbor 
    * Remove the corresponding key/pointer from the parent
    * <u>If at the top level, the root will only have one child – remove the root</u>



Example: 

![image-20220928144330864](Indexing.assets/image-20220928144330864.png)



![image-20220928144422534](Indexing.assets/image-20220928144422534.png)



* Node with Gold and Katz became underfull, and was merged with its sibling 

* Parent node becomes underfull, and is merged with its sibling
  * Value separating two nodes (at the parent) is pulled down when merging
* Root node then has only one child, and is deleted



> The example from textbook
>
> 1. delete "Srinivasan".

```mermaid
graph TD;
A(Monzart ,__ ,__)
A --> B(Califierir, Einstein, Gold)
A --> C(Srinivasan, __, __)
B --> D(Adams, Brandt, __)
B --> E(Califleri, Crick, __)
B --> F(Einstein, El Said, __)
B --> I(Gold, Katz, Kim)
C --> G(Mozart, Sigh, __)
C --> H(Srinivasan, Wu, __)







```

> ```mermaid
> graph TD;
> A(Monzart ,__ ,__)
> A --> B(Califierir, Einstein, Gold)
> A --> C(__, __, __)
> B --> D(Adams, Brandt, __)
> B --> E(Califleri, Crick, __)
> B --> F(Einstein, El Said, __)
> B --> I(Gold, Katz, Kim)
> C --> G(Mozart, Sigh, __)
> C --> H(__, Wu, __)
> 
> ```
>
> ```mermaid
> graph TD;
> A(Monzart ,__ ,__)
> A --> B(Califierir, Einstein, Gold)
> A --> C(Wu, __, __)
> B --> D(Adams, Brandt, __)
> B --> E(Califleri, Crick, __)
> B --> F(Einstein, El Said, __)
> B --> I(Gold, Katz, Kim)
> C --> G(Mozart, Sigh, __)
> C --> H(Wu, __, __)
> ```
>
> Since $n = 4 \ and \ 1 < \left \lceil \frac{n-1}{2} \right \rceil$ , we must either merge the node with a sibling node or redistribute the entries between the nodes, to ensure that each node is at least half-full. Therefore, Wu can be merged with its left sibling node.
>
> ```mermaid
> graph TD;
> A(Monzart ,__ ,__)
> A --> B(Califierir, Einstein, Gold)
> A --> C(Mozart, __, __)
> B --> D(Adams, Brandt, __)
> B --> E(Califleri, Crick, __)
> B --> F(Einstein, El Said, __)
> B --> I(Gold, Katz, Kim)
> C --> G(Mozart, Sigh, Wu)
> 
> ```
>
> Since $1 < \left \lceil \frac{n}{2} \right \rceil \ for \ n =4$ , the parent is not under full. In this case, we look at a sibling node; the nonleaf node containing the search keys "Califieri", "Einstein", and "Gold". We try coalesce the node with its sibling. But in this case, coalescing is not possible, since the node and its sibling together have five pointers, against a maximum of four. The solution in this case is to redistribute the pointers between the node and its sibling, such that each has at least $\left \lceil \frac{n}{2} \right \rceil =2$ child pointers. To do so, we move the right most pointer from the left sibling (the oen pointing to the leaf node containing "Gold") to the underfull right sibling. 
>
> ```mermaid
> graph TD;
> A(Gold ,__ ,__)
> A --> B(Califierir, Einstein, __)
> A --> C(Mozart, __, __)
> B --> D(Adams, Brandt, __)
> B --> E(Califleri, Crick, __)
> B --> F(Einstein, El Said, __)
> C --> H(Gold, Katz, Kim)
> C --> G(Mozart, Sigh, Wu)
> ```



> Now we delete the search-key values "Singh" and "Wu".
>
> The deletion of "Singh" does not make the leaf node underfull.
>
> ```mermaid
> graph TD;
> A(Gold ,__ ,__)
> A --> B(Califierir, Einstein, __)
> A --> C(Mozart, __, __)
> B --> D(Adams, Brandt, __)
> B --> E(Califleri, Crick, __)
> B --> F(Einstein, El Said, __)
> C --> H(Gold, Katz, Kim)
> C --> G(Mozart, Wu, __)
> 
> ```
>
> But the delection of "Wu" it will make the node underfull.
>
> ```mermaid
> graph TD;
> A(Gold ,__ ,__)
> A --> B(Califierir, Einstein, __)
> A --> C(Mozart, __, __)
> B --> D(Adams, Brandt, __)
> B --> E(Califleri, Crick, __)
> B --> F(Einstein, El Said, __)
> C --> H(Gold, Katz, Kim)
> C --> G(Mozart, __ ,__ )
> ```
>
> It is not possible to merge the underfull node with its sibling, so a redistributiong of values is carried out. 
>
> ```mermaid
> graph TD;
> A(Gold ,__ ,__)
> A --> B(Califierir, Einstein, __)
> A --> C(Kim, __, __)
> B --> D(Adams, Brandt, __)
> B --> E(Califleri, Crick, __)
> B --> F(Einstein, El Said, __)
> C --> H(Gold, Katz, __)
> C --> G(Kim, Mozart, __ )
> ```
>
> 

> Now we delete "Gold" from the above the tree.
>
> ```mermaid
> graph TD;
> B(Califierir, Einstein, __)
> C(Kim, __, __)
> B --> D(Adams, Brandt, __)
> B --> E(Califleri, Crick, __)
> B --> F(Einstein, El Said, __)
> C --> H(__, Katz, __)
> C --> G(Kim, Mozart, __ )
> ```
>
> This result is an underfull, which can now be merged with its sibling. 
>
> ```mermaid
> graph TD;
> B(Califierir, Einstein, __)
> B --> D(Adams, Brandt, __)
> B --> E(Califleri, Crick, __)
> B --> F(Einstein, El Said, __)
> 
> G(Katz, Kim, Mozart)
> ```
>
> The resultant delection of an entry from the parent node (the nonleaf node containing "Kim") makes the parent underfull (it is left with just one pointer). This time around, the parent node can be merged with its sibling. This merge results in the search-key value "Gold" moving down form the parent into the merged node.
>
> ```mermaid
> graph TD;
> B(Califierir, Einstein, Gold)
> B --> D(Adams, Brandt, __)
> B --> E(Califleri, Crick, __)
> B --> F(Einstein, El Said, __)
> B-->H(Katz, Kim, Mozart)
> ```
>
> 



#### $B^+$-tree: Update cost

* Cost (in terms of number of I/O operations) of insertion and deletion of a single entry proportional to height of the tree
  * With K entries and maximum fanout of n, worst case complexity of insert/delete of an entry is O($log_{\left\lceil\frac{n}{2}\right\rceil}(K)$)

* In practice, number of I/O operations is less:
  * <u>Internal nodes tend to be in buffer</u>
  * Splits/merges are rare, most insert/delete operations only affect a leaf node

* Average node occupancy depends on insertion order
  * $\frac{2}{3}$rds with random, $\frac{1}{2}$ with insertion in sorted order

> remember, if you have to insert a node, you have to travel through all node first. So all the internal look is probably already in the buffer anyway. You don't have to read it twice. Even you have to do a spread.



#### 14.4.1 & 2 $B^+$-tree as the clustering index / file organization

* $B^+$-Tree File Organization:
  * Leaf nodes in a $B^+$-tree file organization store records, instead of pointers
  * Helps keep data records clustered even when there are insertions/deletions/updates

* Leaf nodes are still required to be half full
  * Since records are larger than pointers, the maximum number of records that can be stored in a leaf node is less than the number of pointers in a nonleaf node.

* Insertion and deletion are handled in the same way as insertion and deletion of entries in a B+-tree index.

* To improve space utilization, involve more sibling nodes in redistribution during splits and merges
  * Involving 2 siblings in redistribution (to avoid split / merge where possible) results in each node at least half full

> The example I show is the $B^+$- tree as a secondary index. There's nothing stopping you from hey, in cell phone, in my table, in the file. I'll just pull my table in the $B^+$- tree.  I basically took the leaving of the tuple, the leaf in the tree now if filled whole tuples. There's nothing stopping us from doing it. There's some limitation to it because people seem to have some expectation of size and you got to point the watch out. But simple things can get a bit dicey. Okay. So so it's not always ideal to do that, but, you know, not to have a fixed size. This actually is and, you know, low key, have some order to it. It is actually quite attractive. Doing this as a B plus three as A as your cluster index or excel basically as a file. So instead of storing a table in a file, store my table in the $B^+$- tree.



#### 14.4.3 Indexing Strings

* Variable length strings as keys
  * Variable fanout
  * Use space utilization as criterion for splitting, not number of pointers

* **Prefix compression**
  * Key values at internal nodes can be prefixes of full key
    * Keep enough characters to distinguish entries in the subtrees separated by the key value
      * E.g., “Silas” and “Silberschatz” can be separated by “Silb”
  * Keys in leaf node can be compressed by sharing common prefixes

> So as I say, typically one trouble with B plus three is that we're dealing with strength because strains can be different size. So now one way of getting around this problem is to not use the number of child, but use how much space is being used as a criterion. And that itself can still be problematic. There are a couple of other tricks. Maybe instead of storing the full name in the notice deck for the leave that we have to store everything. That's no tricks. We can go around for the internal notes. We can play some tricks because, oh, I know it has to be lateral. You call them. I don't have to store the whole string as a key. Maybe I can spot prefix. Maybe I can install this one as a compact SUV or as Aldi. So that can be a alternative for gathering strings.



#### 14.4.4 $B^+$-tree : Bulk loading

* Inserting entries one-at-a-time into a $B^+$-tree requires $\geqslant$ 1 IO per entry 

  * assuming leaf level does not fit in memory
  * can be very <u>inefficient</u> for loading a large number of entries at a time (**bulk loading**)

  > one-at-a-time, so if you insert entries one at a time, this can be quite inefficient. 
  >
  > When i say bulk loading, that I already have a large set of tuples in my table. I suddenly want to fill a $B^+$- tree on it
  >
  > So it's not like I'm starting from scratch, starting with zero tuples. So maybe I have only 10,000 tuples in my table. And suddenly I realize that I really do need a $B^+$ - tree on each. How can I do it efficiently?  So there are a couple of alternative from inserting a tuple one by one.

* Efficient alternative 1:

  * sort entries first (using efficient external-memory sort algorithms discussed later in Section 12.4)
  * insert in sorted order
    * insertion will go to existing page (or cause a split)
    * much improved IO performance, but most leaf nodes half full

  > Now why do we think about this way? Because if you think about it right, the leaves node on $B^+$-tree are actually ordered. So if you are building a $B^+$-tree. You are purposefully inserting two tuples to a index from left to right. Then you won't have the problem of suddenly have a leaf in the middle of the trees, the thing about worst become much less, because you always extending things to the right. And furthermore, because you are inserting things on left to right. The first few things insert it's going to be in the same leaf.  Because at least most likely a bunch of consecutive not things that you think he's going to be on the same leaf. That means if you are using some buffers, your looks will remain the buffers.

* Efficient alternative 2: **Bottom-up $B^+$-tree construction**
  * As before sort entries
  * And then create tree layer-by-layer, starting with leaf level
    * details as an exercise
  * Implemented as part of bulk-load utility by most database systems

> So remember, in this case, you already know how many tuples are there. So you can actually calculate how many leafs do you need. Because you know how many data you can fit in a leaf node. You know how many entries are there? Do a simple division, you figure out how many leaves are there. Some time most system when you do this will leave the leaf node like 75% full. Just in case, when you insert new things, you don't want to do a lot of split right off the that. But still, you can simply calculate how many nodes are dead?  Let's say it turns out that our leave. 12 leave nodes. ??? Then I will first create the 12 leaves notes. Group the data. Now still do have sorted things that you cannot get away. But now   I can ask the same question. I have 12 node. I know that I have 12 nodes. 
>
> ![Screen Shot 2022-09-29 at 16.10.59](Indexing.assets/Screen%20Shot%202022-09-29%20at%2016.10.59.png)
>
> How many internal nodes at my upper level do I need? Well, again, you know, internal looks can hold. Let's see. About several can have between two and three child. Then maybe I need four parents. Or I may want to relax. I may want to have six parent if two child. So I don't have to split immediately. Then you build all these things and have them point to the right children.
>
> ![Screen Shot 2022-09-29 at 16.11.32](Indexing.assets/Screen%20Shot%202022-09-29%20at%2016.11.32.png)
>
> So until you can and then you can recursively repeat the process.
>
> I have six internal node so what the next up level high how many nodes do I need? Maybe two, maybe three. So once again, you can continue to build go on top one level and build things. It will require a separate set of code. You can't quite reuse your standard circle street code, you have to write your extra code for that. But it's just really writing the code once and you can use this subsequent. So that's why this actually become a quite attractive way of building it up willing $B^+$-tree from scratch, assuming you already have all the data available.



## $B^+$-tree: Other issues

* SSD / Flash memory

  * <u>Random I/O cost much lower on flash</u>
  * Writes are not in-place, and (eventually) require a more <u>expensive erase</u>
  * <u>Optimum page size therefore much smaller</u>
  * Bulk-loading still <u>useful since it minimizes page erases</u>
  * Need specialized write-optimized tree structures have been adapted to minimize page writes for flash-optimized search trees

  > Now this is where SSD come into play and in a somewhat negative way. If you keep updating $B^+$-tree, what happened? If you insert to a tuple, you have to update a new leaf regularly, put a new item to leaf. If you swift the node, that means you have to create a new node, but the existing will also likely be updated, then more things are being updated and change. And what's the problem if you use SSD? You cannot update until you erase everything. That means if your tree is really dynamic, you reall y to think about a lot of extra space for moving things around and pray that you can garbage collection very effectively. That make a dynamic index structure. We won't go into detail in this class. Maybe in two or three years time we will start. Need to talk about these because flash memory will become much more popular. And this is a real problem that we need to deal with. Every index structure, especially you expect your database to be somewhat dynamic. That means there's quite a lot of update. If you put on a solid state drive, it is always an issue that we need to deal with. 

* Main memory
  * Random access in memory 
    * Much cheaper than on disk/flash
    * But still expensive compared to cache read
    * Data structures that make best use of cache preferable
    * Binary search for a key value within a large $B^+$-tree node results in many cache misses
  * $B^+$- trees with small nodes that fit in cache line are preferable to reduce cache misses
  * Key idea: use large node size to optimize disk access, but structure data within a node using a tree with small node size, instead of using an array

> Many systems have been using what we call `log-based file structure`. Bascially what happened is that I'll give you a brief overview. I won't go into detail. Let's see. I need to update a page. What I do is I actually don't update the page. I instead of requesting  that, hey, this page needs to be updated. So what happened? So? So then I minimize the update, right? 
>
> I'm just waiting for that. So you think there's a lot entry?  I keep having a new pace, ending all these things. Only when there's too many things out there. Then I modify the file structure once. Now, of course, the problem is what your file structure takes. You may you may still want to query the index before all the all the update entries have been actually apply. So there are special commands and special data structure out there. So I tried to make the life easier. There we go. But it is a very different way of thinking about file system because of the limitation of necessity. And in a in a very dynamic file structure like index, things can be useful over there. Once again, we won't go through in this class. We will go over an operating system because typically offerings some classes have too many things to cover that we have no time to talk about our systems. But this is certainly something we will probably need to talk about it sometime down the road, maybe an advanced OS or an advanced database class. but I do at least want you to think about, Hey, this is something we need to think about. If I have to go out to work and have to work with something like this, I better look at the current literature. What is being done actually being done with it? So I don't want you to go I don't want to go to solution. I want you to at least remember that this is something that we need to deal with. And if I have to do it, I better look up the current literature to see what is being done currently.

> I want you to read it yourself to get a sense of, Hey, let's get this is something I need to worry about if I work in tech view. So so keep that in mind. These are interesting research problem. If you are interested in doing the database research kind of somewhere between database and system research. I don't think we have the final answer yet. And anyway, this is actually a big challenge for database companies. Everybody want to outdone their opposition by five microseconds.



## Hashing based techniques

> What is hashing? So you have items you want to store, and then whenever you want to insert something, you apply a hash function to that item. The hash function will tell you which location you should store it, and then you go ahead and start. Ideally, your hash function should avoid collision. What is a collision? Two different things hash the same value. Now on the other hand, somtimes these are just simply unavoidable.
>
> If you have ten buckest and you are storing eight, then good luck or your target social security number then really good luck. So and if you are in database , if you are in data structure class, there is a lot of different techniques to handle collisions. In fact, if you have nothing to do.
>
> "The art of computer programming", the books are written in the seventies. When you have 64 bytes of memory, you are very cool. Because you don't have any memory, then managing a hash table become very paramount, because I can't create two million buckets. So how do you handle collision? I think the volume two actually talked about hashing. I strongly encourage you to if you have nothing to do, uh, read those kept on hashing. The collison manament techniques are very very smart. And and sometimes I'm sure there is a philosophical lesson out there. If you have nothing in life or where is the pain that you know how to make the best out it. If you are militate just say let's spend money to solve the problem. But if you do not have money to solve the problem that you need to solve the problem in some very very clever way.

* Recall basis of hashing

* You want to store items. Each item has a key value x

* Create a hash function **h(x)** to map x to an integer between [0..n-1]

  > For the sake of this class we are assuming the thing to be has integers, although it works for every other thing. But typically that description make life a bit easier.

* Have a hash table of n slots.

* Item x will be stored in slot h(x)

  * Multiple techniques are used to handle collisions (multiple 

> In database. Once again, things are little bit different here. Assuming we are storing the hash table into a secondary story right into a disk, once again was the basic unit of access on a this far? It's a page. And a page typically of how many bytes? 256 bytes. So if you have a 256 bytes, let's assume we are storing integers: $\frac{256}{8} = 32$
>
> If we think of a page as a single bucket. By default, a bucket can store more than one thing. You still have collision, but collision is not scary as before. Because by default you're going to even if there's eight things that have the same cash value. You're going to store them in the page. It will make no difference because you are reading a page at a time anyway. You don't want everything hatch the same value. But it's not like the end of the world, and they decide to take a very easy approach in coalition management.



Modification for database system

* Each entry of a hash table is now a “bucket”
  * Typically size of a page
  * Thus more than one element 
  * All items with the same hash values (even different keys) stored in the same bucket

* <u>Overflow still possible</u>

  * Instead of using complicated schemes, simple <u>add overflow buckets</u> 

    * Essentially building a link list of buckets for each entry

    > We assume each entry is detected within a bucket that a bucket correspond to a single page on the dish. So that means each entry can now store more than one thing. And if you are so unlucky that you have so many things that have to, the same bucket database may say, you know what? Let's start worry about all those fancy coalition techniques. Let's just do over four buckets. So basically a linked list of buckets. ![Untitled Notebook-9](Indexing.assets/Untitled%20Notebook-9.jpg)

    * Notice that in secondary storage, this can be a file itself
    * This is known as chaining

  * Other techniques are not used 

> And you think that all of the things that you talk about in building high functioning in data structure apply to you. so we'll even sweep that under the rug.

> Q:  So in Java, there is a structure called hash, is there anything to do with? 
>
> A: No, not here. It turns out a very important problem in the database is how many buckets do you need? If you have two filled buckets what happened?  Coalition. That's fine. We said we go to build list, but this linked list can be very large.
>
> Let's say you have 4 buckets, even your data is nicely distributed, but it will be one quarter of a whole table. You don't save a lot of time. If you do hacking, you expect it only take one or two operations to get your data. If you have too many buckets, let's say, what if I have 100 tuples in my hash table and I define 2 million buckets. A lot of overhead, a lot of waste space.
>
> So how do we find the right number of buckets? More interestingly, when you design database, many times you have no clue how many tuples are there.  And even if you have some idea, you still do not know how do the tuples behave respect to the hash function. Is the hash function good on this data set? Or the hash function really stick. How do we account for that? Now, typically your hash function is predefined without knowing data. So that's another limitation.
>
> Remember when you hear word hash table, your excectation is what I calculate hash function, hash function should get me to the bucket, I should immediately be able to retrieve the data. 
>
> At least a user expectation is that I have a bucket I should get the thing. Not reading one quarter of a whole table. Then bucket size become an issue. On the other hand, you don't want to have to make too many buckets in the beginning. Beacuse you have so many overhead. So how do we balance these things out without knowing anything? Become an interesting challenge in hashing. In fact, from database point this is probably the biggest challenge in hashing and that will keep us busy for the rest of lecture.



Example

* Hash file organization of *instructor* file, using *dept_name* as key (See figure in next slide.)
  * There are 10 buckets,
  * The binary representation of the $I^{th}$ character is assumed to be the integer $i$.
  * The hash function returns the sum of the binary representations of the characters modulo 10
    * E.g. h(Music) = 1    h(History) = 2  
           h(Physics) = 3  h(Elec. Eng.) = 3

![image-20220928145455997](Indexing.assets/image-20220928145455997.png)





* The above technique is also known as **static hashing**

  * Static as in the <u>number of buckets is fixed</u>

    >Notice that the size of the bucket can grow that overflow. 

  * The size of each bucket can grow (overflow)

* Problem with database with a lot of insert/delete
  * If initial number of buckets is too small, and file grows, performance will degrade due to too much overflows.
  * If space is allocated for anticipated growth, a significant amount of space will be wasted initially (and buckets will be under-full).
  * If database shrinks, again space will be wasted.

* One solution: periodic re-organization of the file with a new hash function

  * Expensive, disrupts normal operations

    > But that will take a long time.

* Better solution: allow the number of buckets to be modified dynamically: ==**dynamic hashing**==

  > Basically, the key thing is that you allow the number of buckets to be changed along the way. So now you have two buckets and them in the database. Go out at a bucket. If database grow even more out, another set of buckets and then the database straight out combined buckets to get.
  >
  > in order for you to do Dynamic Pershing, you have to have a hash function that allows you to do that. So let's say you have a hash function, hash on something. We assume this to actually generate an integer actually a non negative integer



> The hash function is going to dependent on the number of bucket and the number of bucket will depend. The number of buckets will tell you how many bits you need to represent. 
>
> And the point for the rest of this class is that the number of buckets will change based on how many tuples are there
>
> You must have to address. And the address is represented by digit. You cannot represent address by real name. So the output will always be a binary. And we write it in binary because it make a lot of our algorithm description much easier. So the idea is that you will have written a function so that when you see a it will be mapped to some integer. How do you do that? That's not my business. ASCII values, ASCII value, whatever. You may have a fancy geometric function or whatever.  the point is, is that it outputs a binary. It has always had the output by number because you always have to output a location and location can only be an integer.
>
> 

![Indexing-11](Indexing.assets/Indexing-11.jpg)

![Indexing-12](Indexing.assets/Indexing-12.jpg)



## Dynamic hashing

* Key idea: the number of buckets can increase and decrease with the amount of data

* Implication: the hash function has to be able to adapt to the number of buckets available

* General approach

  * Convert the key (via some function) to a number x

  * Bucket for the item = x MOD (current # of buckets)

    > **11** mod **4** = **3**, because 11 divides by 4 (twice), with **3** remaining.
    >
    > **25** mod **5** = **0**, because 25 divides by 5 (five times), with **0** remaining.
    >
    > **3** mod **2** = **1**, because 3 divides by 2 (once), with **1** remaining.
    >
    > **5** mod **2** = **1**, because *all odd numbers* yield a remainder of **1** when divided by **2**.

    > To be more precise, your hash function has two steps process. 1. The first step is take whatever you have and convert it to an integer to a location 2. and then you do the take the right most bit thing that we do to and and if you think about it, if you remember your binary metric, take the rightmost bit. It's nothing more than doing a modulo

* Another important issue
  * Need to keep track of location of each bucket
  * Need some form of table to keep track of it (or some other convention, see later)
    * Usually a table, with each entry pointing to the first page of a bucket



* Start with 1 bucket (so no hashing)

* At any given time

  * When an insertion make a bucket overflow

  * Double the number of buckets

    * The table storing pointers need to be doubled
    * Each bucket will start with a single page

    > when you introduce an extra bit, you always double the number of buckets.

  * Rehash the whole file (Some data will need to go to a new bucket)

* This implies at any stage, the hash function becomes looking at the rightmost bits of the number (written in binary) converted from the key

> ![Indexing-13](Indexing.assets/Indexing-13.jpg)
>
> ![Indexing-14](Indexing.assets/Indexing-14.jpg)

>This method, Every time you have the double things, you should have a red alert. Doubing things means growing exponentially. So that's the drawback. You keep inserting things and your function is not very nice in the sense that a skill and overflow become often. Then your number buckets grow exponentially. And that's not cool.



Example: 

* Items to be stored are numbers 

* Assume each bucket store 2 numbers

![Screen Shot 2022-09-28 at 14.58.39](Indexing.assets/Screen%20Shot%202022-09-28%20at%2014.58.39.png)

> Notice that we will have kind of a head table to tell the system where each bucket is.
>
> So if you absolutely do not want to have overflow bucket, you will have to immediately create or sell buckets. Now that means what? That means you have a lot of empty buckets.

![Screen Shot 2022-09-28 at 14.59.32](Indexing.assets/Screen%20Shot%202022-09-28%20at%2014.59.32.png)

> Now, so obviously this grow exponentially. And when you grow fast, you will create a lot of empty buckets.



* Limitation
  * Double of number of buckets – exponential growth
  * A lot of empty buckets potentially

* Variations
  * One does not have to immediately rehash when a bucket is overflown
    * Allow <u>some overflow bucket, can slow down the growth</u>
    * Also avoid empty buckets
    * Price : slow down access





## Extensible hashing

> You can actually do things about empty buckets. By a method, what we call extensible hashing.

* One problem with dynamic hashing
  * When rehashing, the number of buckets are doubled 
  * Some buckets may be unnecessary

* One way to get around it, extensible idea

* Key idea: 
  * <u>==When you rehash, only create new buckets when necessary==</u>



Example: 

* Items to be stored are numbers 

* Assume each bucket store 2 numbers

![Screen Shot 2022-09-28 at 15.01.24](Indexing.assets/Screen%20Shot%202022-09-28%20at%2015.01.24.png)

![Screen Shot 2022-09-28 at 15.01.50](Indexing.assets/Screen%20Shot%202022-09-28%20at%2015.01.50.png)



![Indexing-15](Indexing.assets/Indexing-15.jpg)

![Indexing-16](Indexing.assets/Indexing-16.jpg)



## Linear Hashing

> So there is a super smart algorithm that even stopped this called linear hashing.

* Why?
  * Most extensible hashing techniques require <u>some sort of exponential growth</u>
    * Introducing one more bit will double the size of the hash table/index
    * Massive rehashing slow things down

> So linear hashing is a third technique that we use.



* Key ideas

  * Hash table entries <u>grow in a linear fashion</u>

  * ==Have a pre-defined order of splitting the bucket, **regardless of which bucket is overflowing**==

    * A overflow bucket must wait for its turn to be split (rehashed)
    * Need overflow buckets (linked list)

    > And the key thing about linear hashing is this statement, which is quite counter intuitive to your traditional hashing techniques. 
    >
    > In traditional hashing. What happened? You split a bucket when the bucket is overflow. Because the bucket overflow, then you had the split, then hopefully distribute the overflow stuff in the two separate buckets.
    >
    >  in linear hashing. Basically, they say, who cares? I can care less which bucket overflow. Basically what I'm saying is that I have a pre-defined order, all of them on which thing to split regardless of which bucket overflow.
    >
    > So it is the term for bucket 2 to split. I don't care which bucket overflow I'm going to spit bucket 2. Even bucket 2 have nothing, I still split bucket 2.
    >
    > It turns out by doing this, I make a lot of things legal. I get rid of every exponential things that we talked about earlier, and that's worth looking at. 

  * This ensure the growth is linear

  * Price to pay: overflow bucket slow down access

    * Can be serious is hash function is lousy / data distribution is lousy



* Assume Hash function = rightmost k bit of the number (k changes with the algorithm)

* For linear hashing, maintain two variables
  * Level: the current level of hashing,
    * Starts at 0
    * At the start of level k, there will be $2^k$ buckets
      * E.g. k = 2, then buckets are 00, 01, 10, 11
    * A level finishes when all the buckets at the start of the level is split





* Assume we are hashing function

* Hash function = rightmost k bit of the number (k changes with the algorithm)

* For linear hashing, maintain two variables

  * Ptr: Points to the next bucket to be split

    * Whenever ANY bucket overflows, it is the bucket that ptr points to that split

    * When a bucket is split, it split into 2 buckets by adding 0 and 1 as the new leftmost bit

      * E.g. bucket 01 is split into bucket 001 and 101

      * Only the bucket that is split need to be rehashed

    * Reset to 0 at the start of each level

    * Once the bucket is split, increment ptr by 1 (until end of level, by then it reset back to 0)



* Ptr also help us to determine which bucket should one search
  * Consider we are at level k
    * All buckets that are not split are represented by k bits
    * All buckets that are split are represented by k+1 bits
  * When I search for a number
    * Look at the rightmost k bit of the hash value
    * If it is >= ptr, then go straight to this bucket
    * If it is < ptr, than look at one more bit at the left, and that will denote the bucket to search





* Splitting occurs when one inserted into a bucket that is full (or overfull). 

* Remember that the bucket that is overfull may not be the one that is split
  * In such case, we use overflow buckets (building a link list) to store the extra value

* When a bucket is split, it is split into two
  * Even if the split bucket is overfull, we do NOT continue the splitting 
  * Rehashing is done on the split bucket only (and only that is needed)

* More advanced versions of linear hashing will change when splitting occurs (e.g. do not wait till a bucket overflows). 





Example: 

* Items to be stored are numbers 

* Assume each bucket store 2 numbers

  

  ![Screen Shot 2022-09-28 at 15.08.59](Indexing.assets/Screen%20Shot%202022-09-28%20at%2015.08.59.png)

![Screen Shot 2022-09-28 at 15.09.25](Indexing.assets/Screen%20Shot%202022-09-28%20at%2015.09.25.png)

0000    0

0001	1

0010	2

0011	3

0100	4

0101	5

0110	6

==0111	7==

1000	8

1001	9

1010	10

==1011 	11==

1100	12

1101	13

1110	14

==1111	15==

