from collections import Counter, defaultdict,deque

n='Dhaush is bad boy.He can\'t ride bike.'.split()
res=Counter(n)
print(res)


from collections import Counter, defaultdict,deque

n=[9,5,6,8,1,0,0,4,6,6,4,8]
res=Counter(n)
print(res)


from collections import Counter, defaultdict,deque

n=[9,5,6,8,1,0,0,4,6,6,4,8]
res=defaultdict(str)
for i in n:
    res[i]+=str(i)
    print(res)
    

from collections import Counter, defaultdict,deque


q=deque([])
q.appendleft(10)
print(q)

q.appendleft(20)
print(q)

q.appendleft(30)
print(q)

q.pop()
print(q)

q.append(40)
print(q)

q.append(50)
print(q)

q.popleft()
print(q)

q.popleft()
print(q)


10-l
20-l
30-l
pop-r
pop-r
40-r
50-r
pop-l
pop-l

