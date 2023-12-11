**Programming Homework 2 – (Strict) Two-phase locking**

Due Date: Dec 8th 11:59pm (with late pass for 48 hours only)

For this program, you are to implement a version of (strict) two-phase locking. You can use either C++ or python to implement the project.

对于这个程序，要实现(严格的)两阶段锁。你可以使用c++或python来实现这个项目。

We first describe the various parts of the program

我们首先描述程序的各个部分 

**Database** 数据库

To make thing simple, the database contains a list/array of integers. They will be referred to by its position in the list/array (e.g. integer 0, integer 15 etc.)

简单来说，数据库包含一个整数列表/数组。它们将通过其在列表/数组中的位置引用(例如整数0，整数15等)。

You will be provided with a database class with the following methods (we use db[k] to denote the k-th integer of the database).

你将被提供一个具有以下方法的数据库类(我们使用db[k]来表示数据库的第k个整数)。

Constructor:构造函数:

- Database(int k, bool nonzero): Create a database that store k integers. If nonzero = true, then db[i] is initialized to i+1, else all db[i] = 0

  Database(int k, bool nonzero):创建一个存储k个整数的数据库。如果nonzero = true，则db[i]初始化为i+1，否则所有db[i] = 0

  

Methods: 方法

- int Read(int k): Return the db[k] (notice that the number is referenced from 0 to k-1)

  int Read(int k):返回db\[k](注意数字是从0到k-1的引用)

- void Write(int k, int w): Set db[k] = w.

  void Write(int k, int w):设置db[k] = w

- Void Print(): Display the content in the database.

   Void Print():显示数据库中的内容

You are NOT allowed to modify the Database class.

不允许修改数据库类

```python
class Database:
    data = [] 
    def __init__(self, k: int, nonzero: bool):
        if nonzero:
            for i in range(k):
                self.data.append(i + 1)
        else:
            for i in range(k):
                self.data.append(0)
    def Read(self, k: int):
        return self.data[k]
    def Write(self, k: int, w: int):
        self.data[k] = w
        return
    def Print(self):
      	print(self.data)
        return self.data
```





