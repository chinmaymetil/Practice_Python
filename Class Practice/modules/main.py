import test_module 
name=input("What is Your Name ?\n")
test_module.show(name)

# Variable Module
a=test_module.person1["country"]
print(a)

# From-import 
from calculation import addition 
a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
print("Addition =",addition(a,b))
#       OR
from calculation import*  
a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
print("Sub =",substraction(a,b))


# Renaming a Module an use of alise(as)
import calculation as cal
a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
print("Multiplication =", cal.multiplication(a,b))

