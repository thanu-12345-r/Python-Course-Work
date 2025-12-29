for j in range(6):
    for i in range(5):
        print(i,end=' ')
        print()


for row in range(5):
    for column in range (5):
        print('*',end=' ')
        print()


for row in range(4):
    for column in range(5):
        print(column+1,end=' ')
        print()


for row in range(5):
    for column in range(6):
        print(row+1,end=' ')
        print()


for i in range(5):
    for column in range(row+1):
        print('*',end=' ')
    print()


n=int(input("Enter the size: "))
for row  in range(n):
    for column in range( n-row):
        print('*',end=' ')
    print()


n=int(input("Enter the size: "))
for row  in range(n):
    for spc in range(n-1-row):
        print(" ",end=' ')
    for col in range( row+1):
        print('*',end=' ')
    print()


n=int(input("Enter the size: "))
for row in range (n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1:
            print('*',end=' ')
        else:
            print(" ",end=' ')
    print()


n=int(input("Enter the size: "))
for row in range (n):
    for col in range(n):
        if row==0 or row==n-1 or row+col==n-1:
            print('*',end=' ')
        else:
            print(" ",end=' ')
    print()


    



    



    
        
    



