# Quiz 2

1. Which of the following about RAID-1 is correct? ✅

   (a) Writing is always going to be at least twice at slow than RAID-0 ❌

   ==(b) RAID-1 should be more reliable than RAID-0==  ✅

   (c) RAID-1 use parity bits ❌

   A. (c)

   B. (a) and (b) 

   C. (b) ✅

   D. (a), (b) and (c)

   My Answered: B ❌

   Correct Answer: C
   
   > (a):  写入都是并行的 所以没有慢
   >
   > RAID-0: 块级拆分 
   >
   > RAID-1: 块级拆分 
   >
   > 两个可以并行
   >
   > (b): RAID-0: 多个disk 但没有备份
   >
   > RAID-1: 会把所有数据复制一份
   >
   > (c): RAID-1 是使用块级拆分的磁盘镜像 复制一份 没有用到 parity bit (校验位) 这个专有名词, 不是bit stripping的意思.不要搞混了. 论英文的重要性.



2. Which is the following is an advantage of multi-table clustering file organization? ✅

   ==A. Joins involving those tables can be potentially speed up== ✅

   B. Selection for <u>one of the tables</u> can be speed up ❌

   C. All of the other answers are correct ❌

   D. Projection for <u>each</u> of the tables can be speed up  错

   My Answered: C

   Correct Answer: A
   
   > A. 
   >
   > * ==**good for queries involving *department* ⨝ *instructor*, and for queries involving one single department and its instructors**==
   > * bad for queries involving only *department*
   > * results in variable size records
   > * Can add pointer chains to link records of a particular relation
   >
   > B. ❌ Selection for one of the tables can not be seed up,
   >
   > 对于单一的表表格访问不好. 速度会变慢
   >
   > C. ❌
   >
   > D. 并不可以加快每个表的投影, 它对单一的表的操作不好.
   
   

3. **==Which of the following about external merge sort is correct?==**

   (a) The first step of merge sort is to <u>create list of one tuple each</u> ❌

   ==(b) For external merge sort, one can merge more than 2 lists at a time== ✅

   ==(c) With a file of N pages, each iteration takes 2N pages of read+write== ✅

   A. (b) and (c) ✅

   B. (a), (b) and (c) 

   C. (a) and (b) 

   D. (c) 

   My Answered: A

   Correct Answer: A
   
   > (a) ❌ 归并排序的第一步是不是每个元组创建一个列表. 而是每个main memory 为底数, 把file除以它, 然后获得list, 这个list是关于 main memory可容纳的大小, 不是和tuple 有关. 所以错了
   >
   > Step 1: Creating the initial list
   >
   > * Instead of creating list of one tuples, we can use the amount of main memory available
   > * So read B pages from the file at a time
   > * In the memory, sort the B pages using any efficient sorting algorithms
   > * Write the B pages back to the disk somewhere
   > * Repeat until every page is read and written
   > * Total page read/written for this step = 2N 
   >
   >   * Each page is read/written once
   > * At the end of this step: ceiling($\left \lceil \frac{N}{B} \right \rceil$) list is formed, each (possibly except the last one, have length B)
   >
   > (b) ✅ 可以多于两个以上进行排序归并 $log_{B-1}(\left\lceil \frac{N}{B} \right\rceil)$
   >
   > B-1: 多少个一起并
   >
   > (c) ✅ 每次都要读, 读的话N个file 每次都要读一遍, 然后写, 也是Nfile 写一遍 N+N = 2N



4. Which of the following about selection queries using indices are correct?

   (a) A secondary index should always be used

   ==(b) One cannot know whether a secondary index should be used without knowing how many tuples are going to be returned==

   ==(c) If the attribute that is used to build a secondary index is distinct, a query such as "SELECT * FROM A where A.att = 1" should (nearly) always benefit from a secondary index.==

   A. (b) and (c) ✅

   B. (a), (b) and (c) 

   C. (c) 

   D. (a) and (b) 

   My Answered: A

   Correct Answer: A
   
   > (a) ❌ 我有, 但我可以不用
   >
   > (b) ✅ 先有鸡还是又蛋问题
   >
   > (c) ✅ 是的, 可以直接返回该值



5. **==Which of the following about non-clustering index is correct?==** ✅

   ==(a) A non-clustering index cannot be sparse== ✅

   (b) A non-clustering index cannot only be used on an integer attribute

   A. Neither (a) nor (b) ❌

   B. (a)  ✅

   C. (a) and (b) 

   D. (b) 

   My Answered: A

   Correct Answer: B
   
   > (a) ✅ 
   >
   > 稀疏索引必须是clustering的, 它需要排序的
   >
   > 所以非聚集索引不能称为稀疏索引, 它不是排序的
   >
   > Indices whose search key specifies an order different from the sequential order of the file are called nonclustering indices, or secondary indices.
   >
   > Sparse indices can be used only if the relation is stored in sorted order of the search key; that is,if the index is a clustering index.
   >
   > * Case 1: a clustered ordered index on salary
   >   * Notice that the tuples are sequentially ordered by salary
   > * Case 2: an unclustered ordered index on salary
   >
   > 
   >
   > Clustering index(聚集索引): 如果包含记录的文件按照某个搜索码指定的顺序排序, 那么该搜索码对应的索引称为聚集索引. 聚集索引也称为主索引(primary index); 主索引这个术语看起来是表示建立在主码上的索引, 但实际上它可以建立在任何搜索码上. 聚集索引的搜索码常常是主码, 尽管并非如此.
   >
   > Non-clustering index(非聚集索引): 搜索码指定的顺序与文件中记录的物理顺序不同的索引称为非聚集索引(non-clustering index)或辅助索引(secondary index). 
   >
   > (b) ❌
   >
   > 非聚集索引可以用在整数属性上, 如salary. 但是他只是不是排序的而已.
