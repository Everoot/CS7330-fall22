# Quiz 6

1. What is "two-phase" in two phase locking?

   A. None of the other answers are correct

   B. Once you start releasing locks you cannot obtain more locks

   C. Once you start acquiring X-locks, you cannot acquire S-locks

   D. Once you start acquiring X-locks, you cannot acquire S-locks

B ✅

> * **Ensure T1 does not read/write anything after releasing the lock!**
>
>   确保T1在释放锁后不再读写任何东西!
>
> * **===> (basic) Two-phase locking==**
>
>   (基本)两阶段锁定
>
> C.D  You can acquire S-locks after you start acquiring X-locks.



2. What is the motivation of having strict two-phase locking over basic two-phase locking?

   A. Strict two phase locking avoid non-recoverable schedule

   B. ﻿﻿Strict two phase locking require only one type of lock

   C. ﻿﻿Strict two phase lockng allow for more concurrency

   D. ﻿﻿All of the other answers are correct.

A ✅

> A. 
>
> * Strict 2-phase locking:
>
>   严格的两阶段锁
>
>   * 2-phase locking
>
>     两阶段锁
>
>   * ==X-locks can only== be released when the transaction commits
>
>     X-locks只能在事务提交时释放
>
> * Question: does strict 2-phase locking ensure 
>
>   问题:严格的两阶段锁是否能确保
>
>   * Recoverability? (Yes)
>
>     可恢复性?
>
>   * Avoid cascade aborts (Yes)
>
>     避免级联中止
>
>   * Strict? (Not quite)
>
>     严格吗?
>
> ❌B. it is based on basic on 2 phase lock, so it still have some limit on s-lock
>
> you unlock you can not add the other locks whatever s-lock.
>
> ❌C. more strict less concurrency



3. Consider deadlock avoidance in two-phase locking. Suppose Ti is holding a S-lock on an item, and then a transaction Tj request an X-lock on the same item. Which of the following is correct? (Assume i < j)

   A. ﻿﻿Tj will be allowed to proceed because i > j

   B. ﻿﻿Tj will be allowed to wait if "wait-die" policy is in place

   C. ﻿﻿Tj will be allowed to wait if "wound-wait" policy is in place

   D. ﻿﻿No matter what policy is used, Tj will abort

B ❌

C ✅

>A. ❌ Ti has not released the s-lock
>
>B. ❌ i < j means i older than j.  j wait for i means yonger transaction wait for older transactions 
>
>-> wound-wait
>
>C. ✅
>
>D. Tj can wait
>
>* Two options:
>
>  两个选项:
>
>  * ==Wait-die (non pre-emptive)==
>
>    Wait-die(非抢占式): 基于非抢占技术. 当事务Ti申请数据项当前被Tj持有, 仅当Ti的时间戳小于Tj的时间戳(即, Ti比Tj老)时, 允许Ti等待. 否则, Ti回滚(死亡)
>
>    * If $i<j$ then wait
>
>      如果 $i<j$ ，则等待
>
>    * else $T_i$ aborts
>
>      否则 $T_i$ 中止
>
>    例如, 假设事务T14, T15及T16的timestamps分别为5, 10, 15. 如果当前T14申请的数据项当前被T15持有, 则T14将等待. 如果T16申请的数据项被当前T15持有, 则T16讲回滚.
>
>  * ==Wound-wait (pre-emptive)==
>
>    伤口等待(先发制人):基于抢占技术, 与wait-die相反的机制. 当事务Ti申请的数据项当前被Tj持有, 仅当Ti的时间戳大于Tj的时间戳(即, Ti比Tj年轻)时, 允许Ti等待. 否则, Tj回滚(Tj被Ti伤害)
>
>    * If $i > j$ then wait
>
>      如果 $i > j$然后等待
>
>    * Else $T_j$ aborts
>
>      否则$T_j$终止
>
>    例如, 假设事务T14, T15及T16的timestamps分别为5, 10, 15. 如果当前T14申请的数据项当前被T15持有, 则T14将从T15抢占该数据项, T15将回滚. 如果T16申请的数据项被当前T15持有, 则T16讲回滚.
>
>* If i and j represent time (i.e. small number = older transactions)
>
>  如果i和j表示时间(即较小的数字=较早的事务)
>
>  * Wait-die: older transactions wait for younger transactions;
>
>    wait -die:旧事务等待新事务;
>
>  * Wound-wait: younger transaction wait for older transactions
>
>    Wound-wait:年轻事务等待旧事务

4. For recovery purpose, why do we need to have log an operation before executing it?

   A. ﻿﻿The statement is wrong, one shuld exeuction the opeartion before logging it

   B. ﻿﻿Otherwise many transactions will have to wait

   C. Otherwise we may not be aware of an operation being executed when the system restart

   D. Otherwise it is going to be less efficient

C ✅

> A. The statement is right, we have log an operation before executing it. 
>
> B. 无中生有, 只是为了出现bug的时候能够查找
>
> C. 是的, 为了重启的时候system 可以知道在重启前发生了什么, 在execute之后则会导致system重启的时候不知道刚才发生了啥
>
> D. 无中生有, 用小部分效率换取安全性 
>
> Thus logs must be **write-ahead logs** (WAL) 
>
> 因此，日志必须是**预写日志** (WAL)。
>
> * i.e. all operations must be logged first
>
>   即，必须首先记录所有操作
>
> * Log records must be forced to stable storage before actually operations can be executed
>
>   在执行实际操作之前，必须将日志记录强制存储到稳定存储中



5. Let say a transaction T holds an S-lock of an object. Which of the following statement(s) is/are true?

   (a) ﻿﻿﻿﻿If T wants to obtain an X-lock of the same object, it will be granted

   (b) If a different transaction T' want to obtain an S-lock on the same obiect, it will be granted

   (c) If a different transaction T' want to obtain an X-lock on the same object, it will be granted

   A. (a), (b) and (c)

   B. ﻿﻿(b)

   C. (a) and (b)

   D. (a)

C ❌

B ✅

> a. ❌  ==No other transaciton can hold any lock (not even a S-lock) if some transaction has an X-lock.==  Therefore you have to wait other release s-lock. then it will be granted.
>
> b. ✅ Multiple transactions can hold a S-lock on an object simultaneously.
>
> c. ❌ 同理于 a.