> You have to implement a lot. Manager class. Which is his name using the same convention name. Please follow all the convention here. So you have a lot. Manage a class, you create a log manager. I will basically manage all the locks on the actual database. You have to figure out you. You will decide how. What's the data structure and what's the parameter you positive constructor. They'll leave it for you to decide on it that mainly to have these commands you can request a lock on an item. So that's the request method. That's a request that for you. Basically the transaction. Tidey will request a lock on the object K. And you tell them why there is a share lock on an exclusive lock. And do you have in a command to release the all the locks that hold by transaction. So that is and then I also want you to have a method that actually show me all the locks. Show me your talents and and you return basically which object which is locked by which transaction, this kind of stuff and you basically repossess. So in C++ you return as a check to appears so for each object. So basically a wealth of odd objects for each entry, basically which transaction on it. Oh. Actually to by transaction idea. So. And then you also have to implement a transaction class. Basically, each object of a transaction clerk respond to a transaction. You have to declare the key local variables. And then. You do all the operations I mentioned, the reading, the writing, the editing does multiplying. the copying a combination and then to have a display method so that you can display what the local rebels of all these. Okay. And then you have to write the main program, as we mentioned. Your main program should look like this. Uh, I'm right. I'm writing the C++ version of it. You should do something. Correspondent In Python or in Java or whatever other high level language you run the program, you should run it in my line, hope. You should never problem the user to offer anything new to the user. Expect to for what? All the parameters when you run the program. If you if you cancel your program, you ask the use of for some pay at the top the points of your brain.  You should get it and use it the simple way, not being in a full blown crash. It's not your fault. Okay. All right. So the complete parameter, the first parameter is the number of items in the database. Well, you didn't know how big your database is, so you need to specify that. And then each subsequent item is the name of a file that stored a transaction. That's not a transaction. So my program may be something like this.
>
> `./a.out 10 + 1.txt + 2.txt + 3.txt + k.txt + ...`
>
> So you type in one line by Conway. This `1.txt`will be treated as transaction one. This `2.txt`will be transaction two. This will be transactions three. This will be transaction four. So on of. Okay. Right now, the format of each fund, each of the transactions file has the foreign form in the first line with a two numbers. The first number is tell you how many instructions are there. The second number will tell you how many local variables are unique, and then each of the subsequent line will be combined. So five So let me create a transaction file right in front of you so I can't have a transaction file.
>
> The first line will be five four. That means these five tell you there will be five lines. Each line will be compatible. Okay. I will say Rete and I have Falco. Bravo. Read one three. And then we'll add frequently. And then we will copy to free. And then we will write one too. We will write to write, actually write to one and I'll write three. So this will be reading the first. I come on the database. Story in local wearable number three for that transaction. Story in local wearable number three for that transaction. And then I will add 20 to the first wearable, the first or the first local wearable. I will copy the first local wearable to the second local variable. I will write the second local variable into the first item on the database and I'll write the value of the first low corriveau into the second value of the database. So that will be one file look like this. You don't need to check for syntax correctness. Now you should be. If the theme text is correct, you should be able to read it.
>
> ![Screenshot 2022-11-18 at 01.34.12](./Programming Homework 2 – (Strict) Two-phase locking.assets/Screenshot 2022-11-18 at 01.34.12.png)
>
> If the syntax is row and your program crash. You are not responsible. If it referred to a local rebel database object as our rate. You're not responsible either. Okay. I want I want to minimize the error checking because once again, I don't want to get bogged down by the scope. So you can you can write this program assuming the user will behave in giving you the right transaction files. If the user give you the wrong format and your program crash, you are not responsible. Okay there no point to be taken off of that this. Okay then if you are to output, there is certain things I want you to output and I'll leave it up to you to to read that. A couple of, a couple of other things that are implementation that I want to highlight. When a transaction write an item to a database, they need to change a database immediately. Okay. So there's no buffers, basically. A transaction commits immediately after the last comment is executed.

### Lock Manager

This is a object that is used to maintain all the locks that is held by various transactions. All lock requests have to be made through the lock manager.

这是一个对象，用于维护各种事务持有的所有锁。所有的锁请求都必须通过锁管理器进行。

Your lock manager should have the following methods: Constructors:

你的锁管理器应该有以下方法:构造函数:

- LockManager(...) : Create a new lock manager. (You are to determine what parameters need to be passed to)

  LockManager(…): 创建一个新的锁管理器。(你需要确定需要传递给哪些参数)

  
  

Methods

- `Int Request(int tid, int k, bool is_s_lock)`; where tid is the transaction id, k is the -k-th integer of the database where the lock is requested; is_s_lock is true if the request is for a S-lock, otherwise it is for an X-lock. Return 1 if lock is granted, 0 if not.

  `Int Request(Int tid, Int k, bool is_s_lock)`;其中tid是事务id, k是请求锁的数据库的第k个整数;如果请求是S-lock, is_s_lock为true，否则是X-lock。如果授予锁，则返回1，否则返回0

- `Int ReleaseAll(int tid)`: release all the locks that is held by transaction tid. Return the number of locks released

  `Int ReleaseAll(Int tid)`:释放事务tid持有的所有锁。返回已释放锁的数目.

* `vector<pair<int, bool> > ShowLocks(Int tid)`: return all the locks that is being held by transaction tid. For C++ you should return a vector of pairs, each <int, bool> pair contains the item to be locked, and whether it is a S-lock (true) or a X-lock (false).
   For Python, you should return a list of tuples, where each tuple has the same format as the pairs specified above.
   
   `vector<pair&lt;int, bool> > ShowLocks(Int tid)`: 返回事务tid持有的所有锁。对c++来说，你应该返回一个由对组成的向量，每个对都是&lt;int, boolean &gt;pair包含要锁定的项，以及它是S-lock (true)还是X-lock (false)。
   
   对于Python，你应该返回一个元组列表，其中每个元组的格式与上面指定的对相同。

