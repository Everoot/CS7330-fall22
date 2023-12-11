# Quiz 1 ✅

1. Which of the following about the MongoDB query language is true? ✅

   (a)  db.collection.find( {“state": "TX", “pop” : 20000} ) returns all document with key/value pair ("state", "TX") OR ("pop", 20000) ❌

   (b)  db.collection.find({“state” : null}) will only returns document that does not have a "state" key ❌

   A. (a) and (b) 

   B. Neither (a) nor (b) ✅

   C. (b) 

   D. (a) 

   My Answered: B

   Correct Answer: B
   
   (a) It will returns all documents with key/value pair `("state", "TX") AND ("pop", 200000)`, the logical is `And`.
   
   > ### selection
   >
   > * Basic method: find()
   > * `db.collection.find( {<selection>}. {<projection>} )`
   >   * Describe the documents to be retrieved
   >   * Each of this has the same format as a document (but without the_id).
   > * `db.collection.find({})`
   >   * Return all documents in the collection
   > * `db.collection.find({"name" : "john doe", "age" : 30})`
   >   * ==**Return all documents that have BOTH key value pairs**==
   >   * Logical And
   > * Note:
   >   * Value in the key/value pair in find must be a constant.
   >   * Need other constructs to relate different documents from the same/different collections
   >
   > > if you want to be restricted, you are essentially doing kind of a matching by matching columns, all by matching attributes
   >
   
   (b) it will return documents that does not have a "state" key OR the documents have the "state" key and the value is `null`.
   
   > ### ==NULL values==
   >
   > * ==BE VERY CAREFUL!==
   >
   > * Suppose your collection has the following docutments:
   >
   >   * `{"_id": "1", "name": "john doe", "phone": null}`
   >   * `{"_id": "2", "name": "jack doe", "age": 28}`
   >
   > * `db.collection.find({"phone": null})` will return BOTH documents
   >
   >   * Null matches either "having the value null", and "no such key exists in the document"
   >
   >     > If you try to do this form equal to now, then you will return both documents, you have to be careful about what this empty string means
   >
   >   * Use the "$exists" clause to compensate
   
   



2. Consider modeling two entities ("Student" and "Faculty", each of them having multiple properties), and a relationship between them ("Advise"). Suppose we want to embed Faculty documents as part of the Student document (but not vice versa). Under what condition will this be a reasonable choice (as if without causing duplication and potential inconsistencies)?

   (You can also assume these are the only entity/relationships that needs to be modeled)

   (a) if Advise is a 1-1 relationship

   (b) if Advise is a 1-n relationship (with 1 student having many advisers, but each faculty having only 1 advisee

   (c) If Advise is a 1-n relationship (with 1 faculty having many advisers, but each student having only 1 advisor

   (d) If Advise is a m-n relationship (with m, n > 1) 

   > 2. A. (d) 
   >
   >    B. (a) and (c) 
   >
   >    C. (a) and (b) ✅
   >
   >    D. (a), (b), (c) and (d) 
   >
   >    My Answered: C
   >
   >    Correct Answer: C
   >
   >    题意Student(Faculty)
   >
   >    (a) 可以嵌套 因为 是 1-1 Student(Faculty(Advise))
   >
   >    (b) 可以embed, 1-n Student(Faculty{Advise1, Advise 2 ...})
   >
   >    (c) ❌ Student(Faculty({Advise1, Advise 2,....}) Advise 1) -> duplication
   >
   >    (d) ❌ duplication + inconsistencies 
   >
   
   

3. The uniqueness constraints in Cypher refer to:

   A. Specify no two nodes can have <u>the same number of properties</u> 

   指定两个节点不能具有相同数量的属性

   B. Specify <u>no two nodes of the specifed label can be joined by an edge</u> 

   指定指定标签的两个节点不能被边连接

   C. Specify all nodes <u>must have distinct labels</u> 

   指定所有节点必须有不同的标签
   
   D. Specify all nodes that have a certain label must have distinct values in the property that is specified ✅
   
   My Answered: D
   
   Correct Answer: D
   
   > A. ❌ don't care about the number of properties, just care about the a specific label.
   >
   > B. ❌ 可以
   >
   > C. ❌ make sure the have a specific label is ok. 
   >
   > D. Unique node property constraints
   > Unique property constraints ensure that property values are unique for all nodes with a specific label. For unique property constraints on multiple properties, the combination of the property values is unique. Unique constraints do not require all nodes to have a unique value for the properties listed — nodes without all properties are not subject to this rule.
   >
   > 唯一节点属性约束
   >
   > 唯一属性约束确保属性值对于具有特定标签的所有节点是唯一的。对于多个属性上的惟一属性约束，属性值的组合是惟一的。唯一约束不要求所有节点对列出的属性都有唯一值——没有所有属性的节点不受此规则约束。



4. For graph model databases, which of the following is/are correct?

   (a) Subgraph pattern matching is not often implemented because it is NP-complete

   (b) For path queries, one can restrict the types of edges for that path

   Correct Answer

   A. (a) and (b) ✅

   B. Neither (a) nor (b) ❌

   C. (b) 

   D. (a)

   My Answered: C

   Correct Answer: A

   > (a) ✅
   >
   > **==Pattern matching query==**
   >
   > * Find all subgraphs that is **==<u>isomorphic</u>==** to the query subgraph
   >
   >   找到所有与查询子图同构的子图
   >
   > * Gerneral graph isomorphism is ==**NP-complete**==
   >
   >   一般的异构图是np完备的
   >
   >   > P是一个分类, 基本上包括所有可以用相当快的程式解决的问题, 如乘法或者排序
   >   >
   >   > 然后 有个包含P类的NP类: 如果你作出了正确的解决方案, 可以在一个合理的时间量检验它的方案是否正确. 
   >   >
   >   > https://www.youtube.com/watch?v=YX40hbAHx3s
   >   >
   >   > https://www.bilibili.com/video/BV1WW411H7nH/?spm_id_from=333.999.0.0&vd_source=73e7d2c4251a7c9000b22d21b70f5635
   >   >
   >   > 即能用多项式时间验证解的问题是否能在多项式时间内找出解
   >
   > * **==Tree==** isomorphism has polynomial time solutions
   >
   >   树同构有多项式时间解
   >
   >  (b) ✅
   >
   > ==**Path query**==
   >
   > * Whether a path exists between two given vertices
   > * **==Conditions on the edges along the path==**
   > * Can also be given only one vertex and find all the other vertices that can be reached/can reach it from the query vertex.



5. Which of the following about Solid State Drive  (SSD) is correct?

   (a) Seek time for a SSD is the same as rotational latency ❌

   (b) One cannot rewrite on the same spot of the SSD drive without erasing a larger block first ✅

   (c) There is not much difference in reading sequentially and randomly in an SSD ✅

   A. (b) and (c) ✅

   B. (c) 

   C. (a), (b) and (c) 

   D. (a) and (b) 

   My Answered: A

   Correct Answer: A
   
   > 5. (a) SSD has no rotational latency.
   >
   >    (b) SSD 
   >
   >    Applying electricity in different way can “erase” the bit and allow it to be rewritten again
   >
   >    * Erase first, than rewrite
   >
   >    写一个闪存页面通常需要几微秒, 然而, 一旦写入, 闪存的页面不能直接覆盖, 它必须先擦出然后再重写.一次擦除操作可以在多个页面执行, 称为擦除块(erase block), 这种操作需要时约1-2毫秒.
   >
   >    (c) no need to seek time and rotational latency. 
   >
   > 
   
   
