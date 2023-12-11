# File Structures

## File structures for relational databases

* Relational database
  * A set of tables
  * Each table has a set of tuples (records)

* Assumption:
  * Data are stored in files
  * Files are stored on disk
  * Data on files are divided into fixed size blocks (pages)
  * For now, assume each table corresponds to a file

> The rest of the class, unless otherwise stated. I'm going to assume we are dealing with magnetic hard drive. We are assuming data stored in a traditional magnetic hard drives.
>
> I'm going to use the term blocks and pages somewhat interchangeably, maybe even move sector because in at least the early days, a page is basically a sector. A page or a block is a basic unit wheat and right. So basically every time, if even about after a single to pull the system, we will read a page. In a paper, maybe like one kilobytes and so on, so forth.



* Each table has a set of tuples / records
* Each tuple is make up of a fix set of attributes
* Attributes have types, which require bytes to store
  * E.g. integer – 4 bytes, 

* Some types allow variable length
  * E.g. VARCHAR, 
  * But VARCHAR(50) can be viewed as fixed size of 50 

* Thus tuples can be of fixed or variable length





## Page structure: Fixed length records

* Assume each record requires n bytes
  * Store record *i* starting from byte $n\times(i– 1)$, where *n* is the size of each record.
  * Each record has a number associated with it

![image-20220918110737654](File%20Structures.assets/image-20220918110737654.png)

​                  							5 bytes				25bytes						15bytes						5bytes					= 50

What other bookkeeping info is needed? 

Problem of this approach?

>  So, for example, let's say in this case, we have a student ID, the name of the student in the major and a name of the professor in major department and a salary. And let's assume we limited the name of the by the name of department. You know, what department are there. So it's easy to restrict the length of that string. Right. Last name. Name. Maybe we will restrict it to 25 characters. So that is tuple is of a fixed size
>
> So typically each data in a database system, there's something called a data dictionary. That's still what we call metadata. So, for example, how many tuples do this table have? What is the name of the attributes? What is the type of each attribute? So on something. And typically we notice that because this is the fixed size, I don't even bother to store the number.
>
> The good one of the good thing about relational model is what metadata also store in tables. So it's a uniform data organization.
>
> Anything you can think of that you need to be careful about? updating a record, what can happen? So let's see. He moved from history to say geology. You just overwrite. Assume the location 100, the information 50byte. Overwrite, and then my structure will still be intact.
>
> 
>
>  you have to actually read the whole page up there and read the whole page back. 

![Screen Shot 2022-09-18 at 14.23.49](File%20Structures.assets/Screen%20Shot%202022-09-18%20at%2014.23.49.png)



## Fixed length records

* Problem 1 : Records may pass page boundaries
* E.g. A page has 100 bytes, each record has 12 bytes
  * Record number 9 will pass two pages
  * What’s the problem with that?

* Solution, limit size so no record cross boundaries:

  * E.g. in the previous case, each page can only store floor(100/12) = 8 records

  * Trade-off: internal fragmentation

    > trade-off    [ˈtreɪd ɔːf] n. 平衡，协调；妥协，让步
    >
    > fragmentation   [ˌfræɡmenˈteɪʃn] n. 破碎，分裂；分段储存
    >

> And remember, one of the biggest no matter what kind of disk drive you have, you are always going to read and write data on a per patient, per page unit, write every time you go. What if your page size is 240 bytes? 
>
> You can put the first record in, you can put the second record in, until your last 40bytes. Not quite a full record.
>
> I can choose to what I can either choose to forget it will leave 40 bytes of empty space and start putting the next record to the next piece or I can do that I can cut the record and then put the first 40 by the record in the first space and then the rest. 10 bytes into the second page. Which one do you think is better?
>
> It will read 240 every time whatever the whether it is full.  So efficiency is not help there, at least in this instance



> ```sql
> select *
> from Faculty
> where snn = "123456"
> ```
>
> So now I'm clear. I'm going to one record. But one couple can be stored in two pages now because you don't know. That means you can not guarantee that reading one tuple is required. Only one page. That can be an issue. Furthermore, if you want to write, you've got to update that tuple. Now updating this two tuple will require me to write two pages. Because the data is split. How many pages excess do I need to write it to? is now unclear. It's not dependent on where the tuples stayed. Later on you see that for a database to process, query some time, a lot of time they want to have some certainty that, 
>
> Most system will. Actually, if I have nothing to contribute, I'll just simply put full tuples in each picture and leave those 40 parts. And obviously, we have internal fragmentation if you take OS class before you know what fragmentation is.

