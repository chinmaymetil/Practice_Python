# Exception handling in Files
'''
try:
    print(b)
except:
    print("its an Example of Exception")
    

try:
    with open("Not_file.txt","r") as f:
        content =f.read()
        print(content)
except FileNotFoundError:
    print("Error : file does not exits")
except IOError:
    print("error :- File io error")

finally:

    print("file operations attemped")


# jar apan zero ne multiply karayala gelo tr error yete mhanun ha code  
# Runtime Error
try:
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    c=a/b
    print("C=",c)
except:
    print("Error")
print("Code executed successfully...")

#without Try Except ==>
print("fortune")
print(10/0)
print("Cloud")


# with try- except ==>

print("Chinmay")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("Python")



try:
    x=int(input("Enter 1st Number :"))
    y=int(input("Enter 2nd Number :"))
    print(x/y)
except ZeroDivisionError:
    print("Cant Divide with zero")
except ValueError:
    print("Please provide int value only")
 

# Parant Error And child Error
try:
    x=int(input("Enter 1st Number :"))
    y=int(input("Enter 2nd Number :"))
    print(x/y)
except ArithmeticError:
    print("Arithmetic Error")
except ZeroDivisionError:
    print("Zero Divison Error")
'''

# nested Try-Except 
try:
    print("Outer Try block")
    try:
       print("Inner Try Block")
       print(10/0)
    except ZeroDivisionError:
        print("Inner Except Block")
    finally:
        print("Inner Finally Block")
except:
    print("Outer except Block")
finally:
    print("outer Finally Block")

