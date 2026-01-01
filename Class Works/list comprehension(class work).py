namesl=[input("Enter the name:") for i in range(5)]
print(namesl)

l=[]
for i in range(1,11):
    l.append(i)
print(l)


s='python programming'
v='aeiouAEIOU'
r=[i if i in v else 0 for i in s]
print(r)


s='python programming language'
r={ i for i in s }
print(r)


s='python programming language'
r=tuple( i for i in s )
print(r)


d={}
for i in range(1,21):
    d[i]=i*i


d1={i:i*i for i in range(1,6)}
print(d1)


d1={input("Enter the product: "):input("Enter the price: ") for i in range (1,6)}
print(d1)



    