You are to implement this class and add new methods if you want.

你需要实现这个类并添加新的方法。



### Transaction 事务

Each transaction is a list of commands that read from and write to the database. It also contains a set of local variables (integers) that the transactions can manipulate.

每个事务都是读取和写入数据库的命令列表。它还包含一组事务可以操作的局部变量(整数)。

You should create a Transaction class, with the following method defined (we use local[m] to denote the m-th local variable):

你应该创建一个事务类，定义如下方法(我们使用local[m]来表示第m个局部变量):

Constructors:

构造函数: 

* `Transaction(int k)`: Create a transaction with k local variables (reference from 0 to k-1)

  `Transaction(int k)`:使用k个局部变量创建一个事务(从0到k-1的引用)



Method

方法:

  - `void Read(Database& db, int source, int dest)`: Read the source-th number from the database and copy it local[dest]

    `void Read(Database& db, int source, int dest)`从数据库中读取source-th数字并复制到本地[dest]

  - `void Write(Database& db, int source, int dest)`: Write the value of the local[source] from the to the dest-th number in the database.

    `void Write(Database& db, int source, int dest)`: 将本地[source]的值从数据库中的最大数写入数据库

  - `void Add(int source, int v)`, `void Mult(int source, int v)`: set `local[source] = local[source] – v` and `local[source] = local[source] * v` respectively

    `void Add(int source, int v)`, `void Mult(int source, int v)`:分别设置 `local[source] = local[source] – v` 和 `local[source] = local[source] * v` 

  - `void Copy(int s1, int s2)`: set `local[s1] = local[s2]`

    `void Copy(int s1, int s2)`: 设置 `local[s1] = local[s2]`

  - `void Combine(int s1, int s2)`: set `local[s1] = local[s1] + local[s2]`

    `void Combine(int s1, int s2)`: 设置`local[s1] = local[s1] + local[s2]`

  - `void Display()`: Display all local variables’ value. You should list all the numbers on the same line,

    with one space between each of them.

    `void Display()`显示所有局部变量的值。你应该把所有的数字列在同一行上, 它们之间有一个空格。

You may need/want to store more info and provide more methods for the transaction class. You are welcomed to do that.

你可能需要/想要存储更多的信息并为transaction类提供更多的方法。欢迎你这样做。



**Main Task of the program**

Your program should run using the following command (assume you compile your C++ program to a.out):

`../a.out <number of items in database> < file 1> < file 2> ... <transaction file n>`

Where `<number of items in database>` is a positive number to denote the number of items in the database; and `<file 1> ,, <file n>` is the name of a set of files, each of them is a transaction.

DO NOT print a prompt and ask the user for input. Each file corresponds to a list of commands for a transaction. In terms of numbering, the first file should corresponds to T0, the second file T1 etc. Each file has the following format:

你的程序应该使用以下命令运行(假设你将c++程序编译为a.out):

`../a.out <number of items in database> < file 1> < file 2> ... <transaction file n>`

其中`<number of items in database> `是一个正数，表示数据库中的项目数;和 `<file 1> ,, <file n>` 是一组文件的名称，每个文件都是一个事务。

不要打印提示并要求用户输入。每个文件对应于一个事务的命令列表。在编号方面，第一个文件对应于T0，第二个文件对应于T1等。每个文件的格式如下:

- The first line is two numbers. The first number is the number of instructions for the transaction. The second number is the number of local variables for that transaction.

  第一行是两个数字。第一个数字是事务的指令数。第二个数字是该事务的局部变量的数量。

