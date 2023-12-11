# Run this file
# python3 program2_wait_die.py <number of items in the database> <file 1> <file 2> ...
import random
import sys
from collections import deque
from typing import Deque

# ✅
class Database:
    data = []  # 需共享属性

    # Create a database that store k integers. If nonzero = true, then db[i] is initialized to i+1, else all db[i] = 0
    def __init__(self, k: int, nonzero: bool):
        if nonzero:
            for i in range(k):
                self.data.append(i + 1)
        else:
            for i in range(k):
                self.data.append(0)

    # Return the db[k] (notice that the number is referenced from 0 to k-1)
    def Read(self, k: int):
        # print("The value of index " + str(k) + " of db is: "+ str(self.db[k]))
        return self.data[k]

    # Set db[k] = w
    def Write(self, k: int, w: int):
        self.data[k] = w
        # print("The value of index " + str(k) + " write to:" + str(self.db[k]))
        return

    # Display the content in the database
    def Print(self):
        print(self.data)
        return self.data


# DB = Database(2, True)
# DB.Print()
# DB.Write(0, 100)
# DB.Write(1, 200)
# DB.Print()
#
# DB2 = Database(2, False)
# DB2.Print()


# ✅
# Each transaction is a list of commands that read from and write to the database.
# It also contains a set of local variables (integers) that the transactions can manipulate.
# You should create a Transaction class, with the following method defined
# (we use local[m] to denote the m-th local variable)
class Transaction:
    # Create a transaction with k local variables (reference from 0 to k-1)
    def __init__(self, k):
        self.local = []
        self.commands = []
        for i in range(k):
            self.local.append(i)  # t1, t2, t3

    # Read the source-th number from the database and copy it local[dest]
    def Read(self, data: Database, source: int, dest: int):
        self.local[dest] = data.Read(source)
        print("Read data[" + str(source) + "] and copy it to local[" + str(dest) + "]", end = " ")

    # Write the value of the local[source] to the dest-th number in the database.
    def Write(self, data: Database, source: int, dest: int):
        data.Write(dest, self.local[source])
        print("Write value of the local[" + str(source) + "] to data[" + str(dest) + "]", end = " ")

    # set local[source] = local[source] – v   ❓
    def Add(self, source, v):
        self.local[source] = self.local[source] + v
        print("local[" + str(source) + "] = local[" + str(source) + "] + " + str(v), end = " ")

    def Sub(self, source, v):
        self.local[source] = self.local[source] - v
        print("local[" + str(source) + "] = local[" + str(source) + "] - " + str(v), end = " ")

    # set local[source] = local[source] * v
    def Mult(self, source, v):
        self.local[source] = self.local[source] * v
        print("local[" + str(source) + "] = local[" + str(source) + "] * " + str(v), end = " ")

    # set local[s1] = local[s2]
    def Copy(self, s1, s2):
        self.local[s1] = self.local[s2]
        print("local[" + str(s1) + "] = local[" + str(s2) + "]", end = " ")

    # set local[s1] = local[s1] + local[s2]
    def Combine(self, s1, s2):
        self.local[s1] = self.local[s1] + self.local[s2]
        print("local[" + str(s1) + "] = local[" + str(s1) + "] + local[" + str(s2) + "]", end = " ")

    # Display all local variables’ value. You should list all the numbers on the same line,
    # with one space between each of them.
    def Display(self):
        local_list = map(lambda x: str(x), self.local)
        print(" ".join(local_list))

    # R x y / W x y / A x d / M x d/ C x y/ O x y/ P x y
    def Command(self, operator, num1, num2):
        self.commands.append([operator, num1, num2])

    def Finished(self):
        if len(self.commands) == 0:
            # print("Yes, finished")
            return True
        else:
            # print("Not finished yet")
            return False