![Screen Shot 2022-09-18 at 15.37.55](File%20Structures.assets/Screen%20Shot%202022-09-18%20at%2015.37.55.png)





* Insert a record
  * Just add a record at the end of the file

* Delete a record

  * 3 options

    * Shift all records up a slot
    * Shift the last record to fill in a page
    * Other solutions?

  * For the first 2 cases, do not shift record across pages (why?)

    > We seldom shift record over pages unless it's absolutely necessary. Why?
    >
    > The idea, it's probably not very clear for now, There are certain things I need to mention to make the answer make sense.
    >
    > It's acutally more have to do if the notion of an index. We'll get to that in a lot more detail. But point to to give a simple answer is that you have a file of tuples. There might be a lot of pointers pointing to you. There may be things that point to your page. So let's say of a index that index the name so they may have a dot Collins record is pointing to this page unless it is the last last couple in the file. If you say somebody records, delete it, you move up to clean up. Then what? Debt pointer to become invalid unless you also changing.
    >
    > Find the pointer is also cost time

    

![image-20220918110957899](File%20Structures.assets/image-20220918110957899.png)



* Third solution
  * Do not move records, but create a free record list
  * Book-keeping info
    * For each record, need a pointer pointing to the first free record
    * Each free block will need to have a designation that it is free
    * And a pointer pointing to the next free record
    * Also a way to denote end of the list

* Advantages / Disadvantages?



<img src="File%20Structures.assets/image-20220918111054741.png" alt="image-20220918111054741" style="zoom:67%;" />

> There is no free lunch. Maintaining a empty maintaining a list of free records also take time and effort. But the, you avoid moving records all together. And that's something to be said about it. Especially if you have a very complicated data structure where things are pointing left and right.



## Page structure: Variable length record

* Cannot predict how many records are there in a page

* And each page can be of variable length

* Solution

  * A slotted page header containing

    * \# of records in that page
    * The starting location and size of each record
      * Why do we need size?
    * Notice that typically we put a limit on number of records

  * Records can be moved around within a page to keep them contiguous with no empty space between them; entry in the header must be updated.

    

![image-20220918111250715](File%20Structures.assets/image-20220918111250715.png)

![Screen Shot 2022-09-19 at 13.30.52](File%20Structures.assets/Screen%20Shot%202022-09-19%20at%2013.30.52.png)



## Large objects (Blobs)

* Records must be smaller than pages

* Alternatives:
  * Store as files in file systems
  * Store as files managed by database
  * Break into pieces and store in multiple tuples in separate relation
    * PostgreSQL TOAST

![Screen Shot 2022-09-19 at 13.40.29](File%20Structures.assets/Screen%20Shot%202022-09-19%20at%2013.40.29.png)





## Organization (ordering) of records

* How should records in a file be organized (ordered)?

* One file per table:

  * **Heap** – record can be placed anywhere in the file where there is space

  * **Sequential** – store records in sequential order, based on the value of the search key of each record

    >  heap is kind of the most one of the most overloaded term in computer. You take the word heap can mean completely different thing. So be careful.

* With indexing option:
  * **B+-tree file organization**
    * Ordered storage even with inserts/deletes
  * **Hashing** – a hash function computed on search key; the result specifies in which block of the file the record should be placed

* Multiple tables per file:
  * In a **multitable** **clustering file organization**  records of several different relations can be stored in the same file
  * Motivation: store related records on the same block to minimize I/O

![Screen Shot 2022-09-19 at 14.25.52](File%20Structures.assets/Screen%20Shot%202022-09-19%20at%2014.25.52.png)



### Heap file 

* Records can be placed anywhere in the file where there is free space

  > I say I want to emphasize again, heap means really not no structure.

* Records usually <u>do not move</u> once allocated

  > do not move, so that means you have to. So when you delete a record, this one, this thing we probably didn't mention here, but you think about it. What do I mean by deleting a record? So setting it to zero.  
  >
  > You might also have to for each page you probably will have l for each cut you have to have an extra bit. To tell them whether this is empty or this is still something and Kind of empty. So you to a 49 for 50 bytes you will probably need 51 bytes because that one byte do have a bit to tell you whether they it's empty on them. That is actually quite important. So you have two choices. You have a fixed line for a cut if everyone expects, and you're not going to move things around it not never a better idea to have an extra bit, which unfortunately usually means sort byte. We talk about free space maps and so forth to. To to organize the data to recognize whether they free space and ways to free space.

