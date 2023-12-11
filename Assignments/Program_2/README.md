# README

```python
class Databse:
 db = []
 def __init__(self, k: int, nonzero: bool):
 def Read(self, k: int):
 def Write(self, k: int, w: int):
 def Print(self):
  
  
class Transaction:
  local = []
  commands = []
  def __init__(self, k):
  def Read(self, db: Database, source: int, dest: int):
  def Write(self, Database, source, dest):
  def Add(self, source, v):
  def Mult(self, source, v):
  def Copy(self, s1, s2):
  def Combine(self, s1, s2):
  def Display(self):
  def Command(self, operator, num1, num2):
  def Finished(self):
    
    
class LockManger:
  database_lock = {}
  transaction_lock = {}
  def __init__(self, DB: Database):
  def Request(self, tid: int, k: int, is_s_lock: bool):
  def check_x_lock(self, k, tid):
  def ReleaseAll(self, tid):
  def Showlocks(self, tid):
  def check_lock(self, k, tid):
```



DB = [1, 2, 3]

​                         第一个数字代表有几个commands, 第二个代表有 local [0, 1 ,2]         

3	3									

R 	2	2             DB[2]=3    local[2] = 3    local [0, 1, 3]                

M	2	3			 local[2] * 3 = 3* 3 = 9     local [0, 1, 9]

W	2	2.           local[2] = 6          ->        db[2] = 9         db[1, 2, 9

]







T0 request S-lock on item 2: G
T0 execute read db[2] and store it to local[2]
T0 execute local[2] = local[2] * 3
T0 request X-lock on item 2: G
T0 execute write local[2] to db[2]
Database: [1, 2, 9]



T1

db[1 2 3]         local [0 1 2]

```
4 3
R 1 1      
R 2 2
O 2 1
W 2 2
```







T0 request S-lock on item 1: G ✅
T0 excute The value of index 1 of db is: 2
Read the Database[1] and copy it to local[1]
T0 request S-lock on item 2: G ✅
T0 excute The value of index 2 of db is: 3
Read the Database[2] and copy it to local[2]
T0 request S-lock on item 2: G ✅
T0 request S-lock on item 1: G
T 0 excute T0 request X -lock on item 2: G
T0 excute The value of index 2 write to:5
Write the value of the local[2] to the Database[2]
Display the content in the database:[1, 2, 5]





T0 request S-lock on item 1: G
T0 execute read db[1] and store it to local[1]
T0 request S-lock on item 2: G
T0 execute read db[2] and store it to local[2]
T0 execute local[2] = local[2] + local[1]
T0 request X-lock on item 2: G
T0 execute write local[2] to db[2]
Database: [1, 2, 5]





DB = [1, 2, 3]                     Local = [0,1,2]

```
6 3
R 0 0         DB = [1, 2,3]      L = [1,1,2]
M 0 2					D = [1, 2, 3]			 L = [2,1,2]
R 1 1         D = [1,2,3]        L = [2,2,2]
A 1 4					D = [1,2,3]        L = [2,6,2]
W 1 1					D = [1,6,3] 			 L = [2,6,2]
W 0 0 				D = [2,6,3]				 L = [2,6,2]
```

T0 request S-lock on item 0: G
T0 excute The value of index 0 of db is: 1
Read the Database[0] and copy it to local[0]
T0 request S-lock on item 0: G
T 0 excute local[0] = local[0] * 2
T0 request S-lock on item 1: G
T0 excute The value of index 1 of db is: 2
Read the Database[1] and copy it to local[1]
T0 request S-lock on item 1: G
T0 excute local[1] = local[1] - 4
T0 request X -lock on item 1: G
T0 excute The value of index 1 write to:-2
Write the value of the local[1] to the Database[1]
T0 request X -lock on item 0: G
T0 excute The value of index 0 write to:2
Write the value of the local[0] to the Database[0]
Display the content in the database:[2, -2, 3]



T0 request S-lock on item 0: G
T0 execute read db[0] and store it to local[0]
T0 execute local[0] = local[0] * 2
T0 request S-lock on item 1: G
T0 execute read db[1] and store it to local[1]
T0 execute local[1] = local[1] + 4
T0 request X-lock on item 1: G
T0 execute write local[1] to db[1]
T0 request X-lock on item 0: G
T0 execute write local[0] to db[0]
Database: [2, 6, 3]