# DB = Database(3, True) # d= [1,2,3]
# DB.Print()
# T = Transaction(3)     # l = [0, 1, 2]
# T.Display()
# T.Read(DB, 1, 1)  # l[1] = d[1] = 2    l = [0, 2, 2]
# T.Display()
# T.Read(DB, 2, 2)  # l[2] = d[2] = 3  l = [0, 2, 3]
# T.Display()
# T.Combine(2, 1)  # l[2] = l[2] + l[1] = 3+2=5 l=[0, 2, 5]
# T.Display()
# T.Write(DB, 2, 2) # l[2] =  5 ->  db[2] = 5   d=[1,2,5]    l=[0, 2, 5]
# T.Display()
# DB.Print()
# # A
# T.Add(0,2)    # l[0]= l[0] + 2 = 0 + 2 = 2 l =[2,2,5]
# T.Display()
# # M
# T.Mult(0,2)    # l[0] = l[0]*2 = 2 * 2 =4 l=[4,2,5]
# T.Display()
# # C
# T.Copy(1,0) # l[1] =l[0] =4 l=[4,4,5]
# T.Display()


# '''
# T1 = Transaction(2)
# print("T1.Display:")
# T1.Display()
# T1.Read(DB, 0, 0)
# print("T1 Read db[1]: X")     # A <-- Read(x)
# T1.Display()
# print("T1 Read db[2]: Y")
# T1.Read(DB, 1, 1)             # B <-- Read(y)
# print("T1.Display")
# T1.Display()
# T1.Command("r",0,0)
# print(T1.commands)
# '''


# Create a new lock manager. (You are to determine what parameters need to be passed to)
class LockManger:
    database_lock = {}
    transaction_lock = {}

    # database_lock {0: [1, 2]}  t1, t2 share the db[0]
    # transaction_lock = {0: [(k,true)]}  t0 has S-lock on db[k]   true: x-lock

    def __init__(self, DB: Database):
        database_lock_length = len(DB.data)
        for i in range(database_lock_length):
            self.database_lock[i] = []

    # where tid is the transaction id, k is the k-th integer of the database where the lock is requested;
    # is_s_lock is true if the request is for a S-lock, otherwise it is for an X-lock.
    # Return 1 if lock is granted, 0 if not.
    def Request(self, tid: int, k: int, is_s_lock: bool):
        if is_s_lock:  # request for a S-lock
            # whether x-lock on the transaction
            if self.check_x_lock(k, tid):  # true
                print("T" + str(tid) + " request S-lock on item " + str(k) + ": D")
                return 0  # not granted s lock
            else:  # no x-lock granted s lock
                self.database_lock[k].append(tid)
                self.transaction_lock.setdefault(tid, []).append((k, True))  # 1 have lock
                print("T" + str(tid) + " request S-lock on item " + str(k) + ": G")
                return 1
        else:  # false -> request for a X-lock -> during the process no other lock on these
            # whether x-lock on the transaction
            if self.check_lock(k, tid):  # check other whether you have lock on k
                print("T" + str(tid) + " request X-lock on item " + str(k) + ": D")
                return 0
            else:  # no x lock -> has s lock?
                if tid in self.database_lock[k]:  # current tid have the s lock on k -> x
                    for i, (j_k, z_slock) in enumerate(self.transaction_lock[tid]):
                        if j_k == k:
                            self.transaction_lock[tid][i] = (k, False)

                else:  # current tid have no lock on k
                    self.database_lock[k].append(tid)
                    self.transaction_lock.setdefault(tid, []).append((k, False))
                print("T" + str(tid) + " request X -lock on item " + str(k) + ": G")
                return 1

    def check_x_lock(self, k, tid):  # check like  X-lock(A) in the db
        transactions = self.database_lock[k]  # check db[k] lock
        for index, t_locks in enumerate(transactions):
            if tid != index:
                locks = self.transaction_lock[t_locks]
                for i, j in locks:
                    if not j:  # 0: x -lock => j: false  j:true: s-lock
                        return True
                    # else:                # 1: s -lock
                    #    return False
        return False

    # check T1 x lock on X

    # release all the locks that is held by transaction tid. Return the number of locks released
    def ReleaseAll(self, tid):
        if tid not in self.transaction_lock:  # the transaction not has locks
            return 0  # return the number = 0
        else:  # transation has locks
            release_number = len(self.transaction_lock[tid])
            del self.transaction_lock[tid]
            for k, locks_t in self.database_lock.items():
                if tid in locks_t:
                    locks_t.remove(tid)
                    self.database_lock[k] = locks_t
            return release_number

    # return all the locks that is being held by transaction tid. For C++ you should return a vector of pairs,
    # each <int, bool> pair contains the item to be locked, and whether it is a S-lock (true) or a X-lock (false).
    # For Python, you should return a list of tuples, where each tuple has the same format as the pairs specified above.
    def Showlocks(self, tid):
        lock_show = self.transaction_lock[tid]
        if tid in self.transaction_lock:
            return lock_show
        else:
            return []

    # S or X lock
    def check_lock(self, k, tid):
        for i in self.database_lock[k]:
            if i != tid:
                return True  # 1.other tids hold this item -> has lock but not tid.
            else:
                return False  # has lock