* Important to be able to efficiently find free space within file

* **Free-space map**

  * Array with 1 entry per block. Each entry is a few bits to a byte, and records fraction of block that is free

  * In example below, 3 bits per block, value divided by 8 indicates fraction of block that is free

    ![image-20220918111653694](File%20Structures.assets/image-20220918111653694.png)

  * Can have second-level free-space map

  * In example below, each entry stores maximum from 4 entries of first-level free-space map

    ![image-20220918111701111](File%20Structures.assets/image-20220918111701111.png)



* Free space map written to disk periodically, OK to have wrong (old) values for some entries (will be detected and fixed)

> as I say, remapping is the dangerous thing to do. We don't want the move to pause across pages because later on when we the next topic, the tablets index, after we go through this, every index can be once you have an index, then we have other things that point to it.
>
> Reorganizing  within a page is fine. But you have to move a couple between pace. You really have to think twice. One thing we want to do is sometimes you also want to very quickly figure out where that this free space that is for each piece. So that's what we call a free space map.
>
> There's free record days free. We can store on each page. We can also store it in a separate location in the file title. A file header. And you kind of had to start information about the whole file. So maybe, hey, the first piece of free space. The second page of free space. So, so, so forth. So we can do that.
>
> ![Screen Shot 2022-09-19 at 15.15.33](File%20Structures.assets/Screen%20Shot%202022-09-19%20at%2015.15.33.png)
>
> This is obvious as fast you think about it. Just find a divide instead of just find an empty space. So very fast. Very quick. However, if I want to search for something, things can be dicey.



### Sequential file

* Suitable for applications that require sequential processing of the entire file 
* The records in the file are ordered by a **search-key**
* **We sometime call this organization clustered via a search-key**

![image-20220918111737701](File%20Structures.assets/image-20220918111737701.png)

> Make searching the key very fast. Does it help searching based on Salary? It doesn't help at all. So that's why primary key is important. That's why if you remember your database class, we have something called candidate key and a primary key. A table may have multiple attributes that can serve as a key. We call them a candidate key. And based on the self candy key, the DBA or whatever, choose one of those as a primary key. Typically, once you choose the primary key. The database system will try to organize a data like this, or data will actually see some more data. They actually don't do this directly. They do it via an index such that the primary key is order so that you can search for it very efficiently.
>
> You cannot have two of them in a primary here at the same time. Why not?
>
> So if I have to print them, if I want to have the files both sorted by SMU, ID and SSN at the same time. Is that possible?  I may have a larger SMU ID, but a smaller SSN. 

* Deletion – use pointer chains

* Insertion –locate the position where the record is to be inserted
  * if there is free space insert there 
  * if no free space, insert the record in an overflow block
  * In either case, pointer chain must be updated

* Need to reorganize the file from time to time to restore sequential order

![image-20220918111810440](File%20Structures.assets/image-20220918111810440.png)

https://www.jianshu.com/p/ff7f5586a874

> as I mentioned, it's not a good idea to move records.You create extra page and then you respond to pointing to that page and then point it back



### Heap File vs. Sequential File

* What’s the difference?
* Heap file:
  * Relatively little insertion cost

* Sequential file:
  * Cost involved when insertion (to maintain sorted)
  * Or have to sort every time (expensive)

* So why even think about sequential file?
  * It helps with some queries

>```sql
>SELECT * 
>From Faculty
>where ID = "1012345"
>```
>
>| 1    | 2    | ...  | 1000 |      |      |      |      |      |      |
>| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
>
>Let's say your faculty table have 1000 pages. And each page has ten tuples. I never say ID is a primary key. How many tuples of this query return. 
>
>If ID are primary key, how many tuples return?      One
>
>Given this type of a thousand page, how many page do I have to read? One
>
>Why if it's not sorted, if you heap file ?      A Thousand     have to read everything to know whether it exists. There's no choice. So but if you have an index, you do a binary search. $logn$



> in a this space environment, a binary search may not be as worthwhile as you think. Let's assume we store the file on a track. Sequentially. If you do a binary search? 
>
> That means you are from a page, you jump to a page to is not consecutive. If you have a hot, magnetic hot drive, what will happen? That means you have to wait for rotation, to say the least. Because this page is here. The next page you need might be far away.
>
>  If it's a solid state drive, then that's no problem. You definitely should do Binary Search.

