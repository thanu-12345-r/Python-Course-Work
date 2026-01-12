greet = lambda: "Hello python"
print(greet())

square = lambda x:x*x
print(square(5))

add=lambda a,b:a+b
print(add(10,20))

largest=lambda a,b,c:a*b*c
print(largest(10,20,30))

maximum=lambda a,b,c:a if a>b and a>c else b if b>c else c
print(maximum(10,25,15))

even_odd = lambda x: "Even" if x%2 == 0 else "Odd"
print(even_odd(7))

num=[1,2,3,4,5,6]
even = list(filter(lambda x:x%2 == 0,num))
print(even)

num=[0,1,0,2,3,0,0,5]
non_zero=list(filter(lambda x:x!=0,num))
print(non_zero)


num=[5,10,15,20,25]
greater=list(filter(lambda x: x>10,num))
print(greater)

names=["Thanmai","Mohana priya","Roja sri"]
long_names=list(filter(lambda x: len(x)>7,names))
print(long_names)

names=["python","java","datascience","cloudcomputing","cybersecurity"]
upper=list(map(lambda x:x.upper(),names))
print(upper)

