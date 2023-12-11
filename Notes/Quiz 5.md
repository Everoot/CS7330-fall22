# Quiz 5

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
> <img src="https://tva1.sinaimg.cn/large/008vxvgGgy1h85suz560sj30qu0l4q5w.jpg" alt="sql-join" style="zoom:50%;" />





Which of the following statements is/are correct?

(a) Equi-width histograms are better than equi-depth histograms to capture skew in data

(b) Suppose in a equi-width histogram there is an entry from 21.0-30.0 with frequency 100. Assuming uniformity, the best guess of number of items between 22.0 - 26.0 is 50.  

My answer: (a)(b) ❌

Correct: (b) ✅

> (a) 等宽直方图比等深度直方图更能捕捉数据中的倾斜 ❌
>
> Equi-depth histograms are better than equi-width histograms to capture skew in data 
>
> <img src="https://tva1.sinaimg.cn/large/008vxvgGgy1h85sgsj322j30u012r40e.jpg" alt="Chp16 Query Optimization -14" style="zoom: 50%;" />
>
> (b) 假设在等宽直方图中有一个从21.0到30.0的条目，频率为100。假设均匀，在22.0 ~ 26.0之间的物品数量的最佳猜测是50。
>
> ✅



Which of the following about atomicity for transaction is/are correct?

(a) ﻿﻿﻿﻿It means that a transaction, once started, must finish

(b) ﻿﻿﻿﻿It means that operations between different transaction cannot interleave

Neither(a) and (b) ✅

>* ==**Atomicity** (原子性): All or nothing== 
>
>* i.e. : Either all operations of the transaction are properly reflected in the database or none are.
>
>  事务的所有操作都正确地反映在数据库中，或者一个都没有。
>
>* Implications
>
>  * If the system crashes in the middle of a transaction T, when the system restarts, *before any user can use the database* again, the DBMS must ensure either
>    * T is finished
>    * T never started
>
>* Which do you think is easier? Make more sense?
>
>(a) ❌ a transaction does not have to once started and then must finish. because during the process it may encounter some bad problem, the the transaction is allowed to roll back.
>
>(b) ❌ it can have interleave operation. like serializability.  Concurrency schedule. 





In terms of transaction processing, why do DBMS need to have mechanisms to ensure durability?

A. The statement is false. Durability is always automatically maintained.

B. Updated value may get rollback if transactions aborts

C. Updated value is always flushed to the disk immediately (even before the transaction commits)

D. Updated value by a transaction may still remains in the buffers in main memory after transaction commits.

B ❌

D ✅

> * ==**Durability(持久性)** : Once committed, changes to database must be persistent==
>
>   一旦提交，对数据库的更改必须是持久的
>
> * i.e. : After a transaction completes successfully, the changes it has made to the database persist, even if there are system failures. 
>
>   事务成功完成后，即使有系统故障，它对数据库所做的更改也会保留。
>
>   > Now, I'm not saying that another transaction can overwrite your result. I'm not saying that. I'm just saying that if this trans and you can think of this as example.
>
> * Implications:
>
>   * Suppose a transaction commits, and then the system crashes. When the system restarts, *before any user can use the database* again, the DBMS must ensure that the changes made by this transaction is stored onto the disk.
>
>     假设提交了一个事务，然后系统崩溃。当系统重新启动时，在任何用户可以再次使用数据库之前，DBMS必须确保此事务所做的更改存储在磁盘上。
>
> * ==Why is this not automatically the case? ❓==
>
>   > Buffer.
>
> > Now question why can you disappear in the first place?
> >
> > I can choose to write the tuples in the buffer and wait for the system to swap the buffer into the this. And the system can crash at that moment. Remember Murphy's Law. Anything that can go wrong will go wrong at the worst possible time. Right. So once again, the good news is not your problem is the database problem.
> >
> > 现在问你为什么一开始就能消失?
> >
> > 我可以选择将元组写入缓冲区，并等待系统将缓冲区交换到this。系统可能在那一刻崩溃。记住墨菲定律。任何可能出错的事情都会在最糟糕的时候出错。正确的。再一次，好消息不是你的问题而是数据库的问题。
>
> A. ❌ The durability is no automatically maintained. Because when you automatically some information especailly when you update something, these thing when you automatically, and they are in the buffer, and at the same time the power break. Everything gone. You have to save in the disk.
>
> B. ❌ 所以 然后呢? 撤回了相当于没有更改 还没有commit的那块 答非所问
>
> C. ❌ not before commits





Consider 2 transaction T1 and T2, with a database Which of the following pairs of transaction is in conflict?

(a) ﻿﻿﻿﻿T1 Read(X), T2 Write(X)

(b) ﻿﻿T1 Read(X), T2 Write(Y)

(c)﻿﻿﻿﻿ T1 Write(Y), T2 Write(Y)

ac ✅

> 当$I$与$J$是不同事务在相同的数据项上的操作, 并且其中至少有一个是write指令时, 我们说$I$与$J$是冲突(conflict)的.
>
> (a) ✅对于T2的Write(X)的先后会影响  T1Read(X)的会不同 所以顺序重要 从而在conflict
>
> (b) ❌ T1 和 T2 对于不同的数据项进行操作, 所以不冲突
>
> (c) ✅T1 写和T2写 Y, 它俩的写的先后顺序, 会导致 下一次读取Y的进行影响 所以顺序重要, 从而存在conflict.



Which of the following about conflict serializability is correct?

(a) If a schedule is conflict serializable, it can be transformed into a serial schedule (by swapping adjacent operations in the schedule)

(b) A schedule that is NOT conflict serializable will never produce the same result as a serial schedule of the same set of transactions.

My answer: (a) (b)❓❌

Correct answer: a ✅

> 由冲突等价的概念引出了冲突可串行化的概念: 若一个调度S与一个串行调度冲突等价, 则称调度S是冲突可串行化(conflict serializable)的. 那么, 因为schedule 3 冲突等价于serial schedule 1, 所以schedule 3 是冲突可串行化(conflict serializable)
>
> Conflict serializability: a schedule S is conflict serializable if it is conflict equivalent to a serial schedule
>
> (a) ✅ 就是conflict serializability 的定义的另一种表达. conflict serializable -> serial schedule 就是判定是否为conflict serializability 的方法
>
> (b) 不可冲突序列化的调度永远不会与使用同一组事务的串行调度产生相同的结果 ❌ 有可能  p -> q ✅ 但你不能说 非 p -> 非 q.
>
> <img src="https://tva1.sinaimg.cn/large/008vxvgGgy1h85uz2g8koj30ne0ayt9j.jpg" alt="Screenshot 2022-11-15 at 01.45.02" style="zoom:33%;" />
>
> 有可能会产生相同的结果, 但不能保证所有的.