* Example: (used for the rest of the slides)

  * Two tables

    * `Department(dept_name, building , budget)`
      * Assume each tuple is 40 bytes
      * `dept_name` is key

    * `Instructor(id, name, dept_name, salary)`
      * Assume each tuple is 50 bytes
      * `id` is key, `dept_name` is foreign key (referencing Department)

  * Assume data are stored on disk

    * Each page has 1050 bytes
    * Assume 50 bytes are needed for overhead information
    * Assume the pages are fully filled

  * Now assume Department has 100,000 tuples

    * So number of pages = $\frac{100000 \times 40}  {1050-50} = 4000$ pages

      > The notice that this may be wrong. Why?
      >
      > These assume what? Every page is fully filled. That means there is a danger of having pages across boundaries. If we don't want to do that, wash it. How should we calculate? We should actually ask first. How many tuples can we store in a page?  My page is 1000 bytes. Each tuple is 40 bytes. so each page can store how many bytes?
      >
      > $\frac{1000}{40} = 25$ In this case, I'm funny because it's total really well. 
      >
      > So each pages can store 25 tuples, how many tuples do I have ? 100000
      >
      > $\frac{100000}{25}= 4000$ pages
      >
      > But if each tuple is 90 bytes. So each page $\frac{1000}{90} \approx 11$ tuples
      >
      > $\left \lceil \frac{100000}{11}\right \rceil =\left\lceil 9090.9090...\right\rceil = 9091$ pages

  * Assume Instructor has 400,000 tuples

    * So number of pages = $\frac{400000 \times 50} {1050 – 50} = 20000 $pages





* Now consider the following query

  ```sql
  SELECT * FROM Instructor 
  where id = “1997”
  ```

* Now if you have a heap file
  * You have to look for each tuple
  * You can stop when you find the tuple (why?)
  * Worst case: no instructor has such ID
  * In this case, you have to search the whole file
    * Total cost = 20,000 pages
  * However, if Instructor table is sorted via id:
    * Then can apply binary search
    * Total cost =ceiling( $log_2(20000)$ ) = 15 pages



* Now consider the following query

```sql
 SELECT * FROM Instructor 
 where id = “1997”
```

* However, <u>for magnetic disk, we need to worry about seek/rotation</u>

  * For binary search, <u>subsequent searches are not on consecutive pages</u>

  * Thus need rotate (or even seek)

  * Now suppose reading a page take s seconds, and a rotate/seek take $100\times s$ second 

  * Then time for heap file = $100\times s + 20000\times s = (1 seek + 20000 read) = 20100 \times s$

    > If I don't follow anything of the read the whole thing, I have to do one see, one rotate.

  * Time for sequential file = $100\times s + log_220000 \times (100 \times s + s) = (1 seek + 15 rotate \ and\  read) = 1512 \times s$

  * Still win, but not as big a gap

    > But the win is not as drastic as before. So that's what I want you to be aware of. And that's what that's kind of also give you a peek into why, if the database optimization is such a tricky thing because you don't, you have to.
    >
    > Because in this case there is a potential large overhead to do the binary search and we actually   
    >
    > need to do the actual calculation if to file big enough so that the extra overhead doesn't matter.
    >
    > Now, once again, it's not meant for a human being to do this calculation. If you pay a lot of money to buy the system, it makes the database that is calculation for you. But it is important for you to know that, hey, these calculations need to be made.



* Now consider the following query

  ```sql
  SELECT * FROM Instructor 
  where id = “1997”
  ```

* What is the file is smaller (e.g. 400 pages)
  * Then time for heap file = 100s + 400s = 500s
  * Time for sequential file = 100s + ceiling( $log_2(400) ) \times(100s + s)$ = 706s 
  * <u>Binary search on sequential file is not worth it</u>

> So things are trickier in the data base than in algorithmic context because we are typically not talking about the input size that is so big that we only need to look at order in an order and square.



* Now consider the following query

  ```sql
   SELECT * FROM Instructor 
   where salary > 1000
  ```

* Sorting through ID will not help
* In either case, one MUST read the whole file no matter what

* Sequential file doesn’t help

> Does it matter whether the Id sorted? Not at all. Because there's no assumption that your theory is dependent on your id. So sequential file doesn't help here.
>
> this simple some example will be seen as a co introduction to the complications that we're going to see later on.



