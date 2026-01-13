try:
    a=10
    b=a/0

except  ZeroDivisionError:
    print("you can't divide number with zero")
else:
    print()

print("reset of the code")


try:
    a=10
    b=a/10

except ZeroDivisionError:
    print("you can't divide number with zero")
else:
    print("code success, NO Error")
    print("Reset of the Code")


try:
    a=10
    b=a/0
except ZeroDivisionError:
    print("you can't divide number with zero")
except NameError:
    print("value is not defined")
except KeyError:
    print("key is not defined in dict")
except IndexError:
    print("Index is not present in the seq")
except ValueError:
    print("Enter the proper value")
except TypeError:
    print("Data type is different")
else:
    print("Code success,No Error")
finally:
    print("End of Try Block")
    print("Reset of the Code")


try:
    a={1:1,2:4,3:9}
    b=a[4]
except (ZeroDivisionError,NameError,KeyError,IndexError,ValueError,TypeError):
    print(f"Error Occured")
else:
    print("Code sucess,No Error")
finally:
    print("End of Try Block")
    print("Reset of The Code")


try:
    a=-1000
    if a<0:
        raise exception("You can't withdraw -ve amount")

except Exception as e:
    print(f"Error Occured: {e}")
else:
    print("Code sucess,No Error")
finally:
    print("End of Try Block")


try:
    a=10
    b=a/c

except Exception as e:
    print(f"Error Occured: {e}")
else:
    print("Code sucess,No Error")
finally:
    print("End of Try Block")
    print("Reset of The Code")


    