- Each subsequent line is an instruction. Each instruction contains three words, the first is a letter, which denote the operator, and the next two are numbers are the operands. The list of instructions are as follows (x,y, d are all integers):

  后面的每一行都是一条指令。每条指令都包含3个单词，第一个是字母，表示运算符，接下来的两个是数字，是操作数。指令列表如下(x、y、d都是整数):
  
  * R x y–read db[x] and store it to local[y]
  * W x y–write local [x] to db[y]
  * A x d–local[x] = local[x] + d
  * M x d–local[x] = local[x] * d
  * C x y–local[x] = local[y]
  * O x y–local[x] = local[x] + local[y]
  * P x y–print the current elements in the database(x,y are ignored)
  
  

Your main program will have one database object, and then read in all the transaction files and create one transaction each. Then you should “run” all transaction using the following loop:

主程序将有一个数据库对象，然后读入所有事务文件，并为每个文件创建一个事务。然后你应该使用以下循环“运行”所有事务:

  ```
  While (there are transactions still not finished)
     Check if all transactions are blocked (see below), 
     if so,
   	 					print “Deadlock” and quit 
   	 otherwise
  						Randomly pick one of the transactions (it’s ok to pick blocked transaction) 
  	 Try executing the next instruction of that transaction*
  ```

> so what your program is supposed to do is to read the set of files. Each file will have come out like this. And then you're going to simulate. Obviously notice that it's obviously possible for multiple transaction to access the same item. That means you will now have to incorporate your locking protocol. Notice that the transaction doesn't tell you when to lock, when to unlock. You have to figure that out. You have to ensure this is strict two phase locking. What is two phase locking? You only unlock. Once you unlock, you cannot start locking it. So basically, as you mention, what you do is your main program should be look something like this. Your main office before this main loop, you have to open to open the transaction files and I'll show you the form. I'll show you the format and how to do it in a minute. After that, you are basically going to run this loop, checking whether there is some transaction, who hasn't finished, and then checking whether there is a deadlock. We will do it. Very, very simple minded. Definitely check of that lot if there's a deadlock. Quick. I don't even need you to resolve the deadlock. If there's a deadlock, you just quit, okay? If there's no deadlock, then randomly pick one on the transaction and randomly. And then once you pick that transaction, try to execute the next operation. Notice that the next operation might be you might have to wait, that that operation may not be executable. For instance, if you want to write an item from a database and that's already the exclusive level on it. Obviously you cannot proceed and you just simply tell the system, hey, you have to wait and you have to wait. And also, once again, to make life simple, you can even select a transaction that's waiting and try to execute a command again. And if we have any solution out of the way again, that's perfectly fine. Okay. I purposely do it to make things simple for you to program in real life. You probably want to do something fancier, but want to keep it very simple. Relatively straightforward. Okay.



A few points of notes:

几点注意事项:

  - You are required to request the corresponding locks before executing a command

    在执行命令之前，您需要请求相应的锁

  - If a transaction wants to read an item from the database and later on write that item, request

    an S-lock first, and then request the X-lock

    如果事务想从数据库中读取一个项，然后再写入该项，请求先申请s锁，再申请x锁

  - Whenever a transaction writes an item to the database, it needs to change the database immediately

    每当一个事务将一个项目写入数据库时，它需要更改立即数据库

  - A transaction commits immediately after the last command is executed. All locks are released at

    that moment.

    事务在最后一个命令执行后立即提交。所有锁在那一刻被释放

    > All lots are released at that moment. So it's transaction successful to execute or to command an immediate committed and immediate release the locks.

  - Every time you try to execute an instruction, you should print the following like

    `T<transaction id> execute <instruction> <k>`

    

    `T<transaction id> execute <instruction> <k>`

    Where `<instruction>` is the instruction to be executed (together with its parameter), and k is the k-th instruction of that transaction. You print this line every time you attempt to execute that instruction ✅

    其中`<instruction>`是要执行的指令(及其参数)，k是该事务的第k条指令。每次尝试执行这条指令时，都打印这一行

  - If a transaction requests a lock, after printing the previous line, you print the statement `T<transaction id> request <S/X>-lock on item <item number> : G/D`Where G (granted) / D (denied) correspond to whether the lock is granted or not. ✅

    如果事务请求锁，在打印上一行之后，打印语句`T<transaction id> request <S/X>-lock on item <item number> : G/D`
    
    其中G(授予)/ D(拒绝)对应于锁是否授予。 
    
  - We do not have a wait queue for locks. Whenever a request is denied, the system will simply pick another transaction (maybe the same one) to execute. (It is ok if the same transaction is picked multiple times and the request is denied every time).

    我们没有锁的等待队列。每当请求被拒绝时，系统将简单地选择另一个事务(可能是相同的事务)来执行。(如果同一个事务被选中多次，并且每次请求都被拒绝，这是没有问题的)。

