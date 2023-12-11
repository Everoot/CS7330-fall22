# Chapter 16 Query Optimization

> So now we have understand how we do individual operations. The question becomes, how do we put things together.
>
> 中文 chapter 13

## Query Optimization ✅

对于一个给定的查询, 尤其是复杂查询, 通常会有许多种可能的策略, **查询优化(query optimizaiont)**就是从这许多策略中找出最有效的查询执行计划的一种处理过程.

* Step of query optimizaiton 查询优化步骤

* Given an SQL query 给定一个SQL查询

  1. Convert it to (enhanced) relation al algebra 将其转换为(增强的)关系代数

     > We have sql, the convert into relational algebra. I put the work in hand because things like by aggregation does not appear in the original relational algebra definition. But we can but we can think of them as extra operations so that it fits the it fit the paradigm.
     >
     > 我们有sql，转换成关系代数。我把这项工作放在手边，因为像by aggregation这样的东西没有出现在原始的关系代数定义中。但是我们可以但是我们可以把它们看作是额外的操作以便它适合它适合范式。

  2. Build ==multiple== parse trees 构建多棵解析树
  
     > ```sql
     > select * 
     > from A, B, c
     > where 
     > ```
     >
     > Just a query like this. `A, B, C` are $A\Join B \Join C$ . I can do $X_1= A \Join B$ first, then $X_1 \Join C$ . I also can do $X_2 = B\Join C$ first, then $A\Join X_2$ . I also can do $X_3 = A\Join C $ first, then $B \Join X_3$ . And each of them can have variety performance. It very often turns out that which query you need to do join first matters significantly in terms of performance. So you have to at the beginning, at the very least, keep all options open.
     >
     > 就像这样一个查询。`A, B, C `是$A\Join B \Join C$。首先是$X_1= A \Join B$，然后是$X_1 \Join C$。我也可以做$X_2 = B\Join C$，然后$A\Join X_2$。我也可以做$ X_3 = A\Join C $，然后$B \Join X_3 $。每个人都可以有不同的表现。通常情况下，哪个查询需要首先执行关联操作对性能非常重要。所以在一开始，你至少要保留所有的选择。
  
     * Note: Multiple ways to ==decorate a tree== 注意:装饰一棵树有多种方式
  
       > And you need to decorate a tree. How do we do a join? Do we do hash join?  Do we do sort merge? Do we do nested loop? If I do nested loop, which should be outer loop? Which should be inner loop? How many buffer do I set in the outer loop? How many buffer do I set inner loop? 
       >
       > In the DataBase system term is called a plan. Typically we call it a tree because this is classroom. Tree is something we're familiar with. When you go out in the world of DBA, they'll call each tree a plan.
       >
       > 你需要装饰一棵树。如何进行联结?我们做哈希联结吗?我们做归并排序吗?我们有嵌套循环吗?如果我使用嵌套循环，哪个应该是外循环?哪个应该是内循环?我在外循环中设置了多少缓冲区?内层循环设置了多少缓冲区?
       >
       > 在数据库系统中，这个术语称为计划。通常我们叫它树，因为这是教室。树是我们熟悉的东西。当你进入DBA的世界时，他们会把每棵树都称为一个计划。
  
     * Each decorated tree is also called a **plan**
  
       每棵装饰过的树也被称为一个**plan**
  
  3. Calcualte the cost of each plan 计算每个计划的成本
  
  4. Pick the best one 选择最好的一个
  
  > Sounds simple enough. Make perfect sense logically. But there are challenges.
  >
  > `1.` is hopefully standards now. `2.` already have issues. How many trees do I want to be?  Remember, we have three tables to join. We have free options. If you have four tables to join, how many options are there?
  >
  > Why do you need a table join? Many database systems are divided in what we call a star schema. we will see whether no sql can do better optimization than this was.
  >
  > 听起来很简单。在逻辑上完全有意义。但也有挑战.`1`有望成为现在的标准。`2`已经有问题了。我想要多少棵树?记住，有3张表需要合并。我们有免费的选择。如果有4张表需要联结，有多少个选项?
  >
  > 为什么需要表联结?许多数据库系统被划分为星型模式。我们将看到是否没有SQL可以做得比这更好的优化。
  
  > Remember, if you work for a company, do I care about which database system I use? If I'm the boss, I paid money for you guys to develop a system. All I care is performance. And you have a convenient, no thicker system, but the time to execute each query is 5 seconds lower. Do you think I want this system? No!
  >
  > Noticed that many Data System that is free for you to use. But if you need support, that's where Red Hat or whatever all those database company earn their money is support.  If you're a big company and you cannot accept somebody is failing? You have to have constant support. And that support is where those companies earn the money back.  They always have like Enterprise Edition. 
  >
  > 请记住，如果你为一家公司工作，我是否关心我使用的数据库系统?如果我是老板，我付钱让你们开发一个系统。我只关心性能。你有一个方便的，没有更厚的系统，但执行每个查询的时间减少了5秒。你觉得我想要这个系统吗?不!
  >
  > 注意到很多数据系统都是免费供你使用的。但如果你需要支持，红帽或其他数据库公司赚钱的方式就是支持。如果你是一家大公司，你不能接受某人的失败?你必须得到持续的支持。正是这种支持让这些公司赚回了钱。他们总是有像企业版。



## 16.2 Convert to relational algebra ✅

* In a 

  ```sql
  SELECT	...
  FROM	...
  WHERE	...
  ```

  SQL query

  * `SELECT	...` corresponds to $\pi$ 

  * `WHERE  ...` corresponds to $\sigma$

  * `FROM  ...` corresponds to $\Join$  (if corresponding `WHERE` course exists), $\times$ if not

  * `UNION, INTERSECT, EXCEPT` correspond to $\cup, \cap, -$

  * `GROUP BY, HAVING` and aggregate does not appear in relational algebra, so have extra operators added to accommodate it.

    而聚合并没有出现在关系代数中，因此需要添加额外的操作符来适应它.

  * We'll deal with ==nested query== later. 
  
    我们稍后将处理嵌套查询.
    
    > Nested query is a tricky thing. 
    >
    > Exist, not exist. In, Not in all these kind of stuff. Nowadays you can even that's the career in the in the from costs.
    >
    > 嵌套查询是一件棘手的事情。
    >
    > 存在，不存在。不是在所有这些事情上。现在，你甚至可以从成本中获得职业。
    
    > ```sql
    > select * 
    > FROM (select ...) AS A
    > ```
    >
    > Do I encourage the query in this way? Not necessarily. But you can do it. 
    >
    > 我鼓励以这种方式查询吗?不一定。但你可以做到。



* From the relational algebra, one can build a parse tree

  使用关系代数，可以构建解析树

* Parse tree specifies the order of execution of the operations

  Parse tree指定了操作的执行顺序

  * Post-order traversal of the tree

    树的后序遍历
    
    > Post-order traversal -> data structure class. 

* ==**<u>Notice that, for joins, we put the "outer loop" (if we want to do nested loop) on the left.</u>**==   

  注意，对于联结，我们把“外循环”(如果想做嵌套循环)放在左边



* Example

  ```sql
  SELECT S.id, I.id, I.salary
  From Student S, Instructor I, Advise A
  WHERE S.id = A.s_id AND I.id = A.i_id AND S.dept = "CS" AND S.gpa >= 3.5
  ```

  $\Pi_{S.id, I.id, I.salary} (\sigma_{S.gpa \ And \ S.dept='CS'}(Student \Join_{A.sid =S.id''}Advisor\Join_{A.iid=I.id''} Instructor))$

  

  <img src="/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-28 at 00.21.13.png" alt="Screenshot 2022-10-28 at 00.21.13" style="zoom: 25%;" />

> Each interal node is an operation, selection, projection, join may be even group by. Each leaf node is a table.
>
> 每个内部节点都是一个操作，选择、投影、join都可以连组by。每个叶子节点是一个表。
>
> ![Query Optimization -35](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Query Optimization -35.jpg)
>
> Just be careful, you don't want to spend 2 minutes optimizing the query where you only get 1/2 execution where you can make you current 1/2 faster. If that happened, I will probably not spend the 2 minutes and just bite and run 1/2 longer. By nature, query optimizer have to be done very fast. Any exponential number of things is out of the question. But the number of possible tree really grow exponentially. So there's always have to be give and take. Most query optimizer don't give you the optimal global best query. It's just given the limited time we have, look at a bunch of options and let's see who is based on those options who say what is the best. And if we run out of time we can't find a global optimal, so be it. We'll llive that. See the challenge ? 
>
> You don't know the best way to excute a query until you know the result your query.
>
> 只是要注意，你不想花2分钟来优化只能得到1/2执行的查询，而你可以使当前查询更快1/2。如果发生这种情况，我可能不会花2分钟，而是咬着牙跑1/2的时间。本质上，查询优化器必须非常快。任何指数级的东西都是不可能的。但树的数量确实呈指数增长。所以总要有给予和索取。大多数查询优化器不会提供最优的全局最佳查询。这只是给我们有限的时间，看看一堆选项，让我们看看谁是基于这些选项谁说什么是最好的。如果我们没时间了就找不到全局最优解，那就这样吧。我们会活下去的。看到挑战了吗?
>
> 在知道查询结果之前，你不会知道执行查询的最佳方式。





## Generate multiple parse trees ✅

* However, there are multiple options of parse trees 然而，解析树有多种选择

* For relational algebra 用于关系代数
  * Joins are associative 
  
    Join是结合律(associative)
  
  * Selection are commutative 
  
    Selection交换律(commutative)
  
  * Same as projection 
  
    与投影相同
  
  * Also there are some distributive properties 
  
    还有一些分配属性

## Quiz 4

4. Which of the following about the parse tree notation of a query is correct?

   (a) Each node can have at most 2 children

   (b) The leaves corresponds to tables

   (c) For nested loop, the right child is the inner loop.

   A. (b) and (c) 

   B. (a) and (b)

   C. (b)

   D. (a), (b) and (c) ✅



## 16.2 Transformation of Relational Expressions 关系表达式的转换 ✅

> If you see a query, the first thing you should do is to convert it to parse tree or at least one query.
>
> The following always what ? 
>
> Do the join first, then do the selection, then do the projection. This will always be correct, it will give you the correct answer. It may not give you an efficient answer. 
>
> 如果你看到一个查询，你应该做的第一件事是将它转换为解析树或至少一个查询。
>
> 下面总是什么?
>
> 首先进行连接，然后进行选择，然后进行投影。这个总是正确的，它会给你正确的答案。它可能不会给你一个有效的答案。

* Two relational algebra expressions are said to be ==equivalent== if the two expressions generate the same set of tuples on every ==legal== database instance

  如果两个关系表达式在每一个有效数据实例中都会产生相同的元组集, 则称它们是**等价的(equivalent)**

  (一个有效的数据库实例是指满足在数据库模式中指定的所有完整性约束的数据库实例)

  > Can you tell me what is illegal database instance?
  >
  > If two tuples have conflict thing.
  >
  > If illegal Franky, the definition of equivalnet don't care about it. So basically garbage in, garbage out.
  >
  > 你能告诉我什么是非法数据库实例吗?
  >
  > 如果两个元组有冲突。
  >
  > 如果是非法的弗兰克，等价的定义不关心它。所以基本上是垃圾输入，垃圾输出。

  * Note: order of tuples is irrelevant

    注意:元组的顺序无关紧要

  * We don't care if they generate different results on databases that violate integrity constraints 

    我们不关心它们是否在违反完整性约束的数据库上生成了不同的结果

* In SQL, inputs and outputs are multisets of tuples

  在SQL语言中, 输入和输出都是元组的多重集合

  > SQL is not quite relational algebra, the result of sql query it not quite relation. Why not?
  >
  > Duplicate are not removed. So that means what you getting is not necessarily a set. Now the good news is that in real life, this doesn't matter too much. At least in this context.
  >
  > SQL不是完全关系代数，SQL查询的结果也不是完全关系。为什么不呢?
  >
  > 副本不会被移除。这意味着你得到的不一定是一个集合。好消息是，在现实生活中，这并不重要。至少在这种情况下是这样。

  * Two expressions in the multiset version of the relational algebra are said to be equivalent if the two expressions generate the same multiset of tuples on every legal database instance.

    如果关系代数的多重集版本中的两个表达式在每个合法数据库实例上生成相同的元组多重集，则称这两个表达式等价。

* An ==equivalence rule== says that expressions of two forms are equivalent
  
  ==等价规则==表示两种形式的表达式是等价的
  
  * Can replace expression of first form by second, or vice versa
  
    可以用第二种形式代替第一种形式的表达，或者反之, 可以用第一种形式的表达式代替第二种.

> Now once we have this, we want to come up with a set of what we call equivalence.
>
> 一旦我们有了这个，我们想要提出一组我们称之为等价的东西。



### 16.2.1 Equivalence Rules 等价规则 ✅

1. Conductive selection operations can be deconstructed into a sequence of individual selections.

   合取选择运算可分解为单个选择运算的序列. 
   $$
   \sigma_{\theta_1 \wedge \theta_2}(E) \equiv \sigma_{\theta_1}(\sigma_{\theta_2}(E))
   $$

2. Selection operations are commutative.

   选择运算满足交换律(commutative)
   $$
   \sigma_{\theta_1}(\sigma_{\theta_2}(E)) \equiv \sigma_{\theta_2}(\sigma_{\theta_1}(E))
   $$

3. Only the last in a sequence of projection operations is needed, the others can be omitted.

   一系列投医运算中只有最后一个运算是必需的, 其余的可省略.
   $$
   \prod_{L1}(\prod_{L2}(...(\prod_{Ln}(E))...)) \equiv \prod_{L1}(E)
   $$
   Where $L_1 \subseteq L_1 ... \subseteq L_n$

   > $\prod_{name}(\prod_{ssn, name}(Student)) = \prod_{name}(Student)$  This is legal. 
   >
   > $\prod_{name} (\prod_{ssn}(Student))$  This is not.

4. Selections can be combined with Cartesian products and theta joins.

   选择操作可与笛卡尔积以及$\theta$ 连接相结合

   a. $\sigma_{\theta} (E_1 \times E_2) \equiv E_1 \Join_{\theta} E_2$

   b. $\sigma_{\theta_1} (E_1\Join_{\theta_2}E_2) \equiv E_1\Join_{\theta_1 \wedge \theta_2} E_2$

   > If I do a join and then do a selection, I can certainly pull the seleciton as a condition of the Join.
   >
   > 如果我先进行联结，然后再进行选择，我当然可以把选择作为联结的一个条件。

5. Theta-join operations (and natural joins) are commutative.

   $\theta$连接运算满足交换律commutative	
   $$
   E_1 \Join E_2 \equiv E_2 \Join E_1
   $$

6. (a) Theta joins are associative in the following manner:

   自然连接运算满足结合律(associative)
   $$
   (E_1 \Join E_2 ) \Join E_3 \equiv E_1 \Join (E_2 \Join E_3)
   $$
   (b) Theta joins are associative in the following manner:

   $\theta$ 连接具有以下方式的结合律
   $$
   (E_1 \Join_{\theta_1} E_2) \Join_{\theta_2 \wedge \theta_3 } E_3 \equiv E_1 \Join_{\theta_1 \wedge\theta_3}(E_2 \Join_{\theta_2} E_3)
   $$
   ​	  where $\theta_2$ involves attributes from only $E_2$ and $E_3$.
   
   ​	  其中$\theta_2$只包含$E_2$和$E_3$的属性。

> But the key thing is that for correctness, it doesn't matter. The efficiency matters a lot.
>
> That all these doesn't matter, because you will get the correct result. These rules tell you what you can do, whether you want to use this. That's to create optimizesion. 
>
> 但关键是正确性，这无关紧要。效率很重要。
>
> 这些都不重要，因为你会得到正确的结果。这些规则告诉你可以做什么，是否要使用它。那就是创造优化。

7. The operation distributes over the theta join operation under the following two conditions:

   选择运算在下面两个条件下对$\theta$连接运算具有分配律:

   (a) When all the attributes in $\theta_0$ involve only the attributes of one of the expressions ($E_1$) being joined.

   当选择条件$\theta_0$ 中的所有属性只涉及参与连接运算的表达式之一(比如$E_1$)时满足分配律
   $$
   \sigma_{\theta_0}(E_1 \Join_\theta E_2) \equiv (\sigma_{\theta_9}(E_1)) \Join_\theta E_2)
   $$

   > ![IMG_0658](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/IMG_0658.jpg)

   (b) When $\theta_1$ involves only the attributes of $E_1$ and $\theta_2$ involves only the attributes of $E_2$

   当选择条件$\theta_1$ 只涉及$E_1$的属性, 选择条件$\theta_2$ 只涉及$E_2$的属性时, 满足分配律:
   $$
   \sigma_{\theta_1 \wedge \theta_2} (E_1 \Join_\theta E_2) \equiv (\sigma_{\theta_1}(E_1))\Join_\theta(\sigma_{\theta_2}(E_2))
   $$

   > $\sigma_{(a>10) \ and \ (r < 10)} (E_1 \Join_{E_1.b = E_2.q} E_2) \equiv (\sigma_{a>10}(E_1))\Join_{E_1.b =E_2.q}(\sigma_{r < 10}(E_2))$
   >
   > All the things are relatively straightforward.

   > Let's say you have two options. Will you prefer to do the left hand side? Or will you do the right hand side? Then we do the join first or selection first before you do Join?
   >
   > Everything seems to suggest we should do the select before join. 

