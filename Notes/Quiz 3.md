# Quiz 3

1. Which of the following statements about B+-tree is correct?

   (a) Every node of the B+-tree has to be at least half full ❌

   (b) All data in a B+-tree are stored in internal nodes ❌

   A. Neither (a) nor (b)

   B. (a) and (b)

   C. (a)

   D. (b)

   A ✅

   > (a) only leaf node; internal node do not need that
   >
   > (b) no, just store the key and pointer. And leaf node can store data as the whole tuple, but few to do that.



 

2. Which of the following about the B-tree is correct?

   **==(a) All leaf nodes are at the same level==**

   (b) All elements that are stored are evenly distributed among the leaf nodes (to the best extent possible)

   存储的所有元素都均匀地分布在叶节点中(尽可能地最好) 

   A. (a) and (b)

   B. (b)

   C. (a)

   D. Neither (a) nor (b)

   (a). balance

   (b) 那肯定

   A ❌

   C ✅

   > (a) B-tree is balanced
   >
   > (b) ❌ 无中生有, 就算所有元素没有均匀地分布在叶节点中, 只要满足条件的B-tree的就行. 它不是B-tree的必须. 无此要求.



 

3. **==What do we mean by decorating a parse tree?  ✅==**

   我们所说的装饰解析树是什么意思?

   ==A. Deciding the algorithm to be used for each operation==

   B. Ordering the operations in the query

   C. All of the other answers are correct

   D. Translating the SQL statement <u>into a set of relational algebra operation</u> ❌

   My answer: B ❌

   My answer: A ✅

   > A.  决定每个操作使用的算法
   >
   > Optimization:
   >
   > * Decorating the nodes of a parse
   >
   >   * ==For each node, determine how that operation is to be executed==
   >
   > * Select the best parse tree
   >
   >   * For all the parse tree generated, pick the one that will execute the query fastest
   >
   >   >  Just because you have an index doesn't mean you have to use it. Does that mean it's worth it to use it? To make it even stronger.
   >
   > B. 排序查询中的操作
   >
   > C. D❌ 这个秒排
   >
   > D. 使SQL变成关系代数运算, 并不需要解析树 several databases use an annotated parse-tree representation based on the structure of the given SQL query. 而是使用parse tree 使得 SQL 查询更加视觉化,更好理解. 



4. For level k in linear hashing, how many buckets need to be split before we enter level k+1?

   A. $2^k$

   B. $2^{k+1}$

   C. $k$

   D. $2k$

    My answer: A ✅

   Correct answer: A ✅

   注意读题的意思, 对于线性哈希中的级别k，在我们进入级别k+1之前，需要划分多少个桶? 所以它问的还是klevel的,不要被k+1层迷惑了.

   >* Assume Hash function = rightmost k bit of the number (k changes with the algorithm)
   >
   >  假设哈希函数=数字的最右k位(k随算法变化)
   >
   >* For linear hashing, maintain two variables
   >
   >  对于线性哈希，维护两个变量
   >
   >  * Level: the current level of hashing,
   >
   >    Level:散列的当前级别，
   >
   >    * Starts at 0
   >
   >    * ==At the start of level k, there will be $2^k$ buckets==
   >
   >      在第k level开始时，会有$2^k$个桶
   >
   >      * E.g. k = 2, then buckets are 00, 01, 10, 11
   >
   >    * A level finishes when all the buckets at the start of the level is split
   >
   >      当level开始的所有桶被分割时，level就结束了

    





5. In linear hashing, whenever a bucket overflows when an iterm is inserted to it, the next bucket to be splited is:

   A. The bucket that just has the item inserted

   B. Bucket 0

   C. Pre-determined, unrelated to which bucket is full 

   D. The current bucket that has the most overflow buckets

   C ✅

   > Key ideas
   >
   > * Hash table entries <u>grow in a linear fashion</u>
   >
   >   散列表项<u>以线性方式增长</u>
   >
   > * ==Have a pre-defined order of splitting the bucket, **regardless of which bucket is overflowing**==
   >
   >   有预定义的划分桶的顺序，而不管哪个桶溢出
   >
   >   就像example 中的, 使用了overflow bucket 就让它的另一半拆分 然后重新散列
   >
   >   * A overflow bucket must wait for its turn to be split (rehashed)
   >
   >     溢出桶必须等待轮到它拆分(重新散列)
   >
   >   * Need overflow buckets (linked list)
   >
   >     需要溢出桶(链表)
   >
   > A. a bucket overflows when an item inserted, 这个bucket使用了overflow bucket 所以它不会splited. 而它的另一半则会splited. 在example中使用的是另一半 即 01 的另一半为00, 这个是根据提前设置的, 它的另一半的可以根据某种规律设置成其他的.
   >
   > B. 无中生有
   >
   > C. 正确✅
   >
   > D. 使用了overflow bucket 就是为了减少分裂, 该选项与逻辑不符合.

    