> Q: records go into a file and our files are there and there be multiple files within a block. Or is it the other way?
>
> A: So we have files. We have records, blocks, sectors. 
>
> sector is the basic unit hardware. So let's say this sector basically. That's the kind of what we call the lowest level addressable location.
>
> For example, your house, I send a mail. You want to send a mail to you. Let's say your address is 100, 1400 pensylvania Avenue. So I send a message. You live in that house?  Frankly, you only rent a bedroom on the second floor. I cannot send email to second bedroom of 14,000 Pennsylvania Avenue. I only can send the mail to 14,000 Pennsylvania Avenue. So the 14,000 is a lower addressable level. So there's a second. So your post office, postman doesn't care about whether you live in the second bedroom or the third bedroom. Or you live in that dog house is still going to be only that address. So it's what we call the lowes addressable address. Blocks are more or less a software level. Now especially remember during the discussion  of your harddrive. We talk about we want to minimize because we talk about seek and rotation. And we want to minimized debt as much as possible. So it may be it is probably to the system advantages. Every time I read, even though I can really with one sector and another sector and in another sector, I do rather read a bunch of consecutive set posts and think of it as a single unit. Right now, maybe I don't need everything from those three sectors. Fair enough. But it is better for me to read extra stuff and store it locally than have to make multiple trips later on.So that single unit is thing of a block, right? So this is a block. Now, in some literature, they do mix the two turns. So sometimes they call sector, a block club, a sector. so you may want to look at the context of the text to understand the difference between the two. And there are people who will interchange the usage of these two terms. So basically you have the lowest addressable level of storage. You can be unit of storage, you can get a sector. Then the software design, every time I read three consecutive sectors, no questions asked. I will rather have buffers in my memory set aside to store that extra information. I don't need it when I read it like we talked about the trail right. 
>
> now, records and files are completely software structure that's beyond power. Files and records are all logical structures. The hard disk can tell us whether you have a file on the that. The hard disk only care about 1 and 0. It's the operating system. all operating system come with a file system. That is where you define what is a file and the file can be broken down into records. So these are all logical level constructs. How the system meshed a file in two blocks is completely is either the OS decision or the database decision.
>
> But to be fair. Even at this level, some people will actually in the change the use of records and blocks is getting a bit dicey because the records is like for example really a but you look at the cross one database there is a tuple. A tuple can be very big. 



>  so technically a block can be of many sectors a record can be on many blocks, although technically a block has to be at least one sector because a sector is the basic unit of everything. although technically a block has to be at least one sector because a sector is the basic unit of everything. And a file is a collection of records. 



> you need that perspective for you to be a better even a programmer or understand what's going on behind the scene.
>
> And part of this class is doing this from a database perspective, pretty much from like the last couple of lectures on. For the next few weeks, we are going kind of under the hood a little bit, as we mentioned. That's why we asked you to take some low level classes like assembly, like principal programing, languages.

![IMG_0372](File%20Structures.assets/IMG_0372.jpg)

![Screen Shot 2022-09-22 at 15.51.34](File%20Structures.assets/Screen%20Shot%202022-09-22%20at%2015.51.34.png)



#### Addition: How to sort a file

* Suppose you do want to sort a file on the disk

  * And store the results on the disk

  * E.g. 

    ```sql
    SELECT * from instructor ORDER BY salary
    ```

* Simple solution
  * <u>Read the whole file into main memory</u>
  * Sort it using your favorite sorting algorithm
  * Write the whole file back to the disk

* What if the file is too large to fit into main memory?

  * **==Remember comparing value can only occur when both tuples are in main memory==**

    > ![ ](File%20Structures.assets/IMG_0376.png)

  * So we cannot just do a one pass sorting

  * Sorting need to be done in stages

  * Merge sort

> Please do not use bubble sort

> So you have to read the numbers into main memory before you can compare it, before you can think about something. But you don't have enough memory to read the whole thing. See the problem here. Let's say your file is four times bigger than your available memory. You can read the first quarter, then put it back and so forth



> merge sort disadvantages: 1. Space

>Compared with quick sort what the merge sort advantage
>
>quick sort you can do in place but merge sort you cannot 
>
>worst complexity of quick sort is $n^2$
>
>worst complexity of merge sort is nlogn
>
>The merge sort will guarantee the nlogn performance. quick sort you have to depend on luck. 