# # You are to implement this class and add new methods if you want.
# print("------------------")
# lock1 = LockManger(DB)
# print(lock1.database_lock)
# print(lock1.transaction_lock)
# print("----- ")
# lock1.Request(1, 0, True)  # T1: A <- read(x) ask s -lock   db[0] = x
# print("A <- read(x) ask s -lock")
# print(lock1.database_lock)
# print(lock1.transaction_lock)
# print("------- 1---")
# lock1.Request(1, 1, False)  # T1: B <- write(y) : ask X-lock db[1] = y
# print("T1: B <- write(y) : ask X-lock db[1] = y")
# print(lock1.database_lock)
# print(lock1.transaction_lock)
# print("----- ")
# print(lock1.check_x_lock(1, 1))
#
# lock1.Request(2, 1, False)  # T2: B <- write(y) : ask X-lock db[1] = y should be denied
# print(lock1.database_lock)
# print(lock1.transaction_lock)
#
# print(lock1.Showlocks(1))
#
# print(lock1.check_lock(1,1))
# print("----")
# print(lock1.ReleaseAll(1))

# read file add something in the database
# 3 3
# R 2 2
# M 2 3
# W 2 2
def create(db_k: int, file_list: list[str]):  # file_list: [t0,t1 ,t2 ,t3]
    DB = Database(db_k, True)
    T = []
    LM = LockManger(DB)
    for file in file_list:
        with open(file) as f:
            for i, j in enumerate(
                    f):  # i means line1, j means content j[0]:transactionsnumbers j[1]:local   i from 0   0: 2 2   1: R x y   2: W x y
                if i == 0:  # first line
                    j_content = j.strip().split(" ")
                    number_local_variable = int(j_content[1])
                    t = Transaction(number_local_variable)  # create instance
                else:
                    j_content = j.strip().split(" ")
                    operator = j_content[0]
                    num1 = int(j_content[1])
                    num2 = int(j_content[2])
                    t.Command(operator, num1, num2)
        T.append(t)
    return DB, T, LM


# t0
# 3 3
# R 2 2
# M 2 3
# # W 2 2
# file_list = ['t0','t1']
# A = create(3, file_list)
# DB = A[0]
# DB.Print()
# print(DB.db)
# print("---")
# T = A[1]    # object list
# print(type(T))
# for obj in T:
#     print(obj.local, sep = "")
#     print(obj.commands, sep= "")
#     print("---")
#
# print('---')
# L = A[2]
# print(L.database_lock)
# print(L.transaction_lock)
# t = list(T)[0]
# print("t:",t)
# t_commands = t.commands[0]
# print(t_commands)
# operator = t_commands[0]
# print(operator)
# # if operator[0] == 'R':
# #     s_lock = L.Request(0, t_commands[1], True)
# #     print(s_lock)