- We do not do any deadlock management. We check for deadlocks using a simplified algorithm: 

  我们不做任何死锁管理。我们使用简化的算法检查死锁:

  * For each transaction we keep a Boolean variable (name “blocked”) to check if the current instruction is blocked (because of a denied lock request). We initially set all these variables to false. Whenever a transaction is blocked, they set “blocked” to true. However, whenever a transaction is allowed to proceed, the “blocked” variables in ALL transactions are set to false. Whenever all non-finished transactions have the “blocked” variable set to true, then a deadlock occurs.

    对于每个事务，我们保存一个布尔变量(名称“blocked”)来检查当前指令是否被阻塞(因为拒绝锁请求)。我们首先将所有这些变量设置为false。每当事务被阻塞时，他们将" blocked "设置为true。然而，只要允许事务继续进行，所有事务中的“blocked”变量都被设置为false。当所有未完成的事务都将“blocked”变量设置为true时，就会发生死锁。

  When a deadlock is detected. The system should print “Deadlock” and exit the program.

  当检测到死锁时。系统应该打印“死锁”并退出程序

  > As I mentioned, we don't do fancy thing to check for deadlocks. We do something relatively simple, not totally accurate. But once again, I want the programing to be simpler. Each transaction should have a variable block associated with it. Initially, it will be set forth and whenever you execute a command from a transaction and end up have to wait, you change that variable into true. However, if another transaction were able to execute a command, you set all the block variable to force. So you assume that by a other transaction exit of income unsuccessfully. It will unblock everything in real life. After this, if that's not true. But it will be the simplest way for you to call it. Once again, I want this to be simple that lock detection is not the main theme for this project. So we'll do a very loosey goosey thing. Okay. And then. But you can also be assured if the block ramble in all the trials that can actually be finished is set to true that you know definitively.
  >
  > Okay. You are not required to do anything fancy. I believe this should be the simplest way for you to code that. No detection, no cycle checking, no whatever. Now it will be not efficient because just a just because in command, execute, execute command doesn't mean anything is unblocked. But you know what? Let's keep it simple. Let's make your coding simple. Because this is not the time to do the tests. Yes.
  >
  > Like they are able to check that, but that will mean like 50 more lines of code. And I don't want you to. I want you to be optimistic here. Okay. But then you have about three weeks. Three weeks. I don't want to put too much, but you. You have a project to finish. I'll rather cut a lot of fat down, because the key thing for this project is for you to do, to face, like, really for you to to figure out how to do two things. A simulation of two things like not the whole deal of two things like yes, the separation between the words or the numbers is correct. Space is a blank space you can assume, yeah, don't dispense me, but don't assume how many friends space I did. Okay. So if you are in Python's split with your thesis that you are in C++, uh, formatted really best. What actors seeing you should be noticed that each the first two numbers each other like three numbers, free items. That's it. You know exactly what the format is and you w where a value diploma is not correct, you are not responsible.

- If all transaction finishes, you should call the Print() method for the database to print the value, and then exit the program.

  如果所有事务完成，您应该调用数据库的Print()方法来打印值，然后退出程序

  > You should if you have, you can print the statements, whatever before you had in this couple in all your debugging statements. Okay. Where you having the program? I do not want to go into a program and come all of debugging statements. Okay. So make sure by the time you come in, all what I want you to output is the only thing you open for.

