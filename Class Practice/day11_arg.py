# variable length argument ==>
# *marks ==> * means ALL variable tuple format madhe store hoil
def hello(name, *marks):
    print("name=", name)
    print("marks =", marks)

hello("Chinmay", 1,2,3,4,5,6)


def hello( *marks): #name variable define kel nhi tr marks madhe ch value store hoil
    print("marks =", marks)

hello("Chinmay", 1,2,3,4,5,6)

## keyword variable length arugemnt ==> pass all the value of dictonary inside ** marks parameter

def hello(name, **marks):
    print("Name=", name)
    print("marks=", marks)

hello("Abhi", m=78,p=90,c=80,h=75)
    
# Lambda Forms
cube=lambda x:x**3
total = cube(5)
print(total)


# Local And Global Variable ==>
#Local Variable == 

# Global Variable ==>
a="Virat Kohli" # global variable 
def f1():
    global b   # local variable la aapn function chya baher define karayla use kartat
    b="Rohit Sharma"
    print(a,b)
f1()

def f2():
    print(a)
    print(b)
f2()
