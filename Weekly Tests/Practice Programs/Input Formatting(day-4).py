Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input("Enter your full name: ")
Enter your full name: "Thanmai"
print(name)
"Thanmai"
quantity=int(input("Enter the number of items: "))
Enter the number of items: 5
print(quantity)
5
price=float(input("Enter the product price:"))
Enter the product price:99.99
print(price)
99.99
>>> names=input("Enter employee names (space-separated):").split()
Enter employee names (space-separated):thanmai mohana rojasri
>>> print(names)
['thanmai', 'mohana', 'rojasri']
>>> tags=input("Enter tags (comma-separated):").split(',')
Enter tags (comma-separated):sale,discount,offer,new
>>> print(tags)
['sale', 'discount', 'offer', 'new']
>>> marks=list(map(int,("Enter marks:").split()))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    marks=list(map(int,("Enter marks:").split()))
ValueError: invalid literal for int() with base 10: 'Enter'
>>> marks=list(map(int,input("Enter marks:").split()))
Enter marks:90 80 70 60 50
>>> print(marks)
[90, 80, 70, 60, 50]
>>> weights=list(map(float, input("Enter weights: ").split()))
Enter weights: 32.5 80 90.2 
>>> print(weights)
[32.5, 80.0, 90.2]
>>> dimensions=tuple(map(int,input("Enter lenght,width,height: ").split()))
Enter lenght,width,height: 10 20 15 
>>> print(dimensions)
(10, 20, 15)
>>> selected_ids=set(map(int, input("Enter selected image ids:").split()))
Enter selected image ids:424 432 445
>>> print(selected_ids)
{424, 445, 432}
>>> profile=eval(input("Enter user profile as a dictionary: "))
Enter user profile as a dictionary: {'name':'Thanmai','age':'22','role':'admin'}
>>> print(profile)
{'name': 'Thanmai', 'age': '22', 'role': 'admin'}
>>> username , password = input("Enter username and password:").split()
Enter username and password:user05 mypassword345
>>> print("username:", username)
username: user05
>>> print("password:", password)
password: mypassword345
