
greatest1 = lambda a,b:a if a>b else b

print(greatest1(19,12))
print(greatest1(15,20))

def sum(a,b,c):
    return a+b+c

sum = lambda a,b,c: a+b+c

print(sum(19,12,12))
print(sum(15,20,23))


l=[2,0,4,0,9,0,6,0,3,0,0,0]

def removezeros(l):
    res=[]
    for i in l:
        if i!=0:
            res.append(i)
        return res

n= list(filter(lambda i:i!=0,l))
print(n,removezeros(l))


l=[1,2,3,4,5,6,1,2,3,4]

def evennumbers(lst):
    res=[]
    for i in lst:
        if i % 2 == 0:
            res.append(i)
    return res

n=list(filter(lambda i : i%2==0, l))
print(evennumbers(l),n)


vol='AEIOUaeiou'
s='python programming'
def filtervol(s):
    res=[]
    for i in vol:
        res.append(i)
    return res

n=list(filter(lambda i:i in vol,s))
print(filtervol(s),n)






    
