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
    print("file operations attemped")'''


# jar apan zero ne multiply karayala gelo tr error yete mhanun ha code  
try:
    a=int(input("Enter 1st number :"))
    b=int(input("Enter 2nd number :"))
    c=a/b
    print("C=",c)
except:
    print("Error")
print("Code executed successfully...")





