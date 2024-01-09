Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
cars = [20, 'Toyota', True, 'xyz', 20.5]
len(cars)
5
cars[3]
'xyz'
cars['xyz']
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    cars['xyz']
TypeError: list indices must be integers or slices, not str
ls1 = list(range(10, 20))
ls1
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
ls2 = [20, 30, 'abc', [30, 40, 50], True, 'xyz']
len(ls2)
6
ls2[4]
True
ls2[3]
[30, 40, 50]
ls3[3][1]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ls3[3][1]
NameError: name 'ls3' is not defined. Did you mean: 'ls1'?
ls2[3][1]
40
ls2 = [20, 30, 'abc', [30, 40, 50, [1,100, 300]], True, 'xyz']
ls2[3][2][2]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ls2[3][2][2]
TypeError: 'int' object is not subscriptable
ls2[3][3][2]
300
ls2[-1]
'xyz'
ls2[1:3]
[30, 'abc']
ls1
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
ls1[3:]
[13, 14, 15, 16, 17, 18, 19]
ls1[:5]
[10, 11, 12, 13, 14]
ls1[:]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
ls1[::2]
[10, 12, 14, 16, 18]
ls4 = [100, 20, 300]
ls1.extend(ls4)
ls1
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 20, 300]
ls1.append(ls4)
ls1
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 20, 300, [100, 20, 300]]
ls1.remove(16)
ls1
[10, 11, 12, 13, 14, 15, 17, 18, 19, 100, 20, 300, [100, 20, 300]]
ls1[-1]
[100, 20, 300]
ls1[-1].append(400)
ls1[-1]
[100, 20, 300, 400]
ls1
[10, 11, 12, 13, 14, 15, 17, 18, 19, 100, 20, 300, [100, 20, 300, 400]]
ls1[2] = 'abc'
ls1
[10, 11, 'abc', 13, 14, 15, 17, 18, 19, 100, 20, 300, [100, 20, 300, 400]]
100 in ls1
True
for i in ls1:
    i

    
10
11
'abc'
13
14
15
17
18
19
100
20
300
[100, 20, 300, 400]
type(ls1)
<class 'list'>
for i in ls1:
    type(i)

    
<class 'int'>
<class 'int'>
<class 'str'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'list'>
x = (20, 30, 40, [1, 2, 3])
x[-1]
[1, 2, 3]
x.append(200)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x.append(200)
AttributeError: 'tuple' object has no attribute 'append'
x[-1].append(400)
x
(20, 30, 40, [1, 2, 3, 400])
details = {'Name':'Dom', 'Age':40, 'Place':'Trumbull'}
len(details)
3
details['Name']
'Dom'
details['Occupation'] = 'Developer'
details
{'Name': 'Dom', 'Age': 40, 'Place': 'Trumbull', 'Occupation': 'Developer'}
details.get('Age')
40
details.get('Salary')
details['Salary']
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    details['Salary']
KeyError: 'Salary'
details.items()
dict_items([('Name', 'Dom'), ('Age', 40), ('Place', 'Trumbull'), ('Occupation', 'Developer')])

======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========
Traceback (most recent call last):
  File "C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py", line 3, in <module>
    f = open(path+'sample.txt', 'w')
PermissionError: [Errno 13] Permission denied: 'C:\\sample.txt'

======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========

======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========
Traceback (most recent call last):
  File "C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py", line 5, in <module>
    f = open(path+'sample.txt', 'w')
PermissionError: [Errno 13] Permission denied: 'C:\\sample.txt'
import os
path = 'C:\\'
os.access(path, os.W_OK)
True

======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========
Traceback (most recent call last):
  File "C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py", line 5, in <module>
    f = open(path+'sample.txt', 'w')
PermissionError: [Errno 13] Permission denied: 'C:\\Userssample.txt'

======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========
Traceback (most recent call last):
  File "C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py", line 5, in <module>
    f = open(path+'sample.txt', 'w')
PermissionError: [Errno 13] Permission denied: 'C:\\Users\\sample.txt'

======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========
Traceback (most recent call last):
  File "C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py", line 5, in <module>
    f = open(path+'sample.txt', 'w')
PermissionError: [Errno 13] Permission denied: 'C:\\Users\\sample.txt'

======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========
Change the path

======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========

======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========
This a sample file


======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========

======== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/textFiles.py ========

====== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class1_sample1.py =====
90

====== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class1_sample1.py =====
Traceback (most recent call last):
  File "C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class1_sample1.py", line 9, in <module>
    print(sample(80000, 16.5, 40))
  File "C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class1_sample1.py", line 5, in sample
    sol = a+b+c
NameError: name 'a' is not defined

====== RESTART: C:/Users/bolluk/AppData/Local/Programs/Python/Python310/class1_sample1.py =====
80056.5
help(sample)
Help on function sample in module __main__:

sample(a, b, c)
    This is a sample function with 2 parms