# def execute_each_command(DB: Database, t: Transaction, LM:LockManger, tid):
def execute_each_command(DB: Database, t: Transaction, LM: LockManger, tid, t_order: Deque[int]):
    commands_content = t.commands[0]
    operator = commands_content[0]
    num1 = commands_content[1]  # local
    num2 = commands_content[2]  # db
    if operator == 'R':
        s_lockr = LM.Request(tid, num1, True)
        if s_lockr == 1:
            t.commands.pop(0)  # time           t1            ->
            print("T" + str(tid) + " excute ", end="")
            t.Read(DB, num1, num2)
            if tid not in t_order:
                t_order.append(tid)
            else:
                t_order.remove(tid)
                t_order.append(tid)  # FIFO
            return 1
        else:
            wait_die(t_order, t, LM, tid, num1)

    elif operator == 'W':
        x_lockw = LM.Request(tid, num2, False)
        if x_lockw == 1:
            t.commands.pop(0)
            print("T" + str(tid) + " excute ", end="")
            t.Write(DB, num1, num2)
            if tid not in t_order:
                t_order.append(tid)
            else:
                t_order.remove(tid)
                t_order.append(tid)
            return 1
        else:
            wait_die(t_order, t, LM, tid, num2)

    elif operator == 'A':
        t.commands.pop(0)
        print("T" + str(tid) + " excute ", end="")
        t.Add(num1, num2)
        if tid not in t_order:
            t_order.append(tid)
        else:
            t_order.remove(tid)
            t_order.append(tid)
        return 1

    elif operator == 'S':
        t.commands.pop(0)
        print("T" + str(tid) + " excute ", end="")
        t.Sub(num1, num2)
        if tid not in t_order:
            t_order.append(tid)
        else:
            t_order.remove(tid)
            t_order.append(tid)
        return 1

    elif operator == 'M':
        t.commands.pop(0)
        print("T" + str(tid) + " excute ", end="")
        t.Mult(num1, num2)
        if tid not in t_order:
            t_order.append(tid)
        else:
            t_order.remove(tid)
            t_order.append(tid)
        return 1

    elif operator == 'C':
        t.commands.pop(0)
        print("T" + str(tid) + " excute ", end="")
        t.Copy(num1, num2)
        if tid not in t_order:
            t_order.append(tid)
        else:
            t_order.remove(tid)
            t_order.append(tid)
        return 1

    elif operator == 'O':
        t.commands.pop(0)
        print("T" + str(tid) + " excute ", end="")
        t.Combine(num1, num2)
        if tid not in t_order:
            t_order.append(tid)
        else:
            t_order.remove(tid)
            t_order.append(tid)
        return 1

    elif operator == 'P':
        t.commands.pop(0)
        print("T" + str(tid) + " excute ", end="")
        DB.Print()
        if tid not in t_order:
            t_order.append(tid)
        else:
            t_order.remove(tid)
            t_order.append(tid)
        return 1

    return 0

# wait_die
def wait_die(t_order: Deque[int], t: Transaction, LM: LockManger, tid, item):
    t_hold = LM.database_lock[item]
    t_hold = sorted(t_hold, key=lambda x: t_order.index(x))
    for i in t_hold:
        if i != tid:
            tj = i
            break

    if tid not in t_order:
        t_order.append(tid)
    else:
        t_order.remove(tid)
        t_order.append(tid)

    if not wait(t_order, tid, tj):
        print("T" + str(tid) + " rolled back", sep="")
        t.commands = []
        LM.ReleaseAll(tid)


def wait(t_order: Deque[int], ti, tj):
    i = t_order.index(ti)
    j = t_order.index(tj)
    if i < j:
        return True
    else:
        return False


def loading(T: list[Transaction]):
    for t in T:
        if not t.Finished():
            return True
    return False


if __name__ == '__main__':
    # print("yes")
    if len(sys.argv) < 2:
        raise 'Please using the following command: python3 program2_wait_die.py <number of items in the database> <file 1> <file 2>... <transaction file n>!'
    db_k = sys.argv[1]
    file_list = sys.argv[2:]
    instance = create(int(db_k), file_list)
    DB = instance[0]
    T = instance[1]
    LM = instance[2]
    t_order = deque([])
    k = {}
    for i in range(0, len(T)):
        k[i] = len(T[i].commands)
    while loading(T):
        t_index = random.randrange(0, len(T))
        t = T[t_index]
        if not t.Finished():
            execute_each_command(DB, t, LM, t_index, t_order)
            print("<" + str(k[t_index] - len(t.commands)) + ">")
        else:
            LM.ReleaseAll(t_index)
    DB.Print()