![IMG_541802237655-1](File%20Structures.assets/IMG_541802237655-1.jpeg)

> Q: the main memory limited why merge sort work here?
>
> A: merge sort  是分段来完成的所以在这个过程中, 可以先处理一部分进行排序, 排序好的进行空间释放. And then whenever one of the list is exhausted, then I will bring in the next part of the list and continue the merging process. So that's why merge sort works. So the key here is the merging step does not require you to have everything in the main memory at once. That's the most important thing to remember. That's why it makes merge sort work.
>
> 



#### Sorting a file: Merge sort

* Merge sort
  * Start by breaking tuples into list of one tuple
  * At each iteration, merge pairs of list until half the list remains
  * Repeat until all lists are merged

* We use the same basic algorithm but with some modification



* Assumptions

  * We have a file with N pages

    > Once again, pages and blocks. I'm going to use it interchangeably.

  * We have B pages of main memory available (B < N)

  * Number of pages read/written are the main cost (we assume sorting in main memory is much faster that the time can be ignored)

    > We assume I/O time is going to dominate. And even for solid drive, this is still probably going to be true. We assume once you retrain to make a memory comparing them, take no time. And in database systems. It is a fair assumption unless you do something very complicated.



* Step 1: Creating the initial list

  * Instead of creating list of one tuples, we can use the amount of main memory available

  * So read B pages from the file at a time

  * In the memory, sort the B pages using any efficient sorting algorithms

  * Write the B pages back to the disk somewhere

  * Repeat until every page is read and written

  * Total page read/written for this step = 2N

    * Each page is read/written once

  * At the end of this step: ceiling($\left \lceil \frac{N}{B} \right \rceil$) list is formed, each (possibly except the last one, have length B)

    > So in your traditional merge sort, you start by breaking the list until you have only one element. But here we don't need to go that extreme. If we assume that time spent main memories free, what can we do?
    >
    > We will first read the first B pages of the file. We read into the main memory. We sort this B pages by our favourite sorting algorithm. Please do not do bubble sort. and write this out in a separate file or separate location on this. So we now have a sorted list of pages. Then I read next B page into main memory. Then I will have a second sorted list of B pages. Do the same thing again and again until I'm done. 
    >
    >  So at the end of this step, how many lives do I have?
    >
    > A: $\left \lceil \frac{N}{B} \right \rceil$ Because you cannot have 20.6 files. You either you have to have 21 of this the last model.
    >
    > Now the list technically for the algorithm to work the list does not have to be the same size. We assume there is the case to make. Like to make the description easier.

    > How much time does it take? Every page I need to read into the memory. How many times? 
    >
    > Read: from file to main memory once
    >
    > write: sorted and then write once
    >
    > So we read things once. The whole thing is one and the whole thing is written once. But it's written in part. But it's read in part. But everything is done once every page is touched once, essentially.
    >
    > Totally: 2N
    >
    > ![IMG_0380](File%20Structures.assets/IMG_0380.jpg)

    > No assumption. This is just the first step. I don't even start the merging yet.
    >
    > I'm creating notice that at the beginning of this that we have one big file that is not sorted. At the end of this step, we'll have an  $\left \lceil \frac{N}{B} \right \rceil$ list and each list is sorted. Because we remember we can only sort things out in memory. Then there's the combination of read and write. Read plus written if you want to keep.

    

* Step 2: Merging 2 lists
  * Divide the B pages of main memory into two groups
  * Pick 2 list, read the first part of one list into one group, and the first part of the second list into the other
  * Use the standard merge function in mergesort to merge
  * Need to write the merged page to the disk along the way (unless there is output buffer available)
  * When one list is exhausted, than read the rest of the list
  * Time for an iteration = 2N (once again, each page is read and written once)

![IMG_0451](File%20Structures.assets/IMG_0451.jpg)



* Step 3: Until done
  * The total number of iterations = ceiling($log_2(\frac{N}{B})$)

* So the total page read/written

  $2 \times (1 + ceiling(log_2(\frac{N}{B}))) \times N$



##### Sorting a file : Merge Sort (example)

* Suppose you have a file with 12,800 pages
* Assume you have 200 page of memory available.
* First step:
  * Read the first 200 pages of the file into main memory
  * Sort it
  * Write the sorted list somewhere on the disk (on consecutive blocks)

* At the end of the first step, there are a total of $\frac{12,800}  {200} = 64$ sorted segments, each of them contains 200 pages



