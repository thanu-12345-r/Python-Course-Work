Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(5,10,15,20)
print(t)
(5, 10, 15, 20)
print(t[2])
15
print(-3)
-3
print(-3)
-3

print(t(-3))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(t(-3))
TypeError: 'tuple' object is not callable
print(t[-3])
10
s=("Thanmai","Mohana","Rojasri")
print(s[1:3])
('Mohana', 'Rojasri')
print(s[3:1])
()
print(s[1:2])
('Mohana',)
c=(1,2,3,4,5)
d=(6,7,8,9,10)
print(c+d)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
g=(a,e,i,o,u*4)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    g=(a,e,i,o,u*4)
NameError: name 'a' is not defined
g=(a,e,i,o,u)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    g=(a,e,i,o,u)
NameError: name 'a' is not defined
c=(1,2)
print(c*2)
(1, 2, 1, 2)
e=("Usha sri","Thanmai","pujitha","Navya")
print(rojasri in e)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(rojasri in e)
NameError: name 'rojasri' is not defined
e=("Usha sri","Thanmai","pujitha","Navya")
print("Thanmai" in e)
True
>>> print("Renuka" not in e)
True
>>> print("Usha sri " not in e)
True
>>> c=(4,8,12,16)
>>> print(c(8))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(c(8))
TypeError: 'tuple' object is not callable
>>> c=(4,8,12,16)
>>> c=(4,8,12,16)
>>> my_tuple=(1,2,3)
>>> a,b,c=my_tuple
>>> print(a,b,c)
1 2 3
>>> r=(1,3,5,3,5,4,1,6)
>>> r.count(1)
2
>>> a=("Mohana","Thanmai","Rojasri")
>>> a.index(1)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.index(1)
ValueError: tuple.index(x): x not in tuple
>>> a.index(0)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.index(0)
ValueError: tuple.index(x): x not in tuple
>>> len(a)
3
>>> s=(2,4,6,8,10)
>>> max(s)
10
>>> min(s)
2
>>> sum(s)
30
