Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
abs(-10)
10
a = abs
a(-10)
10
a
<built-in function abs>
import math
b = math.sqrt
b(25)
5.0
def simple(x, y):
    return x(y)

simple(math.sqrt, 25)
5.0
def sample():
    return abs

x = sample()
x
<built-in function abs>
y = sample
y()
<built-in function abs>
funs = [abs, math.sqrt, type, len]
funs[1](25)
5.0
funs[-1](funs)
4
nums = ['20', '30', '40', '50']
newNums = list(map(int, nums))
newNums
[20, 30, 40, 50]
s1 = '123456789'
list(map(int, s1))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
names = ('Dom', 'Kevin', 'Priya', 'Henry')
def up(a):
    return a.upper()

upNames = tuple(map(up, names))
upNames
('DOM', 'KEVIN', 'PRIYA', 'HENRY')
s1 = 'abc1234xyz897'
def sample(x):
    if x.isdigit():
        return int(x)
    else:
        return x

    
list(map(sample, s1))
['a', 'b', 'c', 1, 2, 3, 4, 'x', 'y', 'z', 8, 9, 7]
def odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

    
list(filter(odd, [1, 2, 3, 4,5,6,7,8,9]))
[1, 3, 5, 7, 9]
def odd(n):
    if n % 2 == 1:
        return True
    else:
        return True

    
list(filter(odd, [1, 2, 3, 4,5,6,7,8,9]))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
emails = ['a@hotmail.com', 'b@gmail.com', 'c@gmail.com', 'd@yahoo.com']
def gmail(email):
    if email.endswith('gmail.com'):
        return True

    
list(filter(gmail, emails))
['b@gmail.com', 'c@gmail.com']
def gmail(email):
    if email.endswith('gmail.com'):
        return False

    
list(filter(gmail, emails))
[]
from functools import reduce
def sample(x, y):
    return x+y

reduce(sample, [1, 2, 3, 4, 5, 6, 7, 8, 9])
45
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
((((10+20)+30)+40)+50)
150
def sample(x, y):
    return x+y/2

reduce(sample, [10, 20, 30, 40, 50])
80.0
10+20/2
20.0
20+30/2
35.0
35+40/2
55.0
55+50/2
80.0
def sample(x, y):
    return x+y

sample = lambda x, y:x+y
sample(20, 30)
50
x = reduce(lambda x, y:x+y, [10, 20, 30, 40, 50])
x
150
gmails = list(filter(lambda email:email.endswith('gmail.com')), emails)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    gmails = list(filter(lambda email:email.endswith('gmail.com')), emails)
TypeError: filter expected 2 arguments, got 1
emails
['a@hotmail.com', 'b@gmail.com', 'c@gmail.com', 'd@yahoo.com']
gmails = list(filter(lambda email:email.endswith('gmail.com'), emails))
gmails
['b@gmail.com', 'c@gmail.com']
#     lambda <args>: expression
