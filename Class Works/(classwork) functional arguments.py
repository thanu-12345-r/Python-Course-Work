'''
def display(uname,email,pwd):
    print(f"username: {uname}\nemail: {email}\npwd: {pwd}")

username=input()
gmail=input()
password=input()

display(uname=username,email=gmail,pwd=password)
display(email=gmail,uname=username,pwd=password)
display(email=gmail,pwd=password,uname=username)


def display(uname,email,pwd,status="Absent"):
    print(f"username: {uname}\nemail: {email}\npwd: {pwd}")
    
uname=input()
gmail=input()
pwd=input()

display("subash","subash@gmail.com","s@123")
display("vinay","vinay@gmail.com","vinay@123","present")


def display(*names):
    for i in names:
        print(i)
    print('-------')

display("ram","prasad","sujith")
display("subash","lohit","saiteja","surya")
display("abhinov","rakesh")
display("vishnu")


def display(**names):
    for i in names:
        print(f'{i}:{names[i]}')
    print('-------')

display(k1="ram",k2="prasad",k3="sujith")
display(n1="subash",n2="lohit",n3="saiteja",n4="surya")
display(x1="abhinov",x2="rakesh")
display(y1="vishnu")

def display(name):
    name='lohit'
    print(f"Inside: {name}")

name='Ram'
display(name)
print(f"outside: {name}")


def display():
    global name
    name='lohit'
    print(f"Inside: {name}")

name='ram'
display()
print(f"outside: {name}")

'''
def display(course):
    print(f"starting: {course}")

    def change():
        nonlocal course
        course='python full stack'
        print(f"change:{course}")

    change()
    print(f"final course: {course}")

course="java full stack"
display(course)
          


          





    
    
