i=1
while i<=10:
    print(i)
    i+=1


i=10
while i>0:
    print(i)
    i-=1


l=[1,2,3,4,5,6]
i=0
while i<=5:
    print(l[i])
    i+=1


l=(1,2,3,4,5,6,4567,3456,78,89)
s="python programming"
i=0
while i<len(s):
    print(s[i])
    i+=1


for i in range(12):
    if i==7:
        continue
    print(i)

for i in range(12):
    if i==7:
        break
    print(i)


chances=5
stored_pin="12345"
while chances>0:
    pin=input("Enter the pin:")
    if pin==store_pin:
        print("Login successful")
        break
    else:
        print("Incorrect pin")
        chances-=1
else:
        print("Try again!! After 30 secs")


products=['iphone','headset','smartwatch','tv','ac']
product=input("Enter the product:").strip()
for i in products:
    if i == product:
        print("{i} is found. you can buy it")
        break
    else:
        print(f"{product} is not found")


data={
    1:{'name':'bread','price':50},
    2:{'name':'milk','price':40},
    3:{'name':'sugar','price':80},
    4:{'name':'salt','price':70},
    5:{'name':'rice','price':90},
    }
for i in data:
    print(f'{i}.{data[i]["name"].title()}-       
    

    
