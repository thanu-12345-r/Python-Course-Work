Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a={"apple","banana","cherry","apple"}
print(len(a))
3
c={"red","blue","green"}
c.add("orange")
print(c)
{'blue', 'orange', 'green', 'red'}
d={"thanmai","mohana","rojasri"}
e={"usha","pujitha","navya"}
d.update(e)
print(d)
{'mohana', 'pujitha', 'usha', 'rojasri', 'thanmai', 'navya'}
s={"dell","hp","lenovo"}
s.remove("hp")
print(s)
{'dell', 'lenovo'}
q={"cotton","silk","rayon"}
q.pop("silk")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    q.pop("silk")
TypeError: set.pop() takes no arguments (1 given)
q={"cotton","silk","rayon"}
q.clear()
print(q)
set()
>>> g={5,10,15,20,25}
>>> h={30,35,40,45,50}
>>> h={30,35,40,45,50}
>>> print(g.isdisjoint(h))
True
>>> x={"khammam","hyderabad","paleru","wyra"}
>>> y={"khammam","paleru"}
>>> print(y.issuperset(x))
False
>>> print(x.issuperset(y))
True
>>> o={"cse","ece","eee"}
>>> p="civil","mechanical","cse","ece"}
SyntaxError: unmatched '}'
>>> p={"civil","mechanical","cse","ece"}
>>> print(o.issubset(p))
False
>>> print(p.issubset(o))
False
>>> t={1,2,3,4}
>>> u={3,4,5,6}
>>> print(t.symmetric_difference(u))
{1, 2, 5, 6}
>>> f={"samsung","vivo","redmi"}
>>> g={"oppo","oneplus","iphone"}
>>> g={"oppo","oneplus","iphone"}
>>> print( f | g )
{'samsung', 'vivo', 'redmi', 'iphone', 'oneplus', 'oppo'}
>>> m={3,6,5,4,8}
>>> n={9,8,5,2}
>>> print( m & n )
{8, 5}
>>> u={10,20,30,40,50}
>>> v={10,40,50}
>>> print(u.symmetric_difference(v))
{20, 30}
>>> h={8,16,24,36,40}
>>> h.pop()
16

my_set={1,2,3.4}
print(3 in my_set)
print(5 not in my_set)