8. The projection operation distributes over the theta join operation as follows:

   投影运算在下面条件下对$\theta$连接运算具有分配律

   (a) if $\theta$ involes only attributes from $L_1 \cup L_2$:

   连接条件$\theta$ 只涉及 $L_1 \cup L_2$ 中的属性
   $$
   \prod_{L_1 \cup L_2}(E_1 \Join_{\theta} E_2) \equiv \prod_{L_1}(E_1) \Join_\theta \prod_{L_2}(E_2)
   $$

   > However, it is very often that you want a join condition does not contain the attribute that you want to output. Then you just have to be a bit more careful.
   >
   > 但是，您经常希望联结条件不包含要输出的属性。那你就得再小心点。

   (b) In general, consider a join $E_1 \Join_ \theta E_2$

   * Let $L_1$ and $L_2$ be sets of attributes from $E_1$ and $E_2$, respectively.

     令$L_1$、$L_2$分别代表$E_1,E_2$的属性；

   * Let $L_3$ be attributes of $E_1$ that are involved in join condition $\theta $, but are not in $L_1 \cup L_2$ and

     令$E_1$是$E_1$中出现在连接条件$\theta$中, 但不再$L_1 \cup L_2$ 中的属性; 

   * Let $L_4$ be attributes of $E_2$ taht are involved in join condition $\theta $, but are not in $L_1 \cup L_2$.

     令$L_4$是$E_2$中出现在连接条件$\theta$中但不在$L_1 \cup L_2$中的属性

   $$
   \prod_{L_1 \cup L_2}(E_1 \Join_{\theta} E_2) \equiv \prod_{L_1 \cup L_2}(\prod_{L_1 \cup l_3}(E_1) \Join_\theta \prod_{L_2 \cup L_4}(E_2))
   $$

   Similar equivalences hold for outerjoin operations: $ ⟕ , ⟖  \ and \ ⟗$  

   类似的等价关系适用于outerjoin操作: $ ⟕ , ⟖  \ and \ ⟗$  

9. The set operations union and intersection are commutative

   集合的并与交满足交换律
   $$
   E_1 \cup E_2 \equiv E_2 \cup E_1
   $$

   $$
   E_1 \cap E_2 \equiv E_2 \cap E_1
   $$

   (set difference is not commutative)

   集合的差运算不满足交换律

10. Set union and intersection are associative

    集合并union和交intersection是结合律
    $$
    (E_1 \cup E_2)\cup E_3 \equiv E_1 \cup (E_2 \cup E_3)
    $$

    $$
    (E_1 \cap E_2) \cap E_3 \equiv E_1 \cap (E_2 \cap E_3)
    $$

    

11. The selection operation distributes over $\cup, \cap \ and \ -$,

    选择运算对$\cup、\cap和\ -$具有分配律:

    a. 
    $$
    \sigma_\theta (E_1 \cup E_2) \equiv \sigma_\theta(E_1) \cup \sigma_\theta(E_2)
    $$

b. 
$$
\sigma_\theta(E_1 \cap E_2) \equiv \sigma_\theta(E_1) \cap \sigma_\theta(E_2)
$$
c. 
$$
\sigma_\theta(E_1 - E_2) \equiv \sigma_\theta(E_1) -\sigma_\theta(E_2)
$$
d. 
$$
\sigma_\theta(E_1 \cap E_2) \equiv \sigma_\theta(E_1) \cap E_2
$$
e. 
$$
\sigma_\theta(E_1 - E_2) \equiv \sigma_\theta(E_1) - E_2
$$
preceding equivalence does not hold for $\cup$

前面的等价对$\cup$不成立

> Union basically is join. Every attribute has to match, so you can think of intersection as some a kind of a join. Union is some kind of just jump everything together depending on whether the system.
>
> Union基本上就是join。每个属性都必须匹配，所以你可以把交集看作一种联结(join)。工会只是把所有的东西都放在一起取决于系统是否。

> Selection can be push in. 
>
> 选择可以推入

12. The projection operation distributes over union

    投影运算分配到并集上
    $$
    \prod_L(E_1 \cup E_2) \equiv (\prod_L(E_1))\cup(\prod_L(E_2))
    $$

13. Selection distributes over aggregation as below

    选择分布在聚合之上，如下所示
    $$
    \sigma_\theta(_g \gamma_A(E)) \equiv \ _g\gamma_A(\sigma_\theta(E))
    $$
    provided $\theta $ only involves attributes in G

    假设$\theta $只涉及G中的属性

    > $_g\gamma_A$ : group by

14. a. Full outerjoin is commutative:

    Full outerjoin是可交换的:
    $$
    E_1 ⟗ E_2 \equiv E_2 ⟗ E_1
    $$
    b. Left and right outerjoin are not commutative, but:

    左outerjoin和右outerjoin是不可交换的，但是:
    $$
    E_1 ⟕ E_2 \equiv E_2 ⟖ E_1
    $$

15. Selection distributes over left and right outerjoins as below, provided $\theta_1$ only involves attributes of $E_1$

    如果$\theta_1$只涉及$E_1$的属性，则选择分布在左联结和右联结上，如下所示

    a. 
    $$
    \sigma_{\theta_1}(E_1 ⟕_\theta E_2 ) \equiv (\sigma_{\theta_1}(E_1)⟕ _\theta E_2
    $$
    b. 
    $$
    \sigma _{\theta_1}(E_1 ⟖_\theta E_2) \equiv E_2 ⟕_\theta(\sigma_{\theta_1 }(E_1))
    $$

16. Outerjoins can be replaced by inner joins under some conditions

    在某些情况下，outerjoin可以被inner join取代

    a. 
    $$
    \sigma_{\theta_1}(E_1 ⟕_\theta E_2 ) \equiv \sigma_{\theta_1}(E_1 \Join _\theta E_2)
    $$
    b. 
    $$
    \sigma _{\theta_1}(E_1 ⟖_\theta E_2) \equiv \sigma_{\theta_1 }(E_1 \Join _\theta E_2))
    $$
    provided $\theta_1$ is null rejecting on $E_2$

    假设$\theta_1$为null，拒绝$E_2$

> The only thing you want to be careful is for outerjoins
>
> 唯一需要注意的是outerjoin

Note that several equivalences that hold for joins do not hold for outerjoins

请注意，一些对联结有效的等价关系对outerjoin无效

* $\sigma_{year = 2017} (instructor ⟕ teaches ) \not\equiv \sigma_{year=2017}(instructor \Join teaches)$

  > In outer joins, we not just only want to match, but we also need to return tuples that doesn't match.
  >
  > 在外联结中，我们不仅要匹配，还需要返回不匹配的元组。

* Outerjoins are not associative
  
  outerjoin不具有结合性
  $$
  (r⟕s) \Join t \not\equiv r ⟕(s ⟕ t)
  $$
  
  * e.g. with $r(A,B) = \{(1,1)\}, s(B,C) =\{(1,1)\}, t(A,C)=\{\}$



#### Pictorial Depiction of Equivalence Rules 等价表达式的图形化表示

<img src="/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-28 at 18.36.06.png" alt="Screenshot 2022-10-28 at 18.36.06" style="zoom: 25%;" />



### 16.2.2 Example with Multiple Transfromations 转换的例子 ✅

* Query: Find the names of all instructors in the Music department who have taught a course in 2017, along with the titles of the courses that they taught
  
  查询:查找音乐系在2017年教授过一门课程的所有教师的名字，以及他们教授的课程的名称
  $$
  \prod_{name, title}(\sigma_{depar\_name = 'music' \wedge year=2017}(instructors\Join (teaches\Join\prod_{course\_id,title}(course))))
  $$
  
* Transformation using join associatively (Rule 6a):
  
  使用关联连接进行转换(规则6a):
  $$
  \prod_{name, title}(\sigma_{depar\_name = 'music' \wedge year=2017}((instructors\Join teaches)\Join\prod_{course\_id,title}(course)))
  $$
  
* Second form provides an opportunity to apply the "perform selections early" rule, resulting in the subexpression
  
  $$
  \sigma_{depar\_name = 'music' }(instructors)\Join \sigma_{year=2017}(teaches)
  $$
  
  第二种形式提供了应用“尽早执行选择”规则的机会，从而产生子表达式 

> Once again, this is probably the earliest technique that could be optimized if to reorganize. The theory is to push the operation in and out. And for example, intuitively, it seems as a good idea to do the selection first before you do the join. And you might even argue that you'd better do the projection before you do the Join. So these are all a set of what we call risk kind of rules. Nothing has been proven, but it could be seems to work well. So we'll basically rewrite the query based on those intuition.
>
> 同样，这可能是重组时可以优化的最早的技术。理论上是把操作推入推出。例如，直观地说，在进行联结操作之前先进行选择似乎是个好主意。你可能会说，最好先做投影再做联结运算。这些都是我们所说的风险规则。没有任何东西被证实，但它似乎可以很好地工作。所以我们基本上会根据这些直觉重写查询。

 ![Screenshot 2022-10-28 at 23.53.39](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-28 at 23.53.39.png)

> At the very least, we should this transformation need to be done at the very least to produce options we want to accept. So typically what happens is that your algorithm, all your your create your query optimizer.
>
> And the idea is that once you have this tree, then you can do all the transformation and then create extra trees, then the optimizer will then go to work and estimate the cost of how much is needed to execute each of these tree. And execute in time for each of these tree and then figure which trees to best.
>
> In the early system like in the 80s, It will basically say, Hey, eve do this transformation, do this transformation to this transformation but don't do those transformation and just do the transformation and give you a final tree and run it. So it can be using both way. You can use a way to decide how do you want to query? If not, at least we can be a tool for you to generate other options and then you decide which option to do. So there's at least two things you can look at. 
>
> 至少，我们应该完成这种转换，至少产生我们想要接受的选项。通常情况下，你的算法，你创建你的查询优化器。
>
> 这个想法是，一旦你有了这棵树，你就可以进行所有的转换然后创建额外的树，然后优化器就会开始工作并估计执行每棵树需要多少成本。并对每棵树进行及时执行，然后找出最适合的树。
>
> 在早期的系统中，比如80年代，它基本上会说，嘿，伊芙做这个转换，做这个转换到这个转换但不要做那些转换，只做转换然后给你一个最终的树，然后运行它。这两种方法都可以用。你可以使用一种方法来决定你想要如何查询?如果没有，至少我们可以成为您生成其他选项的工具，然后您决定做哪个选项。所以你至少可以看两件事。



### Transformation Example: Pushing Projections

* Consider: 
  $$
  \prod_{name, title}((\sigma_{depar\_name = 'music'}(instructor)\Join teaches)\Join\prod_{course\_id,title}(course))))
  $$
  
* When we compute
  $$
  (\sigma_{dept\_name ='Music'} (instructor \Join teaches)
  $$
  we obtain a relation whose schema is: `ID, name, dept_name, salary, course_id, sec_id, semester, year`

  > How will you describe a attribute that is necessary or is not necessary in this case?
  >
  > Name and title is necessary because you need it at the very end. 
  >
  > what actually were needed, and what could be useless? And if you know that distinction, then you can push the projection down as long as you need.

* Push projections using equivalence rules 8a and 8b; eliminate unneeded attributes from intermediate results to get:
  $$
  \prod_{name, title}((\prod_{name,course\_id}((\sigma_{depar\_name = 'music'}(instructor))\Join teaches))\Join\prod_{course\_id,title}(course))
  $$

* Performing the projection as early as possible reduces the size of the relation to be joined.

> P754

> if you do projection, your table becomes smaller. And hopefully that will make Join faster to compute.

> Now the good news about sql is what you by default, you do or do not remove the duplicates. You don't have to  do any check. It's just linearly reading the table.



### 16.2.3 Join Ordering Example ✅

* For all relations $r_1, r_2$ and $r_3$,
  
  对于所有关系$r_1, r_2$和$r_3$，
  $$
  (r_1 \Join r_2) \Join r_3 = r_1 \Join (r_2\Join r_3)
  $$
   (Join Associativity) $\Join$
  
* If $r_2 \Join r_3$ is quite large and $r_1 \Join r_2 $ is small, we choose
  
  如果$r_2 \Join r_3$很大，而$r_1 \Join r_2 $很小，则选择
  $$
  (r_1 \Join r_2) \Join r_3
  $$
  so that we compute and store a smaller temporary relation.

>  The most challenging thing on a query optimizer is to figure out which join to do first and also figure out which going to do first have a drastic impact on the possible speed of the query.
>
>  So once again you have to estimate the result of join. You don't know the result that John is executed, you don't know how many tuples will return when you execute it. but you really need to know how many tuples you're going to get before you choose how to execute. Let's get back to the chicken and egg problem. It's always a chicken and egg problem.
>
>  对于查询优化器来说，最具挑战性的事情就是要弄清楚哪个连接应该先执行，以及哪个连接会对可能的查询速度产生重大影响。
>
>  同样，你需要估计join的结果。你不知道John执行的结果，也不知道执行它会返回多少元组。但在选择如何执行之前，你真的需要知道你将得到多少元组。让我们回到鸡和蛋的问题。这总是一个先有鸡还是先有蛋的问题。



* Consider the expression 
  $$
  \prod_{name, title}((\sigma_{depar\_name = 'music'}(instructor)\Join teaches)\Join\prod_{course\_id,title}(course))))
  $$

* Could compute $teaches\Join\prod_{course\_id,title}(course)$ first, and join result with $\sigma_{depar\_name = 'music'}(instructor)$. But the result of the first join is likely to be a large relation

* Only a small fraction of the university's instructors are likely to be from the Music department

  * It is better to compute
    $$
    \sigma_{depar\_name = 'music'}(instructors)\Join teaches
    $$
    First.

> obviously, this is a human decision, I want to at least give you start to make some human decisions so that you can think about how do we incorporate this human decision into a database application.
>
> 显然，这是人类的决定，我想至少让你们开始做一些人类的决定这样你们可以考虑如何将人类的决定合并到数据库应用程序中。





### 16.2.4 Enumeration of Equivalent Expressions ✅

* Query optimizers use equivalence rules to **==systematically==** generate expressions equivalent to the given expression

  查询优化器使用等价规则来**==系统地==**生成与给定表达式等价的表达式

* Can generate all equivalent expressions as follows:

  可以生成所有等价的表达式:

  * Repeat

    重复
    
    * apply all applicable equivalence rules on every subexpression of every equivalent expression found so far
    
      对目前找到的每个等价表达式的每个子表达式应用所有适用的等价规则
    
    * add newly generated expressions to the set of equivalent expressions
    
      将新生成的表达式添加到等价表达式的集合中
    
    Until no new equivalent expressions are generated above
    
    除非上面没有生成新的等价表达式

* The above approach is very expensive in space and time

  上述方法在空间和时间上都是非常昂贵的
  
  * Two approaches
    
    两种方法
    
    * Optimized plan generation based on transformation rules
    
      基于转换规则的优化规划生成
    
    * Special case approach for queries with only selections, projections and joins
    
      仅支持选择、投影和连接的特殊查询方法



> I started out with a basic query, always to join first and selection the projection. And then they will apply a set of rules and then it will convert those query into a different query and then run it. Nowadays we still do this, but now the goal is different. The goal is to produce a variety of possible way of executing the query and then figure out which way. And then we push it to the next step. The next step would that evaluate each of this query and see which one is the best? That's why. Query optimizers use equivalence rules to **==systematically==** generate expressions equivalent to the given expression 
>
> 我从一个基本的查询开始，总是先连接，然后选择投影。然后他们会应用一组规则，然后它会将这些查询转换为不同的查询，然后运行它。现在我们仍然这样做，但现在的目标不同了。目标是产生执行查询的各种可能方法，然后找出哪种方法。然后我们把它推到下一步。下一步是对每个查询进行评估，看看哪个是最好的?这就是为什么。查询优化器使用等价规则来**==系统地==**生成与给定表达式等价的表达式

> In general, you will actually generate several possibilities based on the given. I'm not going to all possibilities. I'm only going to generate some possibilities based on how we can optimize.
>
> 一般来说，你实际上会根据给定的情况生成几种可能性。我不会考虑所有的可能性。我只会根据我们如何优化来产生一些可能性。



## Implementing Transformation Based Optimization ✅

* Space requirements reduced by sharing common subexpressions:

  通过共享公共子表达式减少空间需求:

  * When $E_1$ is generated from $E_2$ by an equivalence rule, usually only the top level of the two are different, subtrees below are the same and can be shared using pointers

    当$E_1$通过等价规则由$E_2$生成时，通常只有两者的顶层是不同的，下面的子树是相同的，可以使用指针共享

    * E.g. when applying join commutativity

      例如，当应用连接交换性时
      
      <img src="/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-29 at 02.17.51.png" alt="Screenshot 2022-10-29 at 02.17.51" style="zoom: 50%;" />

  * Same sub-expression may get generated multiple times

    相同的子表达式可能会被生成多次
    
    * Delect duplicate sub-expressions and share one copy
    
      删除重复的子表达式并共享一个副本

* Time requirements are reduced by not generating all expressions

  不生成所有表达式可以减少时间需求
  
  * Dynamic programming is an option
  
    动态规划是一个选择



> When we cover about generation, we talk about basically starting with a tree and generating as many as possible. It turns out there is some merit of doing things bottom up. Now, when I say bottom up, what do you think I mean here? Starting from leaves. 
>
> 当我们谈到生成时，我们基本上是从一棵树开始，生成尽可能多的树。事实证明，自下而上做事是有一定价值的。现在，当我说自下而上时，你认为我在这里是什么意思?从叶子开始。
>
> ![IMG_0659](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/IMG_0659.jpg)
>
> The idea here, if you want to have the self beginning of big picture, we want to build things from below. Even though we may have a lot of expression, many of them are really similar now. What do I mean?
>
> 这里的想法是，如果你想要有一个大的图片的自我开始，我们想要从下面开始构建东西。尽管我们可能有很多表达方式，但其中许多都非常相似。我是什么意思?
>
> ![IMG_0660](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/IMG_0660.jpg)



## Decorating parse trees 装饰解析树 ✅

* **==Once the parse trees are build, need to decorate them with algorithm for each step==**

  一旦构建了解析树，需要为每个步骤使用算法装饰它们

