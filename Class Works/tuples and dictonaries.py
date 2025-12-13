Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=()
t=tuple()
t=(1,2,3,4)
t
(1, 2, 3, 4)
t=(1,1,1,1,2)
t=(1,1.1,'string',[],(),{},{1,23})
t=((1,1),(2,2),(3,3))
t
((1, 1), (2, 2), (3, 3))
t=(1,2,3)
s=(2,3,4)
t+s
(1, 2, 3, 2, 3, 4)
t*s
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t*s
TypeError: can't multiply sequence by non-int of type 'tuple'
t*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 2, 3)
4 in t
False
1 in t
True
lang('java','python',','c','css','bootstrap')
     
SyntaxError: unterminated string literal (detected at line 1)
lang('java','python','c','c++','bootstrap')
     
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    lang('java','python','c','c++','bootstrap')
NameError: name 'lang' is not defined. Did you mean: 'range'?
a=1,2,3,4
     
a
     
(1, 2, 3, 4)
t=(1,2,3)
     
a,b,c=t
     
a
     
1
b
     
2
c
     
3
("dhanush","danush@gmail.com","dh@123")
     
('dhanush', 'danush@gmail.com', 'dh@123')
res[0]
     
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    res[0]
NameError: name 'res' is not defined
NameError: name 'res' is not defined
     
SyntaxError: invalid syntax

res=("dhanush","danush@gmail.com","dh@123")
 res[0]
     
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statement
     
SyntaxError: invalid syntax
x,y,z=[12,13,14]
     
x
     
12
y
     
13
z
     
14
t=(1,2,3,4,5)
     
sum(t)
     
15
t=(1,2,3,[4,5],6,7)
     
t[0]=1
     
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t[0]=1
TypeError: 'tuple' object does not support item assignment
t[3].append(9)
     
t
     
(1, 2, 3, [4, 5, 9], 6, 7)
t=({1,2},{3,4})
     
t[0]
     
{1, 2}
d={}
     
d={1:2,2:3,3:4}
     
2 in d
...      
True
>>> 4 in d
...      
False
>>> data={'name':'subash':'batchno':44,'course':'python full stack'}
...      
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
...      
SyntaxError: invalid syntax
>>> data={'name':'subash','batchno:44','course':'python full stack'}
...      
SyntaxError: ':' expected after dictionary key
>>> 
... data={'name':'subash','batchno':44,'course':'python full stack'}
...      
>>> data.get('dob')
...      
>>> data.setdefault('dob','12-12-2003')
...      
'12-12-2003'
>>> d={1:1,2:4,3:9,4:16}
...      
>>> d.setdefault(5,20)
...      
20
>>> d
...      
{1: 1, 2: 4, 3: 9, 4: 16, 5: 20}
>>> d={1:'int'}
...      
>>> d[1.1]='float'
...      
>>> d["str"]='string'
...      
>>> d["str"]='string'
...      
>>> d["str"]='string'
...      