- Notice that the output specified should be the ONLY statements that is printed out. (Except for the P x y command where the database is printed) Each statement should be printed on a separate line. The amount of space between words does not matter. It is likely I will write a program to check whether your output is correct. The program should be able to handle variable number of spaces between characters but otherwise the output has to be as stated.

  注意，指定的输出应该是唯一打印出来的语句。(除了打印数据库的P x y命令)每条语句都应该打印在单独的一行上。单词之间的空间大小并不重要。我可能会写一个程序来检查你的输出是否正确。程序应该能够处理可变数量的字符之间的空格，但否则输出必须像声明的那样。



**What to hand in**

You need to hand in a copy of your source code ONLY. You should have comment in your source code to denote how to compile and run the program.

你只需要提交一份源代码的副本。源代码中应该有注释，表示如何编译和运行程序。

You would implement deadlock avoidance using the wait-die rule specified in the slides. So when a transaction request a lock and cannot obtain it, there is a possibility that it will need to rollback. A few things of note:

使用幻灯片中指定的wait-die规则来实现避免死锁。因此，当事务请求锁但无法获得锁时，就可能需要回滚。有几点需要注意:

- Transactions that are rolled back are NOT restarted.

  回滚的事务不会重新启动

- If a transaction has to abort, you should print the line

  `T<transaction id> rolled back`

  如果事务必须中止，则应该打印该行

  `T<transaction id> rolled back`

- Since a write instruction require immediate update of the database, thus there is a possibility that updated values need to be rolled back. You are responsible to set up the process of rolling back transactions.

  由于写指令需要立即更新数据库，因此可能需要回滚更新过的值。您负责设置回滚事务的过程。

- You may want to implement new methods for the LockManager class to make your live easier.

  你可能想实现LockManager类的新方法，让你的生活更轻松。

- The main program logic should be the same as the main part, However, you are not required to

  reuse the same code of your main program (as you see fit).

  主程序逻辑应该与主部分相同，但是，你不需要这样做重用主程序中的相同代码(视情况而定)。

> There's a bonus. We are going to talk about doing a lot in this class. I want you to implement one of those method in your extra credit. As I say, if I allow you to go in groups of two, I'll probably cut down on the bonus you can get if you do it.

You should write a separate program for the bonus code (but you are free to reuse any code from your base case).

你应该为额外代码编写一个单独的程序(但你可以自由地重用基线条件中的任何代码).

>  The key thing is that the transaction won't tell you where to lock. You have to figure that out. And that's the only thing that is tricky. And even there is not that tricky. Okay, so. 



### Test

DB = [1, 2, 3]			L

```
4 3								  4条指令 3 t local 变量 3   l = [0,1,2]
R 1 1             	D = [1, 2,3]  d[1]=2  ->  l[1] = 1 -> 2    d=[1, 2,3]    l = [0, 2, 2]
R 2 2								d[2] = 3     l = [2] = 2-> 3       d =[1, 2, 3]     l = [0,2,3]
O 2 1								l[x] = l[x] + l[y]   l[2] = l[2] + l[1] = 3+2=5     l = [0,2,5]
W 2 2               l[2]  -> db[2]     db[2] = l[2] = 5    d = [1,2,5]     l = [0,2,5]
```





DB = 

```
6 3
R 0 0
M 0 2
R 1 1
A 1 4
W 1 1
W 0 0
```



DB =

```
5 3
R 0 0
A 0 1
M 0 -1
O 1 0
W 1 0
```



DB=[1,2,3]    L = [0, 1, 2]

```
3 3            3条指令   local 变量 3
R 2 2					 l[2] = d[2] = 3    l=[0,1,3]       
M 2 3					 l[2] = 3 * 3 = 9   l =[0,1,9]
W 2 2          d[2] = l[2] = 9      d= [1,2,9]
```