```
5 9
R 0 0
A 0 1
M 0 -1
O 1 0
W 1 0
W 2 9
S 3 8
R 0 0
A 0 1
S 0 5
W 0 0
W 2 1
```





D = [1,2,3]				L = [0, 1, 2]

```
4 3
R 0 0        D = [1,2,3]			[1,1,2]
A 0 1				 A = [1,2,3]			[2,1,2]
S 0 5				 [1,2,3]					[-3,1,2]
W 0 0					W = [-3,2,3]
```







```
5 9
R 0 0
A 0 1
M 0 -1
O 1 0
W 1 0
W 2 9
S 3 8
R 0 0
A 0 1
S 0 5
W 0 0
W 2 1
```

T0 request S-lock on item 0: G
T0 excute Read the Database[0] and copy it to local[0]
T0 request S-lock on item 0: G
T0 excute local[0] = local[0] + 1
T0 request S-lock on item 0: G
T0 excute local[0] = local[0] * -1
T0 request S-lock on item 1: G
T0 request S-lock on item 0: G
T0 excute T0 request X -lock on item 0: G
T0 excute Write the value of the local[1] to the Database[0]
T0 request X -lock on item 9: G
T0 excute Write the value of the local[2] to the Database[9]
T0 request S-lock on item 3: G
T0 excute local[3] = local[3] - 8
T0 request S-lock on item 0: G
T0 excute Read the Database[0] and copy it to local[0]
T0 request S-lock on item 0: G
T0 excute local[0] = local[0] + 1
T0 request S-lock on item 0: G
T0 excute local[0] = local[0] - 5
T0 request X -lock on item 0: G
T0 excute Write the value of the local[0] to the Database[0]
T0 request X -lock on item 1: G
T0 excute Write the value of the local[2] to the Database[1]
Display the content in the database:[-5, 2, 3, 4, 5, 6, 7, 8, 9, 2]



T0 request S-lock on item 0: G
T0 execute read db[0] and store it to local[0]
T0 execute local[0] = local[0] + 1
T0 execute local[0] = local[0] * -1
T0 execute local[1] = local[1] + local[0]
T0 request X-lock on item 0: G
T0 execute write local[1] to db[0]
T0 request X-lock on item 9: G
T0 execute write local[2] to db[9]
T0 execute local[3] = local[3] - 8
T0 request S-lock on item 0: G
T0 execute read db[0] and store it to local[0]
T0 execute local[0] = local[0] + 1
T0 execute local[0] = local[0] - 5
T0 request X-lock on item 0: G
T0 execute write local[0] to db[0]
T0 request X-lock on item 1: G
T0 execute write local[2] to db[1]
Database: [-5, 2, 3, 4, 5, 6, 7, 8, 9, 2]









T1 request S-lock on item 1: G
T1 excute Read the Database[1] and copy it to local[1]
T1 request S-lock on item 2: G
T1 excute Read the Database[2] and copy it to local[2]
T1 request S-lock on item 2: D
T1 request S-lock on item 1: D
Deadlock
Display the content in the database:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]





T1 request S-lock on item 1: G
T1 execute read db[1] and store it to local[1]
T1 request S-lock on item 2: G
T1 execute read db[2] and store it to local[2]
T0 request S-lock on item 2: G
T0 execute read db[2] and store it to local[2]
T0 execute local[2] = local[2] * 3
T1 execute local[2] = local[2] + local[1]
T0 request X-lock on item 2: D
T1 request X-lock on item 2: D
Deadlock
Database: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]















T1 request S-lock on item 1: G
T1 excute Read the Database[1] and copy it to local[1]
T1 request S-lock on item 2: G
T1 excute Read the Database[2] and copy it to local[2]
T1 request S-lock on item 2: D
T1 request S-lock on item 1: D
Deadlock
Display the content in the database:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]







T1 request S-lock on item 1: G
T1 execute read db[1] and store it to local[1]
T1 request S-lock on item 2: G
T1 execute read db[2] and store it to local[2]
T1 execute local[2] = local[2] + local[1]
T1 request X-lock on item 2: G
T1 execute write local[2] to db[2]