* Start with looking at the possible algorithms for each operators

  从每个操作符可能的算法开始

* Other consideration
  
  其他注意事项
  
  * Materializaiton vs. Pipelining
  
    物化与流水线
  
  * Combining operators.
  
    组合运算符

> So far we talk about all the transformation. And the goal of the transformation is to generate a bunch of potential path tree. so that we can choose which one is the fastest. Once we have a parse tree, then what we need to do next is what we called that create in the parse tree. So if there's a joint, we need to figure out whether we want to do like sort merge, nested loop. If you are selection. We do figure out whether we should use an index. If so, which index to use and which algorithm which we want to run. If we do projection, we want to know whether do we need to sort anything beforehand, so and so forth. That's so far what we talk about. It turns out there is one more thing we need to consider, and it's the notion of what we call materialization and pipelining.
>
> 到目前为止，我们讨论了所有的变换。转换的目的是生成一堆潜在的路径树。这样我们就可以选择哪个是最快的。一旦我们有了解析树，接下来我们需要做的就是在解析树中创建。如果有一个关节，我们需要确定是否要进行排序合并，嵌套循环。如果你是选择。我们确定了是否应该使用索引。如果是，则使用哪个索引以及要运行哪个算法。如果我们进行投影，我们想知道是否需要事先对任何东西进行排序，等等。这就是我们目前讨论的内容。事实证明，我们还需要考虑一件事，那就是我们所谓的物化和流水线的概念。



> We have a lot of clothes. And you only have one washer and one drier. What do you do? You probably put the first load in the washer, wash it, put the first thing in the dryer, dry it forward, and then put the second load in the washer, wash it. Then they put a second low in the dryer, dry it ... You don't have to wait for the first load to finish drying before you put the second low in the washer. This is a very, very basic form of pipeline. what do I mean by that? You have to clean your clothes. You have to do two operations, right? You have to wash it and then dry it. Each of them is independent of one another. And when you're done trying, you don't go back and watch it. So what does it mean? That means I can't. When I send the first load to wash after the first load is done washing, I immediately send the first load to dry. But the watcher at that time is free. I can actually send a second load to wash. That's what pipelining. You can actually be more efficient. Why do I talk about all this in this database? 
>
> 我们有很多衣服。你只有一台洗衣机和一台烘干机。你是做什么的? 你可能会把第一件东西放在洗衣机里洗，然后把第一件东西放在烘干机里，向前烘干，然后把第二件东西放在洗衣机里洗。然后他们在烘干机里放了第二个低气压，把它烘干…你不必等到第一件衣服晾干后再把第二件衣服放进洗衣机。这是一种非常基本的管道形式。这是什么意思呢?你必须洗你的衣服。你需要做两个操作，对吧?你得先洗，再擦干。每一个都是相互独立的。当你试完了，你就不会再回头看了。那么这是什么意思呢?这意味着我不能。当我送第一批货去洗时，第一批货洗完后，我立即送第一批货去干。但是那个时候的观察者是自由的。我可以再送一批去洗。这就是管道。实际上你可以更有效率。为什么我要在这个数据库中谈论这些?
>
> I'm going to read only a portion of the table. we can pick out a loop and then we wrap that in the loop and we can't just we might not be enough to read in the loop in one shot. We divide it in a bunch of shots. So every time the buffer is full, we are going to join. We are doing the match tuples. And the idea is what once the tuple is match, we can immediately go to do selection on them. We don't have to write the temporary result into the this and then bring it back in to select.
>
> 我只看表格的一部分。我们可以选择一个循环然后把它包装在循环中但是我们不能我们可能不够一次读取循环。我们把它分成一堆镜头。所以每次缓冲区满了，我们就进行join操作。我们正在进行匹配元组。这个想法是，一旦元组匹配，我们可以立即对它们进行选择。我们不需要把临时结果写进this然后再把它带回来选择。![Chp16 Query Optimization -5](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Chp16 Query Optimization -5.jpg)
>
> ![IMG_0661](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/IMG_0661.jpg)
>
> ![Chp16 Query Optimization -7](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Chp16 Query Optimization -7.jpg)



## 15.7 Materialization vs. Pipelining 物化 vs 流水线 ✅

考虑如何计算包含多个运算的表达式. 一种显而易见的方法是以适当的顺序每次执行一个操作; 每次计算的结果被**物化(materialized)** 到一个临时关系中以备后用. 这一方法的缺点是需要构造临时关系, 这些临时关系必须写到磁盘上(除非很小). 另一种方法是在**流水线(pipeline)**上同时计算多个运算, 一个运算的结果传递给下一个, 而不必保存临时关系.

* Consider the following query 考虑下面的查询
  $$
  \sigma_{gpa>3.0}(Student \Join Department)
  $$

* We can push selection in 我们可以将selection推入
  $$
  \sigma_{gpa>3.0} (Student) \Join Department
  $$

  > Now obviously based on the discussion of earlier, we can push the selection down, we can do the selection, then we do the nested loop. 
  >
  > 显然，根据之前的讨论，我们可以把选区往下推，我们可以做选区，然后做嵌套循环。
  
* suppose we use nested loop  假设我们使用嵌套循环

  * Either table can be in the inner loop
  
    任何一个表都可以在内部循环中



$$
\sigma_{gpa > 3.0}(Student)\Join Department
$$

* Now suppose Student is in the inner loop 现在假设Student在内部循环中

  > That means that every time you read a page in the department table, I have to read the whole result inner loop. 
  >
  > 这意味着每次读取department表中的一页时，都必须读取整个result内循环。

* We first apply the selection: $\sigma_{gpa>3.0}(Student)$ 

  我们首先应用选择: $\sigma_{gpa>3.0}(Student)$ 

* **However, since that is in the inner loop, it will have to be read ==multiple times==**

  **但是，由于它位于内循环中，因此必须读取==多次==**

* **So the result of the selection need to be writing to secondary storage -- ==materialization==**

  **因此，选择的结果需要写入辅助存储——==物化==**
  
  > So the result of $\sigma_{gpa>3.0}(Student)$ you actually have to store in the disk because you have to read it multiple time.
  >
  > 因此，$\sigma_{gpa>3.0}(Student)$ 的结果实际上必须存储在磁盘中，因为您必须多次读取它。
  >
  > | Department | $\sigma_{gpa>3.0}(Student)$ |
  > | ---------- | --------------------------- |
  >
  > Department is outer loop, Selection of student is in inner loop. So you read a few page of department. Then you have to read the whole table of $\sigma_{gpa>3.0}(Student)$, and join. And then you read the second page of department. Once again, I have to read the whole result to continue the join process. 
  >
  > 部门是外循环，学生的选拔是内循环。你读了几页部门然后你必须读取$\sigma_{gpa>3.0}(Student)$的整个表，并进行join操作。然后你读第二页的部门。再次，我必须读取整个结果才能继续join过程。
  
  > materialization that means the result of the first query have to materialize. Have you have to actually store the result onto the this that's what we call materialization.
  >
  > 物化意味着第一个查询的结果必须物化。你必须把结果存储到。这就是我们所说的物化。

 **The inner loop of a nested loop join need to be materialized!**

> But if a stuent is in the outer loop, what happened?

$$
\sigma_{gpa > 3.0}(Student)\Join Department
$$

* Now suppose Student is in the outer loop 现在假设Student在外层循环中

* We first apply the $\sigma_{gpa > 3.0}(Student)$

  我们首先应用 $\sigma_{gpa > 3.0}(Student)$

* However, since that is in the outer loop, it will have to be read only once 

  但是，由于它在外层循环中，因此只需要读取一次

* So we can apply the following algorithm

  所以我们可以应用以下算法

  * Allocate some amount of main memory buffers for the result of the selection (the amount one allocate for the outer loop of the join) 

    为选择的结果分配一些主内存缓冲区 (为连接的外循环分配的数量)

  * Start executing the selection 开始执行选区

  * Pause when the buffer is filled up

    当缓冲区填满时暂停

  * Then execute the join for those tuples in the buffers only

    然后仅对缓冲区中的元组执行关联操作

    * **Notice that involve reading the inner loop (Department) once 注意这里只需要读取一次内部循环(Department)**

  * After that is done, those tuples in the buffer from teh selection **==is no longer needed==** (why?)

    在这之后，来自选择的缓冲区中的那些元组**不再需要**(为什么?)

    > Because these is in the outer loop. So we can discard though to resume the selection until the buffer is spill.
    >
    > 因为这些都在外层循环中。所以我们可以丢弃，恢复选择，直到缓冲区溢出。

  * Discard those tuples, resume the selection until the buffer is filled

    丢弃这些元组，恢复选择，直到缓冲区被填满

  * Repeat the process 重复这个过程

* This is known as ==**pipelining**== 这被称为==**流水线**==

> | $\sigma_{gpa>3.0}(Student)$ | Department |
> | --------------------------- | ---------- |
>
> The selection  of student and then you read the whole department table, which is already in the stores anyway. You don't do anything with it. You might have to read department multiple times because we don't have enough buffer. But the point is, once I read the department table and to join this, I can discard these tuples. Those tuples will never be needed again. At least in the content in this join.
>
> 选择学生，然后读取整个部门表，这已经在商店里了。你不用它做任何事情。由于我们没有足够的缓冲区，您可能需要多次读取department。但关键是，一旦我读取了department表并加入它，我就可以丢弃这些元组。这些元组将永远不再需要。至少在联结的内容中是这样。

> ![Chp16 Query Optimization -8](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Chp16 Query Optimization -8.jpg)





## 15.7.1 Materialization 物化 ✅

* Materialized evaluation is always applicable 

  物化评估总是适用的

* Cost of waiting results to disk and reading them back can be quite high

  等待结果到磁盘并将其读取回来的成本可能非常高

  * Our cost formulas for operations ignore cost of writing results to disk, so
    
    我们的操作开销公式忽略了将结果写入磁盘的开销，因此
    
    * Overall cost = Sum of costs of individual operations + cost of writing intermediate results to disk
    
      总成本=单个操作的成本之和+将中间结果写入磁盘的成本

* **==Double buffering==**: use two output buffers for each operation, when one is full write it to disk while the other is getting filled 

  **==双缓冲==**:每个操作使用两个输出缓冲区，当一个缓冲区满时将其写入磁盘，而另一个正在被填满

  * Allows overlap of disk writes with computation and reduces execution time
  
    允许磁盘写入与计算重叠，并减少执行时间
  
  > One buffer doing the printing, the other buffer return receiving the result of caculation, because the caculation is faster than anything 
  >
  > But nowdays, it's triple, quadruple, quintuple buffer because the CPU becomes so fast. You can insert having one output buffer, you can have multiple output offers while one buffer is actually writing the output, the other is actually receiving the result. 
  >
  > 一个缓冲区打印，另一个缓冲区返回接收计算结果，因为计算比任何东西都快
  >
  > 但现在，它有三倍，四倍，五倍的缓冲因为CPU变得非常快。你可以插入一个输出缓冲区，你可以有多个输出提供，一个缓冲区实际上是写入输出，另一个实际上是接收结果。





## 15.7.2 Pipelining 流水线 ✅

