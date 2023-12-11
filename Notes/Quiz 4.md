# Quiz 4

1. **==Consider we have a table A that has attributes A.a, A.b, A.c, A.d. with non-clustering indices on attributes A.a, A.b, A.c separately. Consider the following query==**

   ```sql
   SELECT *
   FROM A
   where <condition>
   ```

   For which condition below we can use the "intersection of identifiers" option to execute the query? (Notice I do not claim that the option will be the best, just a feasible one). 

   ==(a) condition is : A.a = 10 and A.b > 10 and A.c = 5==

   (b) condition is : A.a = 10 or A.b > 10 or A.d = 5  

   > because the d do not have the non-clustering indices therefore there is no intersection of identifiers for it. By the way it is or therefore we have to check every A.d =5

   ==(c) condition is : A.a = 10 and A.b = 10== 

   ==(d) condition is : A.a = 10 or A.b = 10==

   A. (a) and (c) and (d) ✅

   B. (a) and (c) ❌

   C. (c) and (d)

   D. (a), (b), (c) and (d) 
   
   > Intersection of identifiers: 标识符的意思, 不是什么交标识.



2. Consider set operations, which of the following statement(s) is/are correct?

   (a) Union corresponds to joins which match every attributes 

   (b) Intersection corresponds to joins which match every attributes

   A. (b) ✅

   B. (a)

   C. Neither (a) nor (b)

   D. (a) and (b)
   
   >(a)  Union对应于匹配每个属性的联结 ❌
   >
   >​	   连接所有不要每个属性都匹配, 不一样的属性也结合
   >
   >(b) 交集对应于匹配每个属性的联结	
   >
   >​	  交集需要共同的属性 一直 且条件一样才能写入结果
   
   
   
3. One advantage of hash-join over sort-merge is: 

   A. Hash-joins runs in linear time, but sort-merge runs in O(n^2) time

   B. Hash-join ordered the tuples based on the join condition, sort-merge does not

   C. There is no advantage at all

   D. The number of iteration is (potentially) bounded by the size of the smaller table in hash-join, but is definitely bounded by the larger table in sort-merge  
   
   ✅
   
   > A ❌ sort-merge runs O(n^2) 夸张了
   >
   > B. ❌ sort-merge order by the condition attribute
   >
   > C.  D 如果对 所以C 错
   >
   > D. 在hash-join中，迭代次数(潜在地)受小表大小的限制，但在sort-merge中，迭代次数肯定受大表大小的限制
   >
   > Comparing sort-merge and hash-join
   >
   > 比较sort-merge和hash-join
   >
   > * ==Hash-join is better than sort-merge when there is a large different between number of pages between the tables==
   >
   >   当两张表的页数相差很大时，Hash-join比sort-merge要好
   >
   >   * ==The number of iteration is dominated by the larger table in sort-merge (need to completely sort both tables)==
   >
   >     在sort-merge中，迭代次数由较大的表决定(需要对两个表都进行完全排序)。
   >
   >   * But is dominated by the smaller table in hash-join (need to recursive call until ==ONE== of the segment is small enough)
   >
   >     但在散列连接中主要是较小的表(需要递归调用，直到段的==1==足够小)
   >
   > * Sort-merge has more predictable performance 
   >
   >   排序合并具有更可预测的性能
   >
   >   * Hash join’s performance depend on how the hash function performs
   >
   >     散列连接的性能取决于散列函数的性能
   >
   >     > sorting algorithm is not affected by data distribution
   >
   > * Sort-merge has the output sorted by the join attribute
   >
   >   Sort-merge的输出是按照join属性排序的
   >
   >   * May be important (see later)
   >
   >     > This is better than hash join
   
   



4. Which of the following about the parse tree notation of a query is correct?

   (a) Each node can have at most 2 children

   (b) The leaves corresponds to tables

   (c) For nested loop, the right child is the inner loop.

   A. (b) and (c) 

   B. (a) and (b)

   C. (b)

   D. (a), (b) and (c) ✅

   ![Query Optimization -35](https://tva1.sinaimg.cn/large/008vxvgGgy1h85q53jja3j30u012r417.jpg)

    

5. **==Which of the following about pipeline/materialization is correct?==**

   (a) The inner loop of a nested loop join need to be materialized

   (b) An advantage of the left-deep tree is that pipelining is possible along the whole left-path of the tree.

   A. (a)

   B. (a) and (b)  ✅

   C. Neither (a) nor (b) ❌

   D. (b)

   > (a)嵌套循环连接的内部循环需要被物化
   >
   > because the join you have to remember something.
   >
   > the pipeline not work every time, when you do the select, you can do some part of select and do the join, but the join you have to remember something, because the inner join you have to read a lot time. 
   >
   > ![Screenshot 2022-10-29 at 20.44.48](https://tva1.sinaimg.cn/large/008vxvgGgy1h85q2736xcj31ey0godht.jpg)
   >
   > (b)左深树的一个优点是可以沿着树的整个左路径进行流水线。
   >
   > 左深连接顺序用于流水线计算特别方便, 因为右操作对象是一个已存储的关系, 每个连接只有一个输入来着流水线.
