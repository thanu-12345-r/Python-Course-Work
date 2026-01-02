squares = [i*i for i in range (1,6)]
print(squares)

even=[i for i in range(1,11) if i%2==0]
print(even)

n = [ i for i in range(1,6)]
print(n)

n=[10,20,30]
result=[n+10 for n in n]
print(result)

n=[10,20,30,40,50,60]
result=[n for n in n if n > 50]
print(result)

names = ["Thanmai","Mohana","Roja sri"]
upper_names=[name.upper() for name in names]
print(upper_names)

n=["Even" if i%2==0 else "odd" for i in range (1,11)]
print(n)

data=["1","2","3"]
numbers = [int(x) for x in data]
print(numbers)

num=[-3,5,-1,7,0]
positive = [n for n in num if n>=0]
print(positive)

result=[i for i in range(1,101) if i%3==0 and i%5==0]
print(result)

words=["python","java","datascience","embeded system","vlsi"]
lengths = [len(word) for word in words]
print(lengths)

words=["education","python"]
n=[''.join([n for n in n not in 'aeiou']) for n in words] 
print(n)