* **==Pipelined evaluation==**: evaluate several operations simultaneously, passing the results of one operation on to the next.

  **==流水线计算==**:同时计算多个操作，将一个操作的结果传递给下一个操作。

  E.g., In previous expression tree, don't store result of 

  例如，在前面的表达式树中，不要存储的result
  $$
  \sigma_{building='Watson‘} (department)
  $$

  * Instead, pass tuples directly to the join... Similarly, don't strore result of join, pass tuples directly to projection

    相反，直接将元组传递给join…类似地，不要存储join的结果，直接将元组传递给投影

  > Notice that in pipeline we do not wait till the first operating to finish before we start the second. That's where you save the time.
  >
  > 请注意，在pipeline中，我们不会等到第一个操作完成后才开始第二个操作。这就是节省时间的地方

* Much cheaper than materialization: no need to strore a temporary relation to disk.

  比物化便宜得多:不需要存储临时关系到磁盘

* Pipelining may not always be possible - e.g., sort, hash-join.

  流水线可能并不总是可行的——例如，排序、散列连接。

  * **Key observation: pipelining is possible if and only if the data that is pipelined into the next operations is read only once for that operation**

    **关键:当且仅当管道中进入下一个操作的数据对于下一个操作只读取一次时，管道才可能实现**

    > ![Screenshot 2022-10-29 at 20.44.48](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-29 at 20.44.48.png)
    
    > Sort-merge:  You have to wait till the two tables to be sorted before you can merge. So there's no pipeline you can play.
    >
    > Sort-merge:必须等到两张表排序完成后才能进行合并。所以没有管道可以玩`
    
    > **==The inner loop of a nested loop join need to be materialized==** (上图很重要!)

* For pipelining to be effective, use evaluation algorithms that generate output tuples even as tuples are received for inputs to the operation.

  为了使管道有效，使用即使在接收到元组作为操作输入时也生成输出元组的求值算法。

* Pipelines can be executed in two ways: ==**demand driven**== and **==producer driven.==**

  流水线可以以两种方式执行:==**需求驱动**==和==**生产者驱动**==

> And as I say now, in this class we are focused on I/O, we don't talk much about CPU at all. But obviously if you have multiple CPU, you can see that you can gain a lot from doing that.
>
> 就像我说的，在这门课上，我们关注的是I/O，我们不会过多讨论CPU。但很明显，如果你有多个CPU，你可以看到你可以从中获得很多。

> ![Chp16 Query Optimization -9](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Chp16 Query Optimization -9.jpg)





* In **==demand driven==** or **==lazy==** evaluation
  
  需求驱动的或懒评估
  
  * System repeatedly requests next tuple from top level operation
  
    系统重复从顶级操作请求下一个元组
  
  * Each operation requests next tuple from children operations as required, in order to output its next tuple
  
    每个操作根据需要从子操作请求下一个元组，以便输出其下一个元组
  
  * In between calls, operation has to maintain "**==state==**" so it knows what to return next
  
    在调用之间，操作必须保持“**==state==**”(状态)，这样它就知道接下来要返回什么
  
* In **==producer-driven==** or **==eager==** pipelining
  
  在生产者驱动或流水线
  
  * Operators produce tuples eagerly and pass them up to their parents
    
    操作符立即生成元组并将它们传递给它们的父级
    
    * Buffer maintained between operators, child puts tuples in buffer, parent removes tuples from buffer
    
      在操作符之间维护缓冲区，子操作符将元组放在缓冲区中，父操作符从缓冲区中删除元组
    
    * if buffer is full, child waits till there is space in the buffer, and then generates more tuples
    
      如果缓冲区已满，child会等待直到缓冲区有空间，然后生成更多的元组
    
  * System schedules operations that have space in output buffer and can process more input tuples
  
    系统调度在输出缓冲区中有空间的操作，并可以处理更多的输入元组
  
* Alternative name: **==pull==** and **==push==** models of pipelining

  替代名称:**==pull==**和**==push==**管道模型

> ![IMG_0666](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/IMG_0666.jpg)

>So there are two ways of doing it. if you are actually implementing, say, the next version of Oracle, you do have to worry about this because the different mechanism, they will be slightly different. Your overall architecture might be a bit different because now you have to say, who is the boss who called the shots that do affect how the database system is implemented? For the sake of this class, it doesn't really matter too much because all we case how many of these pages are we going to read? So in that sense, push and pull doesn't really matter too much. However, if you are the one to actually implement things, you do have to worry about, which is the better way. Once again, there's no definite answer. 
>
>有两种方法。如果你正在实现Oracle的下一个版本，你就不得不担心这一点，因为不同的机制，它们会略有不同。您的整体架构可能有点不同，因为现在您必须说，谁是影响数据库系统实现的发号施令的老板?对于这门课来说，这并不重要，因为我们要看多少页呢?所以从这个意义上说，推和拉并不重要。然而，如果你是真正实现事情的人，你就不得不担心哪种方式更好。同样，没有明确的答案。



* Implementation of demand-driven pipelining

  实现需求驱动的流水线

  * Each operation is implemented as an ==**iterator**== implementing the following operations

    每个操作都被实现为==**迭代器**==实现以下操作

    * `open()`
  
      > You basically just start an operator 你只需要启动一个操作符
    
      * E.g., file scan: initialize file scan 
        
        例如，file scan:初始化文件扫描
        
        * state: ponter to beginning of file
        
          状态:跳转到文件开头
        
      * E.g., merge join: sort relations;
        
        例如，合并连接:对关系进行排序
        
        * state: pointers to beginning of sorted relations
        
          状态:指向排序关系开始的指针
    
    * `next()`
    
      > Then you need to fetch for the next tuples. It may be the next tuple you just doing a scan. If your operator is a Join and nested give me the next result. 
      >
      > 然后你需要获取下一个元组。它可能是你正在扫描的下一个元组。如果你的操作符是一个Join并且嵌套，给我下一个结果。
    
      * E.g., for file scan: Output next tuple, and advance and store file pointer
    
        用于文件扫描:输出下一个元组，以及前进和存储文件指针
    
      * E.g., for merge join: continue with merge from earlier state till next output tuple is found. Save pointers as iterator state.
    
        对于合并连接:从前面的状态继续合并，直到找到下一个输出元组。将指针保存为迭代器状态
    
    * `close()`
    
      > Because when I open, I have to allocate some buffers. In main memory, so I better be a nice boy and clean it up. Otherwise, running our buffer very soon.
      >
      > 因为当我打开时，我必须分配一些缓冲区。在主内存里，所以我最好乖乖把它清理干净。否则，很快就会运行我们的缓冲区。

> So once again, this is going very deep into implementation issues.So I don't want I don't want to go too much. But the iterator structure, the architecture will allow you to do these things. You really should think in terms of these things. If you operate each operation like a join, a selection, a projection should come when you implement this function, you should have a say, a open function. That means you start the reading the file.  Then you should have a next operation that returns the next tuples.
>
> 因此，这再次深入到实现问题。所以我不想我不想去太多。但是迭代器结构，架构会允许你做这些事情。你真的应该从这些方面考虑。如果每个操作都像联结、选择、投影一样，那么当你实现这个函数时，你应该有一个open函数。这意味着你开始读取文件。然后你应该有一个返回下一个元组的next操作。

> What is iteration in Java?  
>
> https://www.runoob.com/java/java-iterator.html
>
> Why do Java create iterator?
>
> 在程序开发中，经常需要遍历集合中的所有元素
>
> What iterator provide you ?
>
> A: You can call for next. And then so on so forth.

> So a pipeline can also be thinking of as a iterator in the most generic sense. If you do a pipelining operation, each operation should be a thing of an iterator.
>
> 因此，流水线也可以被认为是最一般意义上的迭代器。如果要进行管道操作，则每个操作都应该是迭代器的一部分。

> Java garbage collection?
>
> Basically where you left the things behind, mom come out and clean up, this garbage collection. Somebody have to Garbage collection. It's not you, then it's actually your mother.
>
> 基本上就是你放东西的地方，妈妈出来打扫，这个垃圾收集。总得有人做垃圾收集。不是你，而是你妈妈。

使用生产者驱动的流水线方法可以被看作将数据从一棵操作树的底层推(push)上去的过程；而使用需求驱动的流水线方法可被看成是从树顶将数据拉(pull)上来的过程。在生产者驱动的流水线中， 元组的产生是积极的，而在需求驱动的流水线中，元组消极地(lazily）按需求产生。需求驱动的流水线比生产者驱动的流水线应用得更为普遍，因为它更容易实现。但是，生产者驱动的流水线在并行处理系统中非常有用.



#### 15.7.2.2 Blocking Operations ✅

有些操作例如排序, 其本质上是阻塞操作(blocking operation), 也就是说, 它们可能不能输出任何结果, 直到所有的输入元组被检查为止.

* **==Blocking operations==**: cannot generate any output until all input is consumed
  
  阻塞操作:在所有输入被消耗之前不能生成任何输出
  
  * E.g., sorting, aggregation, ...
  
    例如，排序、聚合……
  
* But can often consume inputs from a pipeline, or produce outputs to a pipeline

  但通常可以使用管道的输入，或者产生管道的输出

* Key idea: blocking operations often have two suboperations
  
  关键思想: 阻塞操作通常有两个子操作
  
  * E.g, for sort: run generation (during sort) and merge
  
    例如，对于排序:运行生成(在排序期间)和合并
  
  * For hash join: partitioning and build-probe(during the final nested loop)
  
    用于散列连接:分区和构建-探测(在最后的嵌套循环期间)
  
* Treat them as separate operations

  将它们视为单独的操作

![Screenshot 2022-10-29 at 23.38.47](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-29 at 23.38.47.png)

> Let's go to the merge sort as a further explanation. So what do you mean by blocking operation? Let's say I do a join. If you just take a look on the surface, you really can't do anything until the whole thing is sorted.
>
> Remeber how merge sort work?
>
> Initially you create a sort of segment, and then you merge. Smallest to a bigger list. You continue to merge bigger list to even bigger lists. You continue do that until the number of segments is less than the number of buffers. Then you can emerge temple. Now, even though the whole operation does not allow you to pipeline because obviously these result in the middle have to be written to do this. There's no way for you to get around that.
>
> 下面进一步解释归并排序。那么阻塞操作是什么意思呢?假设我做了一个join。如果你只看表面，你真的不能做任何事情，直到整个事情被排序。
>
> 还记得归并排序的工作原理吗?
>
> 一开始你创建一个段，然后合并。从最小到更大的列表。不断地将更大的列表合并为更大的列表。你可以继续这样做，直到段的数量小于缓冲区的数量。然后你就可以出来了。现在，即使整个操作不允许你进行流水线操作，因为很明显，这些中间的结果必须被写入。你没办法回避这个问题。
>
> ![Chp16 Query Optimization -11](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Chp16 Query Optimization -11.jpg)
>
> So sometimes even though an operation on surface cannot be pipeline, it is certainly possible part of it could be pipeline. And that allow you to have a kind of what we call a blocking operation.
>
> 所以有时即使一个表面上的操作不能是流水线，但它肯定有一部分可能是流水线。这允许你有一种我们所说的阻塞操作。



* Pipeline stages:

  * All operations in a stage run concurrently
  
    一个阶段中的所有操作同时运行
  
  * A stage can start only after preceding stages have completed execution
  
    一个阶段只有在前几个阶段执行完成后才能开始
  
  ![Screenshot 2022-10-29 at 23.38.47](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-29 at 23.38.47.png)
  
  







## Materialization vs. Pipelining: Cost estimation ✅

$$
\sigma_{gpa>3.0}(Student) \Join Department
$$

* Suppose

  * 1000 pages for Department

  * 5000 pages for Student

  * $\sigma_{gpa>3.0}(Student)$ return 2500 pages

    > In this case, we have to do this selection, so we have to write the result

  * Suppose 100 buffers, split 50 each

* Consider Student in the inner loop (no pipeline)
  $$
  Cost (page \ read) = 5000 (read\  Student \ for \ \sigma) \\+ 2500 (write \ Student\ for \ \sigma  ) \\+ 1000 (outer\  loop \ for \ Department) \\+ 2500 \times \frac{1000}{50} (inner \ loop \ for \ \sigma_{gpa>3.0}(Student))\\ = 58500
  $$

  > So let's say we do it on a solid state drive. So no seek.

 

> If student is outer loop


$$
\sigma_{gpa>3.0}(Student) \Join Department
$$


* Suppose

  * 1000 pages for Department
  * 5000 pages for Student
  * $\sigma_{gpa>3.0}(Student)$ return 2500 pages
  * Suppose 100 buffers, split 50 each

* Consider Student in the outer loop (no pipeline)
  $$
  Cost (page \ read) = 5000 (read\  Student \ for \ \sigma, outerloop) \\+ 1000 \times \frac{2500}{50} (inner \ loop \ for \ Department)\\ = 55000
  $$

> So the total cost is now a little bit smaller, not a lot. But still, if every microseconds count, this is something to think about.  in this case, I'm violating my own rule to put the larger table in the outer loop. But we can do that because pipelines basically eliminate the costs of leading to the end of outer loop once again, because you pay that price when you do the initial reading. It may be worthy to put a larger table in the outer loop in this case. Once again, that's what make career optimization complicated and fascinating. There is a lot of things to consider.
>
> 总成本变小了，不是很多。但是，如果每一微秒都算数的话，这是值得考虑的。在这种情况下，我违反了我自己的规则，将更大的表放在外循环中。但我们可以这样做，因为管道基本上消除了再次进入外循环结束的成本，因为在进行初始读取时需要支付该成本。在这种情况下，在外层循环中放置一个更大的表可能是值得的。再一次，这就是职业优化的复杂和迷人之处。有很多事情要考虑。

> Why do we need to write to the department?
>
> A: Because I haven't touched the department. They define this already in the database. I didn't do anything. I just simply have to read the whole table. I don't do any selection. I didn't find any result.
>
> 为什么我们要给部门写信?
>
> A:因为我还没动过这个部门。他们已经在数据库中定义了这个。我什么都没做。我只需要读整张表。我不做任何选择。我没有发现任何结果。



> If it is hard drive, we have to worry about these things. Things can get dicier. But it is at least something you should actually consider, or at least a career optimizer absolutely should consider. And if you are building a database system, it is actually something that you have to do architecture. Once again, I'm talking about it in the context of database. There might be some other system that you build, even though it's not a full fledged database, have some of these capability. So keep that in mind. You might use it in some other context when you're developing something itself.
>
> 如果是硬盘，我们就得担心这些东西。事情可能会变得更冒险。但这至少是你应该考虑的事情，或者至少是职业优化者绝对应该考虑的事情。如果你要建立一个数据库系统，这实际上是你必须要做的架构。再说一次，我是在数据库的上下文中讨论它的。也许你构建的其他一些系统，即使它不是一个成熟的数据库，也具有其中的一些功能。记住这一点。当你自己开发某些东西时，你可能会在其他语境中使用它。





## Index-only query ✅

* Consider:
  $$
  \sigma_{gpa>3.0}(Student)
  $$

* Now suppose we have a secondary index on gpa 

  现在假设我们对gpa有一个二级索引

  * Probably not useful if a lot of tuples satisfies the query 

    如果有很多元组满足查询，可能就没什么用了

* However, consider
  $$
  \pi_{gpa} (\sigma_{gpa>3.0}(Student))
  $$

  * Now only the gpa attribute is needed

    现在只需要gpa属性

  * All the information needed is in the secodary index
  
    所有需要的信息都在辅助索引中
    
    * No need to go to the main table
    
      不需要转到主表
    
    * Efficient regardless of number of tuples retrieved
    
      无论检索的元组数量如何，都是高效的
    
    > All I need is gap, and the gap is in the index, why should I spend the time looking at tuples. 
    >
    > 我只需要gap, gap在索引中，为什么我要花时间看元组
  
* This is very useful for multi-attribute indices

  这对于多属性索引非常有用
  
  * Index where keys are a combination of attributes (att1, att2, att3, ...)
  
    索引，其中键是属性的组合(att1, att2, att3，…)
  
  * Order is based on att1, if tied then att2, if tied again att3 etc.
  
    顺序基于att1，如果平局则att2，如果再次平局则att3等。

>  if you think that people will actually ask this query a lot. 如果你认为人们会经常问这个问题
>
>  $\Pi_{name,ssn}(\sigma_{gpa>?}(Student))$
>
>  That it is absolutely worthy to create a index with a gpa followed by ssn. Because, hey, for this query, if I have that index, I don't even need to touch the table. I can get everything I need from the Index. Now, obviously, there is no free lunch.
>
>  它绝对值得创建一个以gpa和ssn为基础的索引。因为，嘿，对于这个查询，如果我有那个索引，我甚至不需要碰表。我可以从索引中得到我需要的一切。显然，天下没有免费的午餐。





## Number of parse tree/plans ✅

* Each decorated parse tree is known as a plan

  每个修饰过的解析树都被称为一个plan

* The number of plans can grow very quickly

  计划的数量可以快速增长

* E.g. a query with a N-way joins can have $(n-1)!$ ways to order it. (why?)

  例如，一个具有N-way联结的查询可以包含$(n-1)!$ 顺序方式。(为什么?)

  * This does not even consider the various option (e.g. outer vs. inner loops)

    这甚至没有考虑各种选项(例如外部循环和内部循环)

  > We have four tables: $A_1, A_2, A_3, A_4$  and do the join
  >
  > $4\times 3 \times 2 \times 1$
  >
  > So essentially I can order them whatever way they want and I wouldn't even consider the associated mass number.
  >
  > I won't bore you with the combinatorics, but if you want to calculate the number of combination that you can have, I'll spare you the exponential and worth. And you, as I say, write the key thing about credit optimization. I don't want to spend 2 hours optimizing a query such like a safe one sec. So examining all the trees is just flat out impossible.
  >
  > 所以基本上我可以任意排列它们我甚至不用考虑相关的质量数。我不会用组合数学来烦你，但如果你想计算组合的个数，我就不告诉你指数和值了。而你，如我所说，写出了关于信用优化的关键。我不想花2个小时来优化一个查询，就像一个安全的一秒，所以检查所有的树是完全不可能的。

* Thus we need to limit the number of parse tree generated

  因此，我们需要限制生成的解析树的数量

* Also after chosen a parse tree one will need to find the best way to decorate the tree.

  在选择了解析树之后，还需要找到装饰树的最佳方法。

>  We look at comparing a feeling of  parse tree.  But remember what one of the main problem, the theory optimizer, is There's a whole lot of parse tree. Very many parse tree through. exponential parse tree. I'm dead. If all you have is selection and projection, there's only so many things you can do. If it is a single table query. There's really nothing much to talk about. The the main reason why you have a lot of pastry are joins, because those accommodative jobs are associated.
>
>  我们来比较一下解析树的感觉。但是记住一个主要的问题，理论优化器，是有很多的解析树。非常多的解析树通过。指数解析树。我已经死了。如果你只有选择和投影，那么你能做的事情就只有这么多。如果是单表查询。没什么好谈的。你有很多糕点的主要原因是加入，因为这些容纳工作是相关联的。

* Must consider the interaction of evalution techniques when choosing evaluation plans

  在选择评估方案时必须考虑评估技术的相互作用

  * choosing the cheapest algorithm for each operation independently may not yield best overall algorithm. 

    为每个操作单独选择最便宜的算法可能不会产生最佳的整体算法。

    E.g.
  
    * Sort-Merge-join may be costlier than hash-join, but may provide a sorted output which reduces the cost for an outer level aggregation.
    
      Sort-Merge-join可能比hash-join开销更大，但可以提供有序的输出，从而降低外层聚合的开销
  
      > sort merge you had to sort both tables, hash join you just only need one not the table to be small enough however sort merge do return the tuples in sorted order. And that sort of order may be invaluable in cutting down the next operation.
      >
      > If nothing else, what if your query have `order by`  join condition. Then sort merge suddenly become ten times more attractive. Because if I do sort merge here, I don't have to do sort at the end. So that means greedy algorithm doesn't quite work. You cannot say, let's look at each operation, find the most greedy solution for that and then go on from there.
      >
      > 排序合并你必须对两张表进行排序，散列连接你只需要一张表而不是足够小的表，然而排序合并确实会以有序的顺序返回元组。这样的顺序对于减少下一次操作可能是非常宝贵的。
      >
      > 如果你的查询有`order by`联结条件，怎么办?然后排序合并突然变得有十倍的吸引力。因为如果我在这里做归并排序，我就不需要在最后做排序。这意味着贪心算法不太管用。你不能说，让我们看看每个操作，找到最贪婪的解，然后从那里继续下去。
    
    * Nested-loop join may provide opportunity for pipelining
    
      嵌套循环连接可以为管道提供机会

>  And to make things even worse, maybe I can be greedy. Let's say for each operation, I'll take the most efficient method and then try to combine them. Maybe things are easy. But even that, you have to be careful.
>
>  更糟糕的是，也许我可以变得贪婪。对于每个操作，我将采用最有效的方法，然后尝试将它们结合起来。也许事情很简单。但即便如此，你也得小心。



## 16.4.1 Cost-Based Optimization 基于代价的连接顺序选择 ✅

* Consider finding the best join-order for $r_1\Join r_2\Join ... \Join r_n$

  考虑为 $r_1\Join r_2\Join ... \Join r_n$寻找最佳连接顺序

* There are $\frac{(2(n-1))!}{(n-1)!}$ different join orders for above expression. With $n=7$, the number is 665280, with $n=10$, the number is greater than 176 billion!

  有$\frac{(2(n-1))!}{(n-1)!}$上述表达式的连接顺序不同。当$n=7$时，数字是665280，当$n=10$时，数字大于1760亿!

* No need to generate all the join orders. Using dynamic programming, the least-cost join order for any subset of ${r_1, r_2, ... r_n}$ is computed only once and stored for future use.

  不需要生成所有的关联顺序。利用动态规划方法，求${r_1, r_2, ... ,r_n}$ 的任意子集的最小连接顺序代价, 只计算一次，并存储以备将来使用。

> Number one. This to some degree is a dynamic programing problem. Let's say you have a bunch of matrices. And you want to multiply them.
>
> 第一。这在某种程度上是一个动态规划问题。假设你有一堆矩阵。要把它们相乘。
>
> $A_1 \times A_2 \times A_3 \times A_4$
>
> Matrix multiplication is not commutative. However it is associated. That means I don't care which modification you do first, the result will still be the same. However, if you do it in a different order, the total number of operation can change drastically. 
>
> 矩阵乘法是不可交换的。但它是有关联的。这意味着不管你先做哪项修改，结果都是一样的。然而，如果你以不同的顺序执行，操作的总数可能会发生巨大的变化.
>
> And you have to find the best way of doing a multiplication. And you you can resort to direct programing. Here doing a join have some flavor of this not quite exactly like that. But you can also resort to some form of dynamic programing to basically calculate the best course of each of the joins.
>
> 你必须找到做乘法的最佳方法。你可以求助于直接编程。这里的联结操作有点类似，但不完全是那样。但是，您也可以求助于某种形式的动态规划来基本上计算每个连接的最佳过程.
>
> Why this is not fully applicable because in the major lubrication problem, making modification is not commutative.
>
> 为什么这并不完全适用，因为在主要润滑问题上，做出的修改是不可交换的.
>
> Here. The join is actually commutative. So you can actually write this $r_2\Join r_1...$  It was to give you the correct result. So that will actually add more pressure to the dynamic program.
>
> 在这里。联结实际上是可交换的。所以你可以写成$r_2\Join r_1…$它是为了给你正确的结果。这实际上会给动态程序增加更多的压力。



#### Dynamic Programming in Optimization 优化中的动态规划 ✅

* To find best join tree for a set of $n$ relations:
  
  找到$n$关系集合的最佳关联树:
  
  * To find best plan for a set $S$ of $n$ relations, consider all possible plans of the form: $S_1\Join (S-S_1)$ where $S_1$ is any non-empty subset of $S$.
  
    为$n$关系的$S$集合找到最佳方案，考虑如下形式的所有可能方案:$S_1\Join (S-S_1)$其中$S_1$是$S$的任意非空子集
  
  * Recursively compute costs for joining subsets of $S$ to find the cost of each plan. Choose the cheapest of $2^n -2$ alternatives.
  
    递归计算连接$S$的子集的成本，以找到每个方案的成本。选择$2^n -2$中最便宜的选项。
  
  * Base case for recursion: single relation access plan
    
    递归的基本条件:单一关系访问计划
    
    * Apply all selections on $R_1$ using best choice of indices on $R_1$
    
      使用$R_1$上的最佳索引选择将所有选择应用于$R_1$
    
  * When plan for any subset is computed, store it and reuse it when it is required again, instead of recomputing it.
    
    当为任何子集计算plan时，存储它并在再次需要时重用它，而不是重新计算它。
    
    * Dynamic programming
    
      动态规划

>So the key idea is this. If you have a big Join. $S_1 \Join S_2\Join S_3 \Join S_4$. What you really want to do is that start from doing one join, calculate the cost, caculate back to one join. Then you combine the two one join into a join into two joins and based on the result of the one join, see you can get a better reuslt for the two joins.  either resorting to the same principle or use that algorithm, like sort merge. sort merge not be the best in a single operation, but the two johns are actually join, all the same attributes a sudden become attractive. So we can do that and then we build. The key idea is that we keep track of the best plan for each smaller subset.
>Now, obviously, there's a limitations. If you have n joins, How many possible subsets? So just the total number of subset, it's explanation. So we can't quite pull the same trick totally. We still have to have some limitations. So we won't go into detail.
>
>关键思想是这样的。如果你有一个大的加入。$S_1 \Join S_2\Join S_3 \Join S_4$。你真正想做的是从一个联结开始，计算成本，再计算回一个联结。然后将两个1联结合并成一个2联结，再根据一个联结的结果，看看两个联结能得到更好的结果。要么使用相同的原则，要么使用算法，比如排序合并。归并排序在一次操作中不是最好的，但两个约翰实际上是合并，所有相同的属性突然变得有吸引力。所以我们可以这样做，然后我们构建。关键是我们要跟踪每个较小子集的最佳方案。
>
>很明显，这是有限制的。如果有n个连接，有多少个可能的子集?这就是子集的总数，这就是解释。所以我们不能完全用同样的方法。我们仍然需要一些限制。所以我们不会详细讨论。



#### Join Order Optimization Algorithm

```pseudocode
procedure findbestplan(S)
	if (bestplan[S].cost ≠ ∞)
		return bestplan[S]
		// else bestplan[S] has not been computed earlier, compute it now
	if (S contains only 1 relation)
		set bestplan[S].plan and bestplan[S].cost based on the best way of accesing S using selections on S and 		     indices (if any) on S
	else for each non-empty subset S1 of S such that S1 ≠ S
		P1 = findbestplan(S1)
		P2 = findbestplan(S-S1)
		for each algorithm A for joining results of P1 and P2
			// For indexed-nested loops join, the outer could be P1 or P2
			// Similarly for hash-join, the build relation could be P1 or P2
			// We assume the alternatives are considered as separate algorithms
				if algorithm A is indexed nested loops
					Let Pi and P0 denote inner and outer inputs 
					if Pi has a single relation ri and ri has an index on the join attribute
						plan = "execute P0.plan; join results of p0 and ri using A",
										with any selection conditions on Pi performed as part of the join condition
						cost = P0.cost + cost of A
					else cost = ∞; /* cannot use indexed nested loops join*/
				else 
					plan = "execute P1.plan; execute P2.plan;
									join results of P1 and P2 using A;"
					cost = P1.cost + P2.cost + cost of A
		  	if cost < bestplan[S].cost
		  		bestplan[S].cost = cost
		  		bestplan[S].plan = plan;
	return bestplan[S]
```

>  So they list some kind of recursive algorithm. But you really should do it in dynamic programming.
>
>  他们列出了某种递归算法。但你应该用动态规划来做。

> Most database system use the following trick to limit the number of clicks, which is something what we call a deep join tree.
>
> 大多数数据库系统使用以下技巧来限制点击次数，我们称之为深度连接树。



### 16.4.3 Left Deep Join Trees ✅

* In **==left-deep join trees==**, the right-hand-side input for each join is a relation, not the result of an intermediate join.

  在**==left-deep join trees==**中，每个连接的右侧输入是一个关系，而不是中间连接的结果。

  左深连接顺序用于流水线计算特别方便, 因为右操作对象是一个已存储的关系, 每个连接只有一个输入来着流水线.

  



![Screenshot 2022-10-30 at 03.32.08](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-30 at 03.32.08.png)

> Anything peculiar about the tree on the left?
>
> Every right child will actually go directly to a leaf. There's no subtree. Why do we do that? Because if we are lucky, if that's the right algorithm, we can pipe by all the way from beginning to end. And we are seeing that they can potentially be very beneficial. So why not do this? Now, it certainly cut down on the number of plans because you restricted, you know,
>
> A permutation you can permit. But at least there's a lot of other things you have to work out.
>
> $r_1, r_2 ..... r_5$
>
> 左边的树有什么特别的吗?
>
> 每个右子结点都会直接指向叶结点。没有子树。我们为什么要这样做?因为如果我们幸运的话，如果这是正确的算法，我们可以从头到尾进行管道连接。我们看到它们可能是非常有益的。那么为什么不这样做呢?现在，它确实减少了计划的数量因为你限制了，
>
> 你可以允许的一种排列。但至少还有很多其他事情需要解决。
>
> $r_1, r_2 .....r_5$

> So many database system even nowadays will cheat in the sense that I only consider lefty trees unless I really only join in two or three tables, then I would consider more things. But if I have join six seven tables, I would then only consider that the definition. And as you say, the main advantage of left-deep tree is that you can pipeline to the very top if you if you choose to. Once again does doesn't automatically do that. It may not be worth it, but at least keep the options of doing it.
>
> 即使是现在，很多数据库系统也会作弊，我只考虑左树，除非我真的只关联两到三张表，否则我会考虑更多的事情。但是如果我已经join了六七个表，那么我只会认为这是定义。就像你说的，**<u>==左深树的主要优点是，如果你愿意的话，你可以流水线到最顶端。它不会自动这样做。这样做可能不值得，但至少保留这样做的选择。==</u>**



#### Quiz 4 ✅

Which of the following about pipeline/materialization is correct?

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
> ![Screenshot 2022-10-29 at 20.44.48](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-29 at 20.44.48.png)
>
> (b)左深树的一个优点是可以沿着树的整个左路径进行流水线。
>
> 左深连接顺序用于流水线计算特别方便, 因为右操作对象是一个已存储的关系, 每个连接只有一个输入来着流水线.



## Cost of Optimization ✅

* With dynamic programming time complexity of optimization with bushy tree is $O(3^n)$

  在动态规划下，用灌木树优化的时间复杂度为$O(3^n)$

  * With $n = 10$, this number is 59000 instead of 176 billion!

    当n = 10美元时，这个数字是59000而不是1760亿!

* Space complexity is $O(2^n)$

  空间复杂度为$O(2^n)$

* To find best left-deep join tree for a set of $n$ relations: 

  为$n$关系查找最佳左深连接树

  * Consider $n$ alternatives with one relation as right-hand side input and the other relations as left-hand side input.

    考虑$n$选项，其中一个关系作为右侧输入，另一个关系作为左侧输入

  * Modify optimization algorithm:

    修改优化算法:

    * Replace "for each non-empty subset S1 of S such that S1 $\neq$ S"

      替换“每个非空子集S1 (S)，使S1 $\neq$ S”
    
    * By: for each relation r in S
    
      ​			 let S1 = S - r.

* <u>If only left-deep trees are considered, time complexity of finding best join order is $O(n 2^n)$</u>

  如果只考虑左深树，寻找最佳连接顺序的时间复杂度为$O(n2 ^n)$

  * Space complexity remains at $O(2^n)$

    > Remeber $O(2^n) <\neq O(3^n)$   This constant actually matters.
    >
    > If you can change $O(3^n)$ to $ O(2^n)$, you save a lot.

* <u>Cost-based optimization is expensive</u>, but worthwhile for queries on large datasets (typical queries have small n, generally < 10)

   <u>基于成本的优化是昂贵的</u>，但对于大型数据集的查询是值得的(典型的查询有小n，一般是&lt;10)
  
  > But if your table is really, really huge, you had tons of tuples.
  >
  > 但如果你的表非常非常大，你有很多元组。
  >
  > So things can get very dicey if you're not careful. So that's why even though it can be expensive, it's worth it if you have a large table. And obviously, if I'm a database company, I want to sell it to Wal-Mart Mart.
  >
  > 所以如果你不小心，事情会变得很危险。这就是为什么尽管它可能很贵，但如果你有一个大桌子，它是值得的。显然，如果我是一家数据库公司，我想把它卖给沃尔玛。

> So if you use dynamic programing and you allow any kind of trees, the time compresses all the free to up it.
>
> 所以如果你使用动态编程并且你允许任何种类的树，时间会压缩所有的自由。



> We'll go through it relatively fast until we react, until we answer your question D self-styled relatively fast. I will ask question on the quiz. I'll probably won't ask question on the exam.
>
> 我们会相对快速地过一遍直到我们做出反应，直到我们相对快速地回答你的问题D。我将在测验中提问。我可能不会在考试中提问。



### ==16.4.1 Interesting Sort Orders== ✅

* Consider the expression $(r_1\Join r_2)\Join r_3$ (with A as common attribute)

  考虑表达式$(r_1\Join r_2)\Join r_3$(以A作为公共属性)

* An ==**interesting sort order**== is a particular sort order of tuples that could make a later operation (join / group by / order by) cheaper

  一个==**感兴趣的排序顺序**==是元组的一个特殊排序顺序，它可以使后面的操作(join / group by / order by)更便宜

  若某个具体的元组排序顺序对后面的运算可能有用的话, 我们称该特定的顺序是个一个感兴趣的排序顺序(interesting sort order).

  > $A \Join _{A.a=B.b} B \Join_{B.b=C.c} C$
  >
  > Sorting these table in B.b maybe worthwhile because it may help you save time for doing this join.
  >
  > $A \Join _{A.a=B.b} B \Join_{B.c=C.c} C \Join_{B.b =d.k }D$
  >
  > Maybe it's not. Maybe just one step, but this is still a potentially interesting order. because B.b can use in B.b=d.k
  >
  > So if you do it optimization every time, one thing you do want to remember is whether the my result is sorted or not. And sorted on which attribute. You can only sort your result on one attribute. You can not sort a multiple attribute. So storing that information is cheap. But that can be helpful significantly down the line like.
  >
  > $A \Join _{A.a=B;b} b \Join_{b .b=C} C$
  >
  > 在B.b中对这些表进行排序可能是值得的，因为它可以帮助您节省执行这个连接的时间。
  >
  > $A \Join _{A.a=B;b} b \Join_{B.c C =C.c} C \Join_{b。b = d。k} D $
  >
  > 也许不是。也许只是一步，但这仍然是一个潜在的有趣的顺序。因为B.b可以用B.b=d.k
  >
  > 如果你每次都进行优化，你需要记住的一件事就是，i的结果是否已经排序。并根据哪个属性排序。您只能根据一个属性对结果进行排序。不能对多个属性排序。所以存储这些信息很便宜。但这对以后的工作很有帮助。

  * Using merge-join to compute $r_1\Join r_2$ may be costlier than hash join but generates result sorted on A

    使用合并连接计算$r_1\Join r_2$可能比哈希连接成本高，但生成的结果按A排序

  * Which in turn may make merge-join with $r_3$ and minimizing overall cost

    这反过来可能使合并连接$r_3$和最小化总成本

* Not sufficient to find the best join order for each subset of the set of $n$ given relations

  不足以为$n$给定关系集合的每个子集找到最佳连接顺序
  
  * must find the best join order for each subset, for each interesting sort order

    必须为每个子集找到最佳连接顺序，为每个有趣的排序顺序
  
  * Simple extension of earlier dynamic programming algorithsm
  
    早期动态规划算法的简单扩展
  
  * Usually, number of interesting orders is quite small and doesn't afftect time/space complexity significantly
  
    通常情况下，有趣的订单数量很少，不会显著影响时间/空间复杂度
  
  > But now make things more challenge is that $A \Join_{A.a= B.b} B \Join_{B.k=c.d} C$
  >
  > At the very least I can sort my result value on $A.a$ or $B.k$ .  This is the only thing we do that doesn't seems to be worth it.
  >
  > But if you sql has an `order by` query. That might be change the story. If your sql have `group by B.k` Now you should really think about joining them because the group by operation was suddenly become much cheap. That's why you have to look at Join order to see how. 
  >
  > To make things more interesting $A\Join_{A.a=B.b}B \Join_{B.c=C.k}C$ and in your sql query `select distinct a.k` Now this order `A.k` become an interesting order. Because we have to remove duplicates. That means you either have to sort the result, or have to hash the result. So that become another important, interesting sort order. And if you really, really want to do a good job optimizing, you really have to consider. If I want to maintain my results that we sort in a certain order, I want to at least keep track. And you want to maintain this sort of thing in certain order. That means, for example, you may not be able to use an index. That means you are paying a price as somewhat a step, but I'm paying the price to remain in the right order so I can do better in the next step. And that's the question a great optimizer has to us.
  >
  > 但现在更有挑战性的是 $A \Join_{A.a= B.b} B \Join_{B.k=c.d} C$
  >
  > 至少我可以根据 $A.a$ or $B.k$对结果值进行排序. 这是我们做的唯一不值得的事情。
  >
  > 但是如果sql有一个`order by`查询。这可能会改变故事。如果你的sql有`group by B.k`，现在你真的应该考虑加入他们，因为group by操作突然变得很便宜。这就是为什么您必须查看Join以了解如何操作。
  >
  > 为了使事情更有趣$A\Join_{A.a=B.b}B \Join_{B.c=C.k}C$ 和在您的sql查询`select distinct a.k`现在这个 `A.k` 变成了一个有趣的顺序。因为我们必须去掉重复的部分。这意味着您要么必须对结果进行排序，要么必须对结果进行哈希。这是另一个重要有趣的排序顺序。如果你真的，真的想做好优化工作，你就必须考虑。如果我想保持按一定顺序排序的结果，我至少要保持跟踪。你需要以一定的顺序来维持这些东西。这意味着，例如，您可能无法使用索引。这意味着你要为每一步付出代价，但我要为保持正确的顺序付出代价，这样我才能在下一步做得更好。这是一个伟大的优化者要问我们的问题。



### Quiz 5 ✅

Consider the first part of a multi-table query r1$\Join$ r2 (with the join condition r1.a = r2.a). Which of the following will make sort-merge a potential best-case scenario?

(a) At the end the tuples needed to be ordered by r1.a

(b) There is a subsequent join with the condition r1.b - r3.b

(c) There is a subsequent join with the condition r1.a - r3.c

a. c ✅

> a 属性sort - merge 之后是ordered. 所以需要该属性ordered就是答案
>
> (a) 需要a属性ordered 所以 是
>
> (b) 这里的condition都是关于b属性, 所以a属性的ordered 没有半毛钱关系
>
> (c) 这里的a是order的所以有助于condition 中 a属性的利用



###  16. 4. 2 Cost Based Optimization with Equivalence Rules ✅

* **==Physical equivalence rules==** allow logical query plan to be converted to physical query plan specifying what algorithms are used for each operation.

  **==物理等价规则==**允许将逻辑查询计划转换为物理查询计划，指定每个操作使用什么算法。

  添加一类新的称为物理等价规则(physical equivalence rule) 的等价规则, 允许将例如连接这样的逻辑操作转换成像散列连接或嵌套循环连接这样的物理操作. 通过将这类规则添加到原来的等价规则中, 程序可以产生所有可能的执行计划.

* Efficient optimizer based on equivalent rules depends on 
  
  高效优化器基于等价规则的依赖
  
  * A space efficient representation of expressions which avoids making multiple copies of subexpressions
  
    一种节省空间的表达式表示形式, 来避免应用等价规则时创建相同子表达式的多个副本.
  
  * Efficient techniques for detecting duplicate derivations of expressions
  
    检测相同表达式重复推导的有效技术
  
  * A form of dynamic programming based on memoization, which stores the best plan for as subexpression the first time it is optimize, and reuses in on repeated optimization calls on same subexpression
  
    一种基于缓存(memoization) 的动态规划形式, 当第一次优化子表达式时, 该缓存存储最优的查询执行计划; 后续优化相同子表达式的请求通过返回已经缓存的计划进行处理.
  
  * Cost-based pruning techniques that avoid generating all plans
  
    基于成本的修剪技术，避免生成所有的计划
  
    通过维护到任何时刻为止为任何子表达式产生的代价最低的计划, 并且对其他任何比当前该子表达式代价最低计划的代价高的计划进行剪枝, 避免产生所有可能的执行计划的技术.
  
* Pioneered by the Volcano project and implemented in the SQL Server optimizer

  这个方法由Volcano研究项目率先提出, 并且SQL Server的查询优化器也是基于该技术.

> So here so far we talk about like, hey, I can do selection first, then do projection.
>
> But you can also go to the physical level.
>
> If you a table A, B and C, What if table A and B is in the same track but C on a different track. Then doing $A\Join B$ first become more attractive. So this is where the physical componet comes into play. So some system have been even starting to really squeeze every drop of performance.Some systems are really starting to think in these terms.  I actually look at where the data is physically located to see if I can do something even better.
>
> 到目前为止，我们讨论的是，我可以先做选择，然后做投影。
>
> 但你也可以去物理层面。
>
> 如果你有表a, B和C，如果表a和B在同一个轨道上，而C在不同的轨道上怎么办?那么做 $A\Join B$就变得更有吸引力了。这就是物理组件发挥作用的地方。所以有些系统甚至开始挤压每一点性能。一些系统真的开始从这些方面思考。我实际上查看数据的物理位置，看看我是否可以做得更好。



### 16.4.3 Heuristic Optimization 启发式优化 ✅

* Cost-based optimization is expensive, even with dynamic programming.

  基于成本的优化是昂贵的，即使是动态规划。

* Systems may use heuristics to reduce the number of choices that must be made in a cost-base fashion.

  系统可以使用启发式来减少必须以成本为基础的方式做出的选择的数量。

* Heuristic optimization transforms the query-tree by using a set of ruls that typically (but not in all cases) improve execution performance:
  
  启发式优化通过使用一组规则来转换查询树，这些规则通常(但不是所有情况下)提高执行性能:
  
  * Perform selection early (reduces the number of tuples)
  
    提前执行选择(减少元组的数量)
  
  * Perform projection early (reduces the number of attributes)
  
    提前执行投影(减少属性的数量)
  
  * Perform most restrictive selection and join operations (i.e., with smallest result size) before other similar operations.
  
    在其他类似操作之前执行最限制性的选择和连接操作(即，结果大小最小的操作)。
  
  * Some systems use only heuristics, others combine heuristics with partial cost-based optimization.
  
    有些系统只使用启发式，有些则将启发式与部分基于成本的优化相结合。

> for example, we always look for selection first. I always try to figure out what's the most restricted and most join adoption operation and do that first. Some system is basically just to these rules.
>
> So it's kind of a balancing act. The rules will restrict the number of plans you're going to generate. Those rules may not always give you the best plan. But it has the advantage of limiting the number of rules you do so that you can actually so that the query optimizer can be fast.
>
> 例如，我们总是首先寻找选择。我总是试图弄清楚什么是最受限制的和最容易参与的采用操作，然后首先做这些。有些系统基本上就是这些规则。
>
> 所以这是一种平衡。这些规则会限制你计划的数量。这些规则可能并不总是给你最好的计划。但是它有限制规则数量的优点，这样你就可以让查询优化器更快。



> So as they mentioned many optimizer consider only left deep Join orders and he heuristic. 
>
> 所以正如他们提到的，许多优化器只考虑左深连接顺序和启发式。



### 16.4.3 Structure of Query Optimizers ✅

* Many optimizers considers only left-deep join orders.
  
  许多优化器只考虑左深连接命令。
  
  * Plus heuristics to push selections and projections down the query tree
  
    加上启发式的选择和预测下推查询树
  
  * Reduces optimization complexity and generates plans amenable to pipelined evaluation.
  
    降低优化的复杂性，生成适合流水线评估的计划
  
* Heuristic optimizaiton used in some versions of Oracle:
  
  在Oracle的某些版本中使用启发式优化

  * Repeatedly pick "best" relation to join next
    
    重复选择“最佳”关系加入下一步
    
    * Starting from each of n starting points. Pick best among these
    
      从n个起始点开始。从这些中选出最好的
  
* Intricacies of SQL complicate query optimizaiton 
  
  SQL的复杂性使查询优化变得复杂
  
  * E.g. , nested subqueries.
  
    例如，嵌套子查询

> For example, I mentioned earlier, Greddy doesn't always give you the best solution, but what's good about greedy algorithms. Compared with dynamic programming. Fast 
>
> Why greedy algorithm is in general fast than dynamic programming, Because whenever greedy ever make a choice, they never turn back. Once I make a choice, I am not going to regret my choice. I'm going to go forward without turning my back. So that means I can go first.
>
> dynamic programing always  you grab to reconsider your choice. That's why you make this slow. But that also means that the greedy algorithm doesn't always will work.  In fact, very often it doesn't give you the best solutions, but it does give you a fair solution.
>
> 例如，我之前提到过，Greddy并不总是能给出最好的解决方案，但贪婪算法的优点是什么?与动态规划进行比较。快
>
> 为什么贪婪算法通常比动态规划快，因为每当贪婪做出选择时，他们永远不会回头。一旦我做出选择，我不会后悔我的选择。我要勇往直前，不背身而行。所以我可以先来。
>
> 动态规划总是让你重新考虑你的选择。这就是为什么你要放慢速度。但这也意味着贪心算法并不总是有效。事实上，它通常不会给你最好的解，但它会给你一个公平的解。



* Some query optimizers integrate heuristic selection and the generation of alternative access plans.

  一些查询优化器集成了启发式选择和可选访问计划的生成.

  * Frequently used approach

    常用方法

    * heuristic rewriting of nested block structure and aggregation

      启发式重写嵌套块结构和聚合

    * followed by cost-based join-order optimization for each block

      然后对每个块进行基于代价的连接顺序优化

  * Some optimizers (e.g. SQL Server) apply transformations to entire query and do not depend on block structure

    一些优化器(例如SQL Server)将转换应用于整个查询，而不依赖于块结构

  * **==Optimizaiton cost budget==** to stop optimizaiton early (if cost of plan is less than cost of optimization)

    **==优化成本预算==**提前停止优化(如果计划成本小于优化成本)

  * **==Plan caching==** to reuse previously computed plan if query is resubmitted.

    **==计划缓存==**，以便在重新提交查询时重用之前计算的计划。

    * Even with different constants in query
    
      即使在查询中使用不同的常量
    
    > One thing I do mention is that many advanced databases don't have what we call plan cache. There's actually some memory buffers set aside to store query projects. In fact, many career optimizer allowed the DBA to specify certain claims to be stopped. That's why we need to teach you that, because you might be a DBA one day and these are the things you will interact with them a lot.
    >
    > 我提到的一件事是，许多高级数据库没有我们称为计划缓存的东西。实际上，有一些内存缓冲区被留出来存储查询项目。事实上，许多职业优化器允许DBA指定要停止的某些声明。这就是为什么我们要教你这些，因为有一天你可能会成为一名DBA，你会和他们有很多互动。

* Even with the use of heuristics, cost-based query optimizaiton imposes a substantial overhead.

  即使使用启发式方法，基于代价的查询优化也会带来很大的开销。
  
  * But is worth it for expensive queries
  
    但对于昂贵的查询来说是值得的
  
  * Optimizers often use simple heuristics for very cheap queries, and perform exhaustive enumeration for more expensive queries.
  
    优化器通常对非常廉价的查询使用简单的启发式方法，对更昂贵的查询执行穷举枚举

> Now when I say when I say query is small, I'm not saying the number of tuples is small. I'm saying that that's only involved like two or three tables. And then we will find the best query if there's a large. All in all on the other hand if the tuples in what is really small. If you have large query, but each table is very small. Who cares just do some things. Even if we don't get the best solution is not the end of the world. But if the table if you are joining we have 10 billion to hold each, then may be worthy to actually spend 5 minutes stopping.  So once again, this is self. Whether I how much effort I need to plan to optimize a query. If a decision to query Optimizer. 
>
> 当我说查询很小的时候，我并不是说元组的数量很小。我是说那只需要两到三张桌子。然后我们会找到最好的查询，如果有一个大。All in All另一方面，如果元组里的东西真的很小。如果你有一个大的查询，但是每个表都很小。谁在乎呢，做点什么就好。即使我们没有得到最好的解决方案，也不是世界末日。但是如果桌子如果你加入我们每个人有100亿，那么可能值得花5分钟停下来。同样，这是self。我是否需要花多少精力来计划优化一个查询。如果决定查询优化器。





## Cost estimation ✅

* Recall the basic problem of query execution (slight modified)

  回顾查询执行的基本问题(略有修改)

  * The best way to execute a query (operation) depends on the size of its results, which you don't know until you execute it.

    执行查询(操作)的最佳方式取决于结果的大小，在执行之前你并不知道结果的大小.

* Thus need to estimate the tuples return from an operation.

  因此需要估计操作返回的元组

  > That's the chicken and egg problem. So now that in itself cannot be solved because it is a chicken egg problem. However, even though we cannot get the exact number of tuples to be returned, we can make a guess. And if my guess is good, then maybe things can work up. So probably since the mid-nineties. The majority of effort in sql optimization is being built on cost estimation. How do I estimate the number of tuples to be returned from a query? There is a huge amount of effort in doing this. 
  >
  > 这是先有鸡还是先有蛋的问题。所以现在这个问题本身无法解决，因为这是一个先有鸡还是先有蛋的问题。然而，尽管我们无法得到要返回的元组的确切数量，但我们可以猜测一下。如果我猜对了，也许事情会有转机。大概从90年代中期开始。sql优化的大部分工作都建立在成本估算上。我如何估计从查询返回的元组的数量?要做到这一点需要付出巨大的努力。
  
  > Let say I do a query $\sigma_{(A.c <= 10)}A \Join_{A.a=B.b} B$
  >
  > What information do the database system have that you think can be useful in estimating the result of the query? Or what do you think the database system should need, should have in order to estimate? 
  >
  > First, you need to know how tuples in A and how many tuples should be in B. Otherwise, there's no place to start. But that can be easily maintained by the database system every time.  I just thought extra number every time you create  add one to it. That's not costly to maintain.
  >
  > 1. So the number of tuples
  >
  > What else do you think? You need to make a good estimation?
  >
  > 2. Distribution of C
  >
  > What other information do you think you can be useful?
  >
  > 3. Is A.a unique?
  >
  > Why is this important? If A.a is unique, what does it mean to look? 
  >
  > Every tuple in B can only join one tuple in A. You immediately have a up bar of the result of the join.
  >
  > Obviously. Is B.b unique? This is symmetrical.
  >
  > 4. distinstion co A.a / B.b
  >
  > Less than that still can useful
  >
  > <img src="/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-30 at 23.34.41.png" alt="Screenshot 2022-10-30 at 23.34.41" style="zoom: 33%;" />
  >
  > The distribution of A.a B.b
  >
  >  maybe we can still get a reasonable estimate of the sign of query. So with that we can still do something. But remember, there is no free lunch. If I need to know this distribution, I have to what store information about this distribution was again. Now, the second chicken egg problem. I need read them then I know the distribution.
  >
  > A.a B.b的分布
  >
  > 也许我们仍然可以得到查询符号的合理估计。因此，我们仍然可以做一些事情。但是要记住，天下没有免费的午餐。如果我需要知道这个分布，我需要知道这个分布的存储信息。现在来看第二个鸡生蛋的问题。我需要阅读它们才能知道它们的分布。



## ==16.3 Statistical Information for Cost Estimation==

表达式结果集统计大小的估计

* $n_r$: number of tuples in a relation $r$

  关系r的元组数

* $b_r$: number of blocks containning tuples of $r$.

  包含关系r中元组的磁盘块数

* $l_r$: size of a tuple of $r$.

  关系r中每个元组的字节数

* $f_r$: blocking factor of $r$ –– i.e., the number of tuples of $r$ that fit into one block

  关系r的块因子—一个磁盘块能容纳关系r中元组的个数.

* $V(A, r)$: number of distinct values that appear in $r$ for attribute $A$; same as the size of $\prod_A(r)$.

  关系r中属性A中出现的非重复值个数. 该值与$\prod_A(r)$的大小相同. 如果A是关系r的主码, 则V(A, r)等于$n_r$

* If tuples of $r$ are stored together physically in a file, then:
  
  如果$r$的元组存储在一个文件中，那么:
  $$
  b_r =\left\lceil \frac{n_r}{f_r}\right\rceil
  $$
  

> Either solid state drive or magic hard drive. 
>
> 固态硬盘或磁盘。
>
> But for now we are talking about mostly figuring out how many tuples fit the answer of the query and that has nothing to do with where the data is being stored.
>
> 但现在我们主要讨论的是确定有多少元组适合查询的答案，这与数据存储在哪里无关。

> For example, let's say we have a table student 
>
> Student(id, name, dept, gpa)
>
> Let's say we have 10,000 tuples for ID in this table. What is this value `V(id, student)`
>
> A: 10,000 Because this the primary key.
>
> Q: How abut `V(dept, Student)` ?
>
> You can't be quite sure because you need domain knowledge. So obviously this is domain knowledge and may not be available. If not, then you will have to do an estimation. 
>
> Q: `V(gpa, Student)`
>
> In an ideal world, this is one, right. So sometimes unique where you make a number of this thing where it may not be important, but for some queries like joins, you will actually see that a group by this can actually be a useful estimate or at least useful thing to know.
>
> 在理想情况下，这是1。因此，有时这个数是唯一的，它可能并不重要，但对于一些查询，如联结，你会看到这个分组实际上是一个有用的估计或至少是有用的东西。



### ==16.3.1 Histograms== 直方图 ✅

Histogram on attribute *age* of relation `person`

![image-20221101124644017](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/image-20221101124644017.png)

* **Equi-width** histograms 等宽直方图

  把取值范围分成相等大小的区间

  > $\sigma_{age<20}(Person) $ This will help you figure out what for you, how well how many tuples are going to be returned.
  >
  > This is probably the most common type, you see.
  >
  > $\sigma_{age<20}(Person) $ 这将帮助你了解将返回多少元组。
  >
  > 你看，这可能是最常见的一种。

* **Equi-depth** histograms break up range such that each range has (approximately) the same number of tuples

  **等深度**直方图划分了范围，使得每个范围(近似)具有相同数量的元组

  * E.g. (4, 8, 14, 19) 

  <img src="/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Chp16 Query Optimization -12.jpg" alt="Chp16 Query Optimization -12" style="zoom:33%;" />

  >$\sigma_{age<= 18}(Person)$
  >
  >for the 1-5, 6-10 11-15 bars satisfy the query. But 16-20 bar you have to estimate.
  >
  >So if you do equi-depth histogram, in some cases, this gives you slightly better estimates. Once again, we wont' go into details why this is happening. So that's why people have been using both types of histograms. So different system prefer  different type of histogram.
  >
  >对于1-5、6-10、11-15条满足查询。但你得估计一下16-20吧.
  >
  >因此，如果你使用等深度直方图，在某些情况下，它会给你更好的估计。同样，我们不会详细说明为什么会发生这种情况。这就是人们使用两种直方图的原因。所以不同的系统喜欢不同类型的直方图。

  >  One thing about store histogram is that it is never a free lunch. Why?
  >
  >  A: Firstly, you have to have space to start a histograms.  Secondly, you'll still need to be updated when you have insertion and deletion that will be a cost involved. 
  >
  >  On the other hand, it may be a bargain. Well, I'm saying there's no free lunch. It doesn't stopping you from getting a huge bargain for lunch. 
  >
  >  关于存储直方图的一点是，它从来都不是免费的午餐。为什么?
  >
  >  答:首先，你必须有空间来绘制直方图。其次，当需要进行插入和删除操作时，仍然需要进行更新。
  >
  >  另一方面，这可能是一个便宜货。我是说天下没有免费的午餐。这并不妨碍你买到便宜货。

  > For example, for the bar 21-25 even though I have a billion tuples, the amount of space required to store this histogram doesn't really change, because I'm still only by numbers. I don't care whether it is numbers one or one million. 
  >
  > Let say I start accessing, I bring that histogram into my memory. I'm going to risk to the dangers of the system crash. But then, because it is so small, I can bring it to my memory and I don't really write the updated version of the disk until where really I'm willing to take that risk. Then at least you kind of now we really get a good balance because the update costs we must has at least in terms of writing the disk.
  >
  > 例如，对于条形图21-25，尽管我有10亿个元组，但存储这个直方图所需的空间并没有真正改变，因为我仍然只使用数字。我不管它是数字1还是100万。
  >
  > 假设我开始访问，我把这个直方图存入我的记忆。我要冒系统崩溃的危险。但是，因为它很小，我可以把它放到我的内存中，我不会真正地写入磁盘的更新版本，直到我真的愿意冒这个风险。我们现在得到了一个很好的平衡因为更新成本我们必须至少有写入磁盘的成本。

* Many databases also store *n* **most-frequent values** and their counts

  许多数据库还存储$n$最频繁的值及其计数

  * Histogram is built on remaining values only
  
    直方图仅基于剩余值构建
    
    > Let say I have age, and it turns out the five most common a here say 18, 19, 20, 21, 22.
    >
    > 假设我有年龄，这里最常见的5个a是18 19 20 21 22。
    >
    > |      | Frequency |
    > | ---- | --------- |
    > | 18   | --        |
    > | 19   | --        |
    > | 20   | --        |
    > | 21   | --        |
    > | 22   | --        |
    >
    > For these five age actually explicitly start a frequency of each because it happens so often. Maybe an exact count here will be more precise. It allows me to make smarter decision. And then the rest of the value I store. because it's not that often maybe estimating them is not going to hurt that much, things like that.  So there's a lot of games you can play essentially and how you're going to play, how you're going to store it.  If I say a good thing about especially even your table scale, it is a very compressed way of storing things. You have to admit that. And the extra costs of storage up the requirement might be worth it.
    >
    > 对于这五岁的孩子来说实际上是明确地开始了每一个的频率因为它发生得太频繁了。也许精确的计数会更精确。它让我做出更明智的决定。然后存储剩下的值。因为它不太经常可能估计它们不会有那么大的伤害，诸如此类。你可以玩很多游戏你将如何玩，如何存储它。如果我说它的优点，尤其是表的规模，它是一种非常压缩的存储方式。你必须承认。而且存储所需的额外成本可能是值得的。

 

> Now how do we calculate histograms?
>
> The obvious thing is that every time we do an update, we update a result. Once again, even with all what all I have said about they still involve costs. It still may not be worth it. For example, if your system require a very good response time, then up in the histogram doesn't have friendly to use. The user does't care if you update the histogram. The user just want query result or just want to know that the tuple have been successfully updated. So a lot of time histogram are not updated in real time. In some extreme histogram are not kept on this.  This is very extreme. Not very often our database system actually do that. But we can what we can do is that every time I access a table, then I will do a guess. I would either do a random guess or I will actually you say get a random sample from the database and then try to use them to estimate the frequency.
>
> 那么我们如何计算直方图呢?
>
> 很明显，每次更新时，我们都会更新结果。再说一遍，即使我说了那么多它们仍然涉及成本。它可能仍然不值得。例如，如果你的系统要求非常好的响应时间，那么在直方图上就没有友好的使用。用户并不关心你是否更新了直方图。用户只想要查询结果，或者只想知道元组已经成功更新。因此很多时间直方图并没有实时更新。在一些极端的直方图中并没有保持这一点。这是非常极端的。我们的数据库系统并不经常这样做。但是我们可以我们可以做的是每次我访问一个表，然后我要做一个猜测。我会随机猜测或者从数据库中随机抽取一个样本然后尝试用它们来估计频率。

* Histograms and other statistics usually computed based on a ==**random sample**==

  直方图和其他统计量通常基于一个 ==**随机样本**==

  > When we actually do calculations, all I need is ratio. I used percentage to represent this, this is perfectly fine.
  >
  > 当我们实际计算时，我只需要比值。我用百分比来表示，这很好。
  >
  > <img src="/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Chp16 Query Optimization -13.jpg" alt="Chp16 Query Optimization -13" style="zoom:33%;" />
  >
  > if you want to estimate the number of tuples, I assume you know the total number of tuples. That is probably one thing the system will keep updating constantly. How often, how much do I need to keep updated if it is slightly off base? Is it the end of world? That's always a question to have to be asked, to have to be balanced.
  >
  > 如果你想估计元组的数量，我假设你知道元组的总数量。这可能是系统会不断更新的一件事。如果有轻微的偏差，我需要多久更新一次?这是世界末日吗?这是一个必须要问的问题，必须要平衡。

* Statistics may be out of date 统计数据可能已经过时

  * Some database require a **analyze** command to be executed to update statistics
  
    有些数据库需要执行**analyze**命令来更新统计信息

  * Others automatically recompute statistics 
    
    其他人会自动重新计算统计数据
    
    * e.g., when number of tuples in a relation changes by some percentage
    
      例如，当关系中的元组数量按百分比变化时
  
  > Now remember another thing to remember. It is easy when I look at one attribute. If you table have 25 attributes and actually five histogram, things start to get dicey. If you insert one to tuple s you have to update 25 attributes that may not necessary. 
  >
  > Your job is to find the bargain of the month. But seldom come free, so you have to make a decision of when to do what. And if you are a system person. This problem is always going to be in your mind whenever you develop something that's always given to.
  >
  > 现在要记住另一件事。当我看一个属性时，这很容易。如果你的表有25个属性和5个直方图，事情就开始变得不稳定了。如果向元组s中插入一个属性，可能需要更新25个不必要的属性。
  >
  > 你的工作是找到本月的便宜货。但很少有免费的，所以你必须决定什么时候做什么。如果你是一个系统的人。这个问题总是会出现在你的脑海中每当你开发一些东西的时候。

> Why you want to equate with? 
>
> A: Once again, I don't want to go into too much detail here.  if data is uniform, uniform with histogram usually do well. If data is somewhat skew. It is a little bit more robust to the skill and some of the thing about it. Think abou this, you are basically fixed by the width. This is 1 to 5. This is 6 to 10. If there's any skewness within each band, it is virtually impossible for you to detect. 
>
> But if you table is large and you number distinction become larger. 
>
> 你为什么要等同?
>
> A:再说一遍，我不想在这里讲太多细节。如果数据是均匀的，那么均匀的直方图通常效果很好。如果数据有些倾斜。它的技巧和一些东西更强大。想想看，宽度基本上是固定的。这是1比5。这是6到10。如果每个频带都有偏斜，你几乎不可能检测到。
>
> 但是如果你的表很大，你的数字区分就会变大。
>
> ![Chp16 Query Optimization -14](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Chp16 Query Optimization -14.jpg)
>
> There's no free lunch, the updating is tricky. Always remember, you can get a bargain, but there's no free lunch.
>
> 天下没有免费的午餐，更新是很棘手的。永远记住，你可以买到便宜货，但天下没有免费的午餐。

### Quiz 5 ✅

Which of the following statements is/are correct?

(a) Equi-width histograms are better than equi-depth histograms to capture skew in data

(b) Suppose in a equi-width histogram there is an entry from 21.0-30.0 with frequency 100. Assuming uniformity, the best guess of number of items between 22.0 - 26.0 is 50.  

My answer: (a)(b) ❌

Correct: (b) ✅

(a) 等宽直方图比等深度直方图更能捕捉数据中的倾斜 ❌

Equi-depth histograms are better than equi-width histograms to capture skew in data 

<img src="/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Chp16 Query Optimization -14.jpg" alt="Chp16 Query Optimization -14" style="zoom: 50%;" />

(b) 假设在等宽直方图中有一个从21.0到30.0的条目，频率为100。假设均匀，在22.0 ~ 26.0之间的物品数量的最佳猜测是50。

✅



### 16.3.2 Selection Size Estimation ✅

* $\sigma_{A=v} (r)$
  * $\frac{n_r}{V(A, r)}$:  number of records that will satisfy the selection
  
    满足选择的记录数
  
    >$n_r$: number of tuples
    >
    >$V(A, r)$: number of distinct values that appear in $r$ for attribute $A$; same as the size of $\prod_A(r)$.
    >
    > So how many distinct Department are there?
    >
    >如果我们假设取值是均匀分布的(即, 每个值以同样的概率出现)
  
  * Equality condition on a key attribute: *size estimate =* 1
  
    关键属性的相等条件:*大小估计=* 1
    
    > $$
    > \sigma_{ID = ''12345''}(Student)
    > $$
    >
    > What's the estimate? How many tuples it is going to return?
    >
    > A: 1 or 0
  
  >  Let's do a selection for first because that's the most obvious one we need to do.
  >
  > Let's say 
  > $$
  > \sigma_{dept=''CS''}(Student)
  > $$
  > Obviously you have a histogram and so you keep up every department can. Obviously you read the histogram. No big deal. You can still order string. You can always get alphabetically if you want it. ![IMG_0673](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/IMG_0673.jpg)
  
* $\sigma_{A\leq V}(r)$ (case of $\sigma_{A \geq V} (r)$ is symmetric)
  
  > This is call range query.
  > $$
  > \sigma_{age \leq 13}(Student)
  > $$
  >  So once again, if you have a histogram. How do you estimate this?
  
  * Let $c$ denote the estimated number of tuples satisfying the condition. 
  
  * If $min(A,r)$ and $max(A,r)$ are available in catalog
    * $c = 0$ if $v < min(A,r)$
    * $c = n_r \frac{v-min(A,r)}{max(A,r)-min(A,r)}$
    
    > ![IMG_0675](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/IMG_0675.jpg)
    >
    > Just make sure when you do the calucuate don't forget to +1, the formulate not detial that, you  have to pay attention to that. 
    
  * If histograms available, can refine above estimate
  
    如果直方图可用，可以改进上述估计
  
  * In absence of statistical information *c* is assumed to be $\frac{n_r}{2}$
  
    在缺乏统计信息的情况下，*c*被假定为$\frac{n_r}{2}$



### 16.3.2 Size Estimation of Complex Selections ✅

>  Here. I do want to bring in a term that people use a lot. The term is called selectivity. Some textbook called the reduction factor.  Noticed that selectivity is always related to a condition.
>
>  在这里。我想引入一个人们经常使用的术语。这个术语叫做选择性。一些教科书称之为减法因子。注意，选择性总是与一种条件有关。

* The **==selectivity==** of a condition $\theta_i$ is the probability that a tuple in the relation $r$ satisfies $\theta_i$ . 

  条件$\theta_i$的**==selective==**是关系$r$中的元组满足$\theta_i$的概率。

  * If $s_i$ is the number of satisfying tuples in $r$, the selectivity of  $\theta_i$ is given by $\frac{s_i}{n_r}$.

    如果$s_i$是$r$中满足的元组的个数，$\theta_i$的选择性由$\frac{s_i}{n_r}$给出。
    
    > For example
    > $$
    > \sigma_{age \leq 13} (Student) 
    > $$
    > The selectivity of this condition is based. What is the probability that tuples in this table will satisfy this condition?
    
    对于每个$\theta_i$, 我们按照以前描述的那样估计选择$\sigma_{\theta_i}(r)$ 的大小, 记为$s_i$. 因此, 关系中的一个元组满足选择条件$\theta_i$ 的概率为$\frac{s_i}{n_r}$. 上述概率称为选择$\sigma_{\theta_i}(r)$ 的中选率(selectivity).

* **Conjunction:** 
  
  **合取** 
  $$
  \sigma_{\theta_1 \wedge \theta_1 \wedge...\wedge \theta_n}(r)
  $$
  **<u>Assuming independence</u>**, estimate of tuples in the result is:
  $$
  n_r \times \frac{s_1 \times s_2 \times s_2 ... \times s_n}{n^n_r}
  $$
  
  > For example
  > $$
  > \sigma_{(age \leq 13) \ AND \ (dept=''CS') }(Student)
  > $$
  > If the selectivity of $age \leq 13$ is 0.5 ; the selectivity of $depat = ''CS''$ is 0.1 .Then I can talk about the selectivity of the overall condition with the `AND`.
  >
  > $0.5\times 0.1 = 0.05$    assuming independence means the age have nothing to do with the department.
  >
  > Q: what's the good thing about so many independents?
  >
  > A:  if you let's say you have histograms, means you only need to keep a histogram on the age and the histogram of the department. You don't have to keep a histogram of age plus the apartment.  you have to be smart or some databases system allow you to tell them this is not really independent. Be careful. Things like that.
  >
  > 问:这么多独立人士有什么好处?
  >
  > A:假设你有一个直方图，这意味着你只需要保留一个关于年龄的直方图和部门的直方图。你不需要保存年龄和公寓的直方图。你必须聪明，否则一些数据库系统允许你告诉他们这不是真正独立的。小心些而已。诸如此类的事情
  
  > Let's say I want to test whether age and department is independent.  I will test it when I answered this query: $\sigma_{(gpa < 3.5)} (Student)$  Because this query has nothing to do with age and  department. So the result I get hopefully will be independent.
  >
  > So a lot of statistics are collected. because you're going to receive the tuples anyway. So let's say if somebody asked you a query on gpa, you will have to return a bunch of tuples and a bunch of tuples return, hopefully now once again, you can easily argued otherwise have nothng to do. It's not related the department. It's not related to two age. Hopefully they are both randomly distributed on that. They say you are really going to retrieve those tuples anyway and why not use those tuples to estimate statistics without me having to look at the whole table, without me having to constantly updating certain things So this is what I mean by piggybacking. Obviously there's no free lunch. If you piggyback things, that means a lot and you spend time answering that query. And that can also slow things down too. So that's always a give and take here, but very often. Piggy banking is a technique that every system uses. I have to give you those tuples, Why don't I treat it as a random sampling process? This is the condition. I will not assume this a random sample on gpa. Because you told me what is gpa. So it is not random with respect to GPA, but it may be random. Now, once again, I want to emphasize, I used a what may. So please don't sue me if it's not right. But they will at least be a good data point to test whether this is independent things. So all of these are little tricks. But these are all little teeny weeny tricks that the optimizer always use to try to get.
  >
  > 假设我想测试年龄和部门是否独立。当我回答这个问题时，我会测试它:$\sigma_{(gpa < 3.5)} (Student)$ ，因为这个查询与年龄和部门无关。所以我得到的结果应该是独立的。
  >
  > 所以收集了大量的统计数据。因为无论如何你都会收到元组。假设有人问你一个关于gpa的问题，你会返回一堆元组一堆元组返回，希望现在再一次，你可以很容易地说，其他什么都不用做。这与部门无关。这和两岁没有关系。希望它们都是随机分布的。他们说你无论如何都要检索这些元组为什么不使用这些元组来估计统计呢我不需要查看整个表，不需要不断更新某些东西这就是我说的捎带。显然，天下没有免费的午餐。如果你背东西，那意味着很多，你花时间回答这个问题。这也会减慢速度。这是一种取舍，但很常见。存钱罐是每个系统都使用的技术。我必须给你这些元组，为什么不把它当作一个随机抽样过程呢?这就是条件。我不会假设这是gpa的随机样本。因为你告诉我什么是gpa。所以GPA不是随机的，但它可能是随机的。现在，我再强调一次，我用的是什么。所以如果不对请不要起诉我。但它们至少是一个很好的数据点来检验它们是否独立。所有这些都是小技巧。但这些都是优化器总是试图获得的一些小技巧。
  
* Disjunction: 
  
  析取
  $$
  \sigma_{\theta_1 \vee \theta_1 \vee...\vee \theta_n}(r)
  $$
  Estimated number of tuples:
  $$
  n_r \times (1-(1-\frac{s_1}{n_r})\times(1-\frac{s_2}{n_r})\times ... \times (1-\frac{s_n}{n_r}))
  $$
  
  > And once again, assuming independence, what do you do?
  >
  > $\sigma_{(age \leq 13) OR (dept = ''cs'')}$
  >
  > Because you have two polls that satisfy both conditions. If you just do a plus, you had a choice.
  
  如前所述, $\frac{s_i}{n_r}$ 代表某元组满足条件$\theta_i$ 的概率. 元组满足整个析取式的概率为1减去元组不满足任何一个条件的概率.
  
* **Negation:** 
  
  取反
  $$
  \sigma_{\lnot\theta}(r)
  $$
  
  
  Estimated number of tuples:
  $$
  n_r -size(\sigma_\theta(r))
  $$
  





### ==16.3.3 Join Operation: Running Example== ✅

> How do you estimate Joy? Selectivity is a important issue because why? 
>
> For example, you have $A \Join B \Join C$ which joint do I do first can play a very significant difference. You probably want the first joint to eliminate as many tuples as possible. You probably do not want your first joint to generate a lot of tuples because that will make your second joint potentially much longer.  I don't care if that's a nested loops joint or merge. So here, estimate the size of each joint become a very, very interesting question. Now, on the other hand, the challenge is it's not that easy. There are a lot of situation make things complicated. Let's say we have 5000 students.
>
> 你如何估计快乐?选择性是一个重要的问题，因为为什么?
>
> 例如，你有$A \Join B \Join C$我先做哪个连接可以发挥非常显著的差异。你可能希望第一个联合尽可能多地消除元组。您可能不希望您的第一个关节生成大量元组，因为这将使您的第二个关节可能更长。不管它是嵌套循环还是合并循环。估计每个关节的大小就成了一个非常非常有趣的问题。现在，另一方面，挑战是这并不容易。有很多情况使事情变得复杂。假设有5000名学生。

Running example: 
$$
student \Join takes
$$
Catalog information for join examples:

* $n_{student} = 5,000$

  >  we have 5000 students.

* $f_{student} =50$, which implies that $b_{student} = \frac{5000}{50} = 100 (pages)$

  > we have 50 students per page, totally 100 pages

* $n_{takes} = 10000$

  > we have 10,000 takes.

* $f_{takes} = 25$ , which implies that $b_{takes} = \frac{10000}{25}=400 (pages)$

  > we have 25 takes per page, totally 400 pages

* $V(ID, takes) = 2500$, which implies that on average, each student who has taken a course has <u>taken 4 course.</u>

  * Attribute $ID$ in takes is a foreign key referencing student.
  * $V(ID, student) = 5000 (primary \ key!)$

> Student(ID, ...)
>
> Takes(stu_ID, course_ID, .... ) basically means what I want installed, what classes each student take, or now, we don't care that in this example we don't care about it. For now, we'll just focus on this ID Join. 
>
> 基本上是指我想安装什么，每个学生上什么课，现在，我们不关心在这个例子中，我们不关心它。现在，我们只关注这个ID联结。
>
> $V(ID, student) = 5000$ 
>
> How about this $V(ID, take)$, Id itself is not the primary key. It is only part of a primary key, So you don't know. Let's say the database I've estimated is small you and come up with 2500. All you can say is that a student on average is taking 4 courses. o this is where we're going to start. And then we're slowly building things.
>
> 那么这个$V(ID, take)$， ID本身不是主键。它只是主键的一部分，所以你不知道。假设我估计的数据库很小，你得到了2500个。你只能说一个学生平均上4门课。我们从这里开始。然后我们慢慢地建造东西。



### ==16.3.3 Estimation of the Size of Joins==

> Homework2

* The Cartesian product $r\times s$  contains $n_r•n_s$ tuples; each tuple <u>occupies $s_r + s_s$ bytes.</u>

  笛卡尔积$r\times s$包含$n_r•n_s$元组;每个元组占用$s_r + s_s$

  > remember, a Join is a Cartesian product followed by a selection
  >
  > ```sql
  > select *
  > from student_take
  > ```
  >
  > This just the product of .
  >
  > the size of the output can be tricky because you really have to see what the star in Select dies. What attributes do you want to get? What projection do you want to do? Because if you just do a start, that means what you had to pull in. Because if you just do a start, that means what?
  >
  > Each tuple in the result is the combination of all the attributes of the two tables, which will be a larger tuple than either of the table itself. That means the blocking factor is going to be smaller. You're only going to see even smaller pages, smaller tuples, fewer tuples in each page because each item will become larger. So just by saying 100 times 400 is a bit dangerous. Number of coupons that debt is generated versus number of pages that need to store. When you talk about the number of pages you need to store the two poles, then what is the size of each tuple matters?
  >
  > 这就是乘积。
  >
  > 输出的大小可能很棘手，因为你必须看到Select中的星号终止了什么。你想要什么属性?你想做什么投影?因为如果你只是开始，那就意味着你必须拉进来。因为如果你只是开始，那意味着什么?
  >
  > 结果中的每个元组是两个表所有属性的组合，它将比两个表本身的元组更大。这意味着阻塞因子会变小。你只会看到更小的页面，更小的元组，每个页面中的元组更少，因为每个项目会变得更大。所以说100乘以400有点危险。债务产生的优惠券数量与需要存储的页面数量。当讨论需要存储两个极点的页数时，每个元组的大小很重要

* If $R\cap S  = \varnothing$, then $r\Join s$ is the same as $r\times s$.

* If $R\cap S$ is a key for $R$, then a tuple of $s$ will join with at most one tuple from $r$

  * therefore, the number of tuples in $r\Join s$ is no greater than the number of tuples in $s$.

    > Let's say $R\Join_{R.a=S.b} S$ and if $a$ is a primary key or unique value of $R$ What does it mean?
    >
    > Each tuple in S, How many tuples in R can join with?  One or zero. 
    >
    > But then that at least tells you what the number of tuples in the result is not going to be more than size of S. The number of tuple s that's already give you up about.
    >
    > 我们设$R\Join_{R.a=S。b} S$，如果$a$是$R$的主键或唯一值，这意味着什么?
    >
    > S中的每个元组，R中有多少个元组可以进行联结操作?1或0。
    >
    > 但这至少告诉你结果中元组的数量不会超过s的大小，元组s的数量已经让你放弃了。

* If $R\cap S$ in $S$ is a **==foreign key==** in $S$ referencing $R$, then the number of tuples in  $R\Join S$ is exactly the same as the number of tuples in *s.*

  如果$S$中的$R\cap S$是引用$R$的$S$中的一个**==外键==**，则$R\Join S$中的元组数量与$S$中的元组数量完全相同

  * The case for $R\cap S$ being a foreign key referencing $S$ is symmetric.

    $R\cap S$作为引用$S$的外键是对称的
    
    > Now be a bit careful about foreign key. 99.9% of the time when you decide database, you're foreign always referring to a primary key. There is a 0.01% chance that it's not. There are some weird database design situation where you do want to be a foreign key relationship, but it doesn't get the two one. It's not necessary. Primary key. It seldom happen. It does happen. So when you when you offer up guarantees, you want to be careful whether you're referring to a primary key or not. 
    >
    > If not primar key means that each tuple may not match with more than one thing. It must match with at least one thing. But it may not be because they may be difficult enough.  So that's something. You have to be careful. 
    >
    > 现在要小心使用外键。当你决定使用哪个数据库时，99.9%的情况下，你总是引用主键。有0.01%的可能性不是。有一些奇怪的数据库设计情况，你想要一个外键关系，但它不能得到两个1。没有必要。主键。这种情况很少发生。它确实发生过。所以当你。当你提供保证时，你要小心你引用的是否是主键。
    >
    > 如果不是主键，则每个元组不能与多个元素匹配。它必须与至少一个东西匹配。但这可能不是因为它们可能足够困难。这很重要。你必须小心。

* In the example query $student \Join takes$,  `ID` in  $takes$ is a foreign key referencing $student$

  在示例中，查询$student \Join takes$为参数，中的`ID` 是指向student的外键

  * hence, the result has exactly $n_{takes}$ tuples, which is 10000
  
    > Now, no question now because ID is the primary key now and you a foreign key in so that's another. Obviously if it makes sense and if it is correct you should try to define. You can set things unique you should do. If you want to set thing as a foreign key, you should do. It will be good if your function actually refer to a primary key, which is once again 99.9% of the time needed all the time in the Relation model.
    >
    > 毫无疑问，因为ID是主键，而in是外键，这是另一个。显然，如果它是有意义的，如果它是正确的，你应该尝试定义。你可以设置一些你应该做的独特的事情。如果你想把thing设置为外键，就应该这么做。如果你的函数确实引用了一个主键，那就更好了，在关系模型中，99.9%的时间都需要用到主键。



??? ?????

> Now here thing goes dicey.
> $$
> R\Join_{R.a=S.b} S
> $$
> Neither `a` or `b` is key, a is not a key of R , b is not key of S, and neither a or b is unique. What do I do? Now things become dicey, right? Each tuple can join with zero, one or more tuples on the other side, and there's no guarantee that.
>
> So for example, this tuple may join with seven tuples now.  but these people may join with zero tuples in that. That's at least if I don't give you any more information. There's no there's nothing you can do about that. There's nothing very specific that you can do in this previous case, but we can still do something about it.
>
> Now. Let's say there's no foreign key relations. But you do assume you're willing to assume that every vlalue of B will appear in the a, So every tuple in S, `S.b` will appear in table R. But that's no guarantee that Table R is unique. What do you do? What was the best you can do? Once again, in this case, if you don't have any more information, you should assume some kind of uniformity.
>
> So let's say this is R.a, This S,b .   There is value a in` S.b`. So I know a must be here. I just don't know how many A's are there.
>
> `a`和`b`都不是键，`a`不是R的键，`b`也不是S的键，`a`和`b`都不是唯一的。我该怎么办?现在事情变得危险了，对吧?每个元组可以与另一端的0个、1个或多个元组进行联结，而且不能保证这一点。
>
> 例如，这个元组现在可以连接7个元组。但这些人可能会加入零元组。至少在我不给你更多信息的情况下。没有你对此无能为力。在前面的例子中，你不能做什么具体的事情，但我们仍然可以做一些事情。
>
> 现在。假设没有外键关系。但是你假设B的每个值都会出现在a中，所以S中的每个元组都是。b '会出现在表R中，但这并不能保证表R是唯一的。你是做什么的?你能做到最好的是什么?同样，在这种情况下，如果你没有更多的信息，你应该假设某种均匀性。
>
> 我们设这是R.a，这是S b。在` S.b`中有值a。所以我知道a一定在这里。我不知道有多少个A。
>
> ![Screenshot 2022-11-02 at 02.56.43](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-11-02 at 02.56.43.png)
>
> So I need to estimate how many A's are there. We felt anything more. And you willing to assume the authority was the. Expectation. What's the selectivity here? You go back and look at the number of this thing value of V(A, d). If there are a hundred listing value of a in R, then you assume the number of tuples that where you'll pay is going to be 1% of the tuples in table R. And they say this is 10,000 to polls. 1% will be hundred tuples.
>
> 我需要估计有多少个A。我们有了更多的感觉。你愿意认为权威是。期望。这里的选择性是多少?你回头看看V(A, d)这个东西的数量，如果R中有100个A的列表值，那么你假设你要支付的元组的数量将是表R中元组的1%他们说这是10 000到民意调查。1%是100个元组。

* If $R\cap S = {A}$ is not a key for $R$ or $S$.
  If we assume that every tuple $t$ in $R$ produces tuples in $R$  $S$  the number of tuples in $R \Join S$  is estimated to be:
  
  如果我们假设$R$中的每一个元组$t$产生$R$ $S$中的元组，则$R \Join S$中的元组数量估计为:
  $$
  \frac{n_r*n_s}{V(A,s)}
  $$

  > And neither angel is unique. Now what do I do?

  If the reverse is true, the estimate obtained will be:
  $$
  \frac{n_r*n_s}{V(A,r)}
  $$
  The lower of these two estimates is probably the more accurate one.

* Can improve on above if histograms are available
  
  如果直方图可用，可以改进上述情况吗
  
  * Use formula similar to above, for each cell of histograms on the two relations 
  
    使用类似于上面的公式，对于两个关系上的直方图的每个单元格

* Compute the size estimates for $depositor \Join customer$ without using information about foreign keys:
  $$
  V(ID, takes) = 2500, and \ V(ID, student) = 5000
  $$
  The two estimates are $5000*\frac{10000}{2500} = 20,000$ and $5000 * \frac{10000}{5000} = 10000$

  <u>We choose the lower estimate, which in this case, is the same as our earlier computation using foreign keys.</u>

  >```sql
  >select * 
  >from A, B
  >f
  >```
  >
  
  



### 16.3.4 Size Estimation for Other Operations

* Projection: estimated size of $\prod_A(r) = V(A,r)$

* Aggregation: estimated size of $_G \gamma_A (r) = V(G,r) $

* Set operations
  *  For unions/intersections of selections on the same relation: rewrite and use size estimate for selections
    * E.g. $\sigma_{\theta_1}(r) \cup\sigma_{\theta_2}(r)$ can be rewritten as $\sigma_{\theta_1 \ or \ \theta_2}(r)$
    
  * For operations on different relations:
    * estimated size of $r \cup s = size \ of \ r +size\ of \ s$
    * estimated size of $r\cap s = minimum \ size \ of \ r \ and \ size \ s$ 
    * estimated size of $r-s=r$
    * <u>All the three estimates may be quite inaccurate, but provide upper bounds on the sizes.</u>
    
    
  
* Outer join:
  * Estimated size of $r ⟕ s = size \ of \ r \Join s + size \ of \ r$
    * Case of right outer join is symmetric
  * Estimated size of $r⟗ s = size\  of \ r\Join s + size \ of \ r + size \ of \ s $ 





### 16.3.5 Estimation of Number of Distinct Values

Selections:
$$
\sigma_\theta (r)
$$

* if $\theta$ forces A to take a specified value: $V(A, \sigma_{\theta}(r)) = 1$.

  * e.g. A= 3

* If $\theta$ forces A to take on one of a specified set of values:

  $V(A, \sigma_\theta(r)) = number \ of \ specified\ values$

  * e.g $A = 1 \vee A=3 \vee A=4$

    > return 3

* If the selection condition $\theta$ is of the form $A \ op \ r$ estimated $V(A, \sigma_\theta(r))=V(A.r)*s$

  * where $s$ is the selectivity of the selection.

    > $op$ 为一个比较运算符

* In all the other cases: use approximate estimate of $min(V(A,r),n_{\sigma\theta(r)})$

  * More accurate estimate can be got using probability theory, but this one works fine generally.



Joins:
$$
r \Join s
$$

* If all attributes in $A$ are from $r$ estimated $V(A, r\Join s) = min(V(A,r), n_{r\Join s})$

* If $A$ contains attributes $A_1$ from $r$ and $A_2$ from s, then estimated
  $$
  V(A,r\Join s)= min(V(A_1, r) *V(A_2-A_1, s), V(A_1-A_2,r)* V(A_2, s), n_{r\Join s})
  $$

  > 有些属性可能在$A_1$中又在$A_2$中, $A_1 - A_2$ 和 $A_2 - A_1 $ 分别指来自$r$和只来自$s$的A中的属性.

* More accurate estimate can be got using probability theory, but this one works fine generally





* Estimation of distinct values are straightforward for projections

  * They are the same in $\prod_{A}(r)$ as in $r$

* The same holds for grouping attributes of aggregation.

* For aggregated values

  * For $min(A)$ and $max(A)$, the number of distinct values can be estimated as $min(V(A,r), V(G,r))$ where $G$ denotes grouping attributes
  * For other aggregates, assume all values are distinct, and use $V(G,r)$

  

### ~~16.4.4 Optimizing Nested Subqueries**~~

> Leave this .

* Nested query example:

  ```sql
  select name
  from instructor
  where exists (select * 
               		from teaches
               		where instructor.ID = teaches.ID and teaches.year = 2019)
  ```

* SQL conceptually treats nested subqueries in the where clause as functions that take parameters and return a single value or set of values

  * Parameters are variables from outer level query that are used in the nested subquery; such variables are called **==correlation variables==**

* Conceptually, nested subquery is executed once for each tuple in the cross-product generated by the outer level from clause

  > SQL（在概念上)按以下方式执行整个查询：首先计算位于外层查询的from 子句中的关系的笛卡儿积，然后对结果中的每个元组用 where 子句中的谓词进行测试。在上述的例子中，就是测试子查询运算结果是否为空。

  * Such evaluation is called **==correlated evaluation==**

  * Note: other conditions in where clause may be used to compute a join (instead of a cross-product) before executing the nested subquery

    > SQL 优化器尽可能地试图将嵌套子查询转换成连接的形式.

  

* Correlated evaluation may be quite inefficient since 

  * a large number of calls may be made to the nested query 

  * there may be unnecessary random I/O as a result

    
    

* SQL optimizers attempt to transform nested subqueries to joins where possible, enabling use of efficient join techniques

* E.g.: earlier nested query can be rewritten as 
  $$
  \prod_{name}(instructor \Join_{instructor.ID = teaches.ID \wedge teaches.year =2019}teaches)
  $$

  > ```sql
  > select name
  > from instructor, teaches
  > where instructor.ID = teaches.ID and teaches.year=2007
  > ```

* Note: the two queries generate different numbers of duplicates (why?)

  * Can be modified to handle duplicates correctly using semijoins

  

????? ❓

* The semijoin operator $⋉$ is defined as follows

  * A tuple $r_i$ appears $n$ times in $r ⋉_\theta s$ if it appears $n$ times in $r$, and there is at least one matching tuple $s_i$ in $s$

* E.g: earlier nested query can be rewritten as 
  $$
  \prod_{name} (instructor ⋉_{instructor.ID \wedge teaches.year =2019 }teaches)
  $$

  * Or even as: $\prod_{name}(instructor ⋉_{instructor.ID} (\sigma_{teaches.year =2019 }teaches)$)

  * Now the duplicate count is correct!

  


* The above relational algebra query is also equivalent to 

  ```sql
  from instructor
  where ID in (select teaches.ID
              from teaches
              where teaches.year = 2019)
  ```



* This could also be written using only joins (in SQL) as 

  ```sql
  with t1 as         
  	(select distinct ID
     from teaches
     where year = 2019)
  select name
  from instructor, t1
  where t1.ID = instructor.ID
  
  ```

* The query

  ```sql
  select name 
  from instructor 
  where not exists (select *
                   from teaches
                   where instructor.ID = teaches.ID and teaches.year = 2019)
  ```

  can be rewritten using the anti-semijoin operation as $\bar ⋉$
  $$
  \prod_{name}(instructor \bar ⋉_{instructor.ID = teaches.ID \wedge teaches.year=2019}teaches)
  $$
  

In general, SQL queries of the form below can be rewritten as shown

* Rewrite:

  ```
  select A
  from r1,r2,...,rn
  where P1 and exists (select *	
                       from s1, s2, ..., sm
                       where P^1_2 and P^2_2)
  ```
  
* To : $\prod_A(\sigma_{p_1}(r_1 \times r_2 \times ... \times r_n)⋉_{P_2^1} \sigma_{P_2^1}(S_1 \times S_2 \times ...\times S_m))$

  * $P_2^1$ contains predicates that do not involve any correlation variables
  * $P_2^2$ contains predicates involving correlation variables

* The process of replacing a nested query by a query with a join/semijoin (possibly with a temporary relation) is called decorrelation.

* Decorrelation is more complicate in several cases, e.g. 

  * The nested subquery uses aggregation, or 
  * The nested subquery is a scalar subquery

* Correlated evaluation used in these cases



### Decorrelation 

* Decorrelation of scalar aggregate subqueries can be done using groupby/aggregation in some cases

  ```sql
  select name
  from instructor
  where 1 < (select count(*)
            	from teaches
            	where instructor.ID = teaches.ID
            				and teaches.year = 2019)
  ```

  
  $$
  \prod_{name} (instructor ⋉_{instructor.ID = TID \wedge 1cn}(_{ID\ as\ TID }\gamma_{count(*) \ as cnt}(\sigma_{teaces.year = 2019}(teaches))))
  $$
  
  
  





## Quiz 4

Which of the following about the parse tree notation of a query is correct?

(a) Each node can have at most 2 children

(b) The leaves corresponds to tables

(c) For nested loop, the right child is the inner loop.

A. (b) and (c) 

B. (a) and (b)

C. (b)

D. (a), (b) and (c) ✅

 

Which of the following about pipeline/materialization is correct?

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
> ![Screenshot 2022-10-29 at 20.44.48](/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Screenshot 2022-10-29 at 20.44.48.png)
>
> (b)左深树的一个优点是可以沿着树的整个左路径进行流水线。
>
> 左深连接顺序用于流水线计算特别方便, 因为右操作对象是一个已存储的关系, 每个连接只有一个输入来着流水线.





## Quiz 5

Consider the first part of a multi-table query r1$\Join$ r2 (with the join condition r1.a = r2.a). Which of the following will make sort-merge a potential best-case scenario?

(a) At the end the tuples needed to be ordered by r1.a

(b) There is a subsequent join with the condition r1.b - r3.b

(c) There is a subsequent join with the condition r1.a - r3.c

a. c ✅

> a 属性sort - merge 之后是ordered. 所以需要该属性ordered就是答案
>
> (a) 需要a属性ordered 所以 是
>
> (b) 这里的condition都是关于b属性, 所以a属性的ordered 没有半毛钱关系
>
> (c) 这里的a是order的所以有助于condition 中 a属性的利用



Consider joining to table A and B with the condition A.a = B.b, and A.a is the primary key of A. Which of the following statement(s) is/are correct?-

(a) If A.a is the primary key of A, then the result cannot have more tuples than the number of tuples in A

(b) If A.a is the primary key of A, then the result cannot have more tuples than the number of tuples in B

(b) ✅

> 因为a是primary key 所以不可以重复, 它只能有唯一, 因而table A 有n个tuples, 那么A.a 就只有ntuples
>
> 而b不是primary key 所以可以重复, 所以如果table b是n个, 那么B.b的tuples数量大于等于n
>
> 所以当A和B要连接的时候, 数量会多, 这个标准则以B为准.
>
> <img src="./Chapter 16 Query Optimization.assets/sql-join.png" alt="sql-join" style="zoom:50%;" />





Which of the following statements is/are correct?

(a) Equi-width histograms are better than equi-depth histograms to capture skew in data

(b) Suppose in a equi-width histogram there is an entry from 21.0-30.0 with frequency 100. Assuming uniformity, the best guess of number of items between 22.0 - 26.0 is 50.  

My answer: (a)(b) ❌

Correct: (b) ✅

> (a) 等宽直方图比等深度直方图更能捕捉数据中的倾斜 ❌
>
> Equi-depth histograms are better than equi-width histograms to capture skew in data 
>
> <img src="/Users/eve/Desktop/CS7330_Database/Notes/Chapter 16 Query Optimization.assets/Chp16 Query Optimization -14.jpg" alt="Chp16 Query Optimization -14" style="zoom: 50%;" />
>
> (b) 假设在等宽直方图中有一个从21.0到30.0的条目，频率为100。假设均匀，在22.0 ~ 26.0之间的物品数量的最佳猜测是50。
>
> ✅
>
> 