* Second step

  * Put the 64 segments into groups of 2 (32 groups)

  * For each group, apply the merge algorithm in merge sort

    * However need to remember merging can be done only when data is in main memory

    * So for each group

      * Divide the main memory equally into 2 part (100 page each)

      * Read the first 100 page of each segment
      * Apply the merge algorithm, until one of the segment (100 page) is used up
      * Then read in the rest of that segment into the main memory and continue
      * Continue merging (if the first 100 of the other segment is used up), bring in the next 100 page
      * Until one of the segments is completely merged
      * Then write the rest of the remaining segment to the disk 
      * Now a sorted segment of 200 + 200 = 400 pages is formed

    * Repeat for all groups, so now we have 32 sorted segments, each with 400 pages

  

* Third step (next iteration)
  * Put the 32 segments into groups of 2 (16 groups)
  * For each group, apply the merge algorithm in merge sort
  * However need to remember merging can be done only when data is in main memory
  * So for each group
    * Divide the main memory equally into 2 part (100 page each)
    * Read the first 100 page of each segment
    * Apply the merge algorithm, until one of the segment (100 page) is used up
    * Then read in the next 100 pages of that segment into the main memory and continue
    * Continue merging (whenever one of the 100 pages part of a segment is used up), bring in the next 100 page
    * Until one of the segments is completely merged
    * Then write the rest of the remaining segment to the disk 
    * Now a sorted segment of 400 + 400 =800 pages is formed
  * Repeat for all groups, so now we have 16 sorted segments, each with 800 pages



* Subsequent steps (continued)
  * Merge 16 segments of 800 pages by pairs , forming 8 segments of 1600 pages
  * Merge 8 segments of 1600 pages by pairs, forming 4 segments of 3200 pages
  * Merge 4 segments of 3200 pages by pairs, forming 2 segments of 6400 pages
  * Merge the 2 remaining segments, forming 1 sorted file



> Q: Can we do it in fewer iterations?
>
> Every mergesort how many at a time ? 2  Is it required by law? NO
>
> So why can't we merge most list at a time. So the same principle applies, right?
>
> If I have four list, I want to move together. What can I do? I will have for Points. Each of them point to the beginning of the list. And when you move to list, I need to do one comparison. Here is where I pay the price. I will find the minimum of awful numbers. But there's one more point and then I will. this is a smaller. So this has to be the front of this. I will move this to here. Then I'll compare free 1493, which was the smallest, free to smallest. It turns out the gain you have emerging more or less is offset by every time you compare a lot of elements.
>
> 

![Screen Shot 2022-09-23 at 23.12.46](File%20Structures.assets/Screen%20Shot%202022-09-23%20at%2023.12.46.png)



### Sorting a file: Merge sort

* Modification:
* Since we have B buffers available
* We can actually merge more than 2 list at a time
* In the extreme, we merge B-1 list at each step
  * Pick B-1 list
  * Assign one page in main memory to each list
  * Read the first page of each list into the corresponding memory
  * Continue the merge process
  * Time taken: $2 \times (1 + ceiling(log_{(B-1)}\frac{N}{B}))) \times N$

> every time you only need to get the smallest number and you put an new number in. That's exactly what a particle is useful. So if you're willing to spend a little bit more time organizing them in memory, even merging 99, this is not going to be that horrible. But we won't go into detail and I won't ask you questions on this point. But I do want to ask you, there's a possibility. So in theory, this works right now to over 10,000 and 110,000. That's a drastic difference. So let's say if we do that, we we might suck the seventh iteration into free. Notice that iteration. I still read each page once and write each page once, no matter how many lists I much for each iteration. Every page still need to be read one correct and every page still need to be written once only. So really the running time here, at least in terms of number of pages and written, is really only being dominated by the number of iterations. You can do a few iteration and get it sorta as much as as fast as possible. so the question becomes why not do it right?
>
> Why do we want to make as many pages and at least as possible? 
>
> There is no free lunch. So we have to pay somewhere. What are we paid? Give us give you a hint. Assume we actually stored data in the hard drive. Not a solid state drive. What can go wrong?
>
> Pay: more seek time
>
> And that's the one moment we have an account for it. Remember when I doing the merge step? Right. I say which one is the smaller number and when. I have a small but I have the immediate right time to do this. Remember, I need to find a page to write things down. There is another seek. Because you defined it, you can you can override the existing thing. You have to find an alternative place to write your result. So, number one, what I do just now is a very silly thing to do because I do a lot of things.

<img src="File%20Structures.assets/IMG_0452.jpg" alt="IMG_0452" style="zoom: 50%;" />



* In theory, it works well

* But issues

  * We haven’t factor in output need
  * One probably should not write a tuple to storage every time a single merge step (comparing 2 (or B) tuples) is taken
    * Why?
  * So need to assign memory pages for output
  * Also, for each read/write operation, there is a potential seek/rotate for hard drive
  * **<u>The more segements we merge with one step -> less space for each segment -> there are more reads require to read the segments -> more seeks.</u>**

   

### Multitable Clustering File Organization

![image-20220918114442584](File%20Structures.assets/image-20220918114442584.png)

> Why not just organize the whole thing like third table?  What is this table doing? Well, it is valuing if thought of computer science department and then order to pull in the instructor table. There is the instructor from the computer science department. Then you store the physics department and order instructor from the physics department. And we combine them into a single file. Essentially, we are doing the joint first. We are anticipating we are going to do the joint anyway. So why not do it first for. So.

* good for queries involving *department* ⨝ *instructor*, and for queries involving one single department and its instructors

* bad for queries involving only *department*

  > However, if you want to ask just in what department, then you have to read every pupil in the instructor table too. So that may waste a lot of time. So once again, you have to decide whether you want to do this by determining in real life how likely you're going to ask query on the format itself and how often do you need to do a job?

* results in variable size records

* Can add pointer chains to link records of a particular relation

>So if you have a foreign key, there is at least reasonable assumption to assume that you will join these two. They quite often. But not always. But there's a chance. If there's a chance of doing this. And as you see later on, join can be expensive.





### Partitioning

* **Table partitioning**: Records in a relation can be partitioned into smaller relations that are stored separately
* E.g., *transaction* relation may be partitioned into 
    *transaction_2018, transaction_2019, etc.*
* Queries written on *transaction* must access records in all partitions
  * Unless query has a selection such as *year=*2019, in which case only one partition in needed

* Partitioning 
  * Reduces costs of some operations such as free space management
  * Allows different partitions to be stored on different storage devices 
    * E.g., *transaction* partition for current year on SSD, for older years on magnetic disk





## Data Dictionary Storage

The **Data dictionary** (also called **system catalog**) stores **metadata**; that is, data about data, such as

* Information about relations
  * names of relations
  * names, types and lengths of attributes of each relation
  * names and definitions of views
  * integrity constraints

* User and accounting information, including passwords

* Statistical and descriptive data
  * number of tuples in each relation

* Physical file organization information
  * How relation is stored (sequential/hash/…)
  * Physical location of relation 

* Information about indices (Chapter 14) 





## Relational Representation of System Metadata

* Relational representation on disk

* Specialized data structures designed for efficient access, in memory

![image-20220918114747953](File%20Structures.assets/image-20220918114747953.png)





## Column-Oriented Storage

* Also known as **columnar** **representation**
* Store each attribute of a relation separately
* Example

<img src="File%20Structures.assets/image-20220918114820987.png" alt="image-20220918114820987" style="zoom: 67%;" />





## Columnar Representation

* Benefits:
  * Reduced IO if only some attributes are accessed
  
  * Improved CPU cache performance 
  
  * Improved compression
  
    > You do need to compress data because all the data are the same type that make it easier to compress. It won't make you easier to compress, just make you can get a higher compression rate.
  
  * **Vector processing** on modern CPU architectures

* Drawbacks
  * Cost of tuple reconstruction from columnar representation
  * Cost of tuple deletion and update
  * Cost of decompression

  > No free lunch. You do have to spend time to build the tuple. Even if your query is a select start then you as group.
  
* Columnar representation found to be more efficient for decision support than row-oriented representation

* Traditional row-oriented representation preferable for transaction processing

* Some databases support both representations
  * Called **hybrid row/column stores**





## Columnar File Representation

* ORC and Parquet: file formats with columnar storage inside file

* Very popular for big-data applications

* Orc file format shown on right:

![image-20220918114957971](File%20Structures.assets/image-20220918114957971.png)





## Storage Organization in Main-Memory Databases

* Can store records directly in memory without a buffer manager

* Column-oriented storage can be used in-memory for decision support applications

* Compression reduces memory requirement

![image-20220918115022471](File%20Structures.assets/image-20220918115022471.png)