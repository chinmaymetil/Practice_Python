# array ==> the array can be created in python by importing the array module to the python program .
# scalar = 0d array
# vector = 1d array
# matrix = 2d array
# tenser = 3d array

from array import*
a=array('i',[2,4,6,8])
print(a)

import array as arr
a=arr.array('i',[2,4,6,8])
print(a)

# Add element in array
num = arr.array('i',[1,2,3,4,5])
num[0]=0
print(num)

#  slicing in array (Replace)
num = arr.array('i',[1,2,3,4,5])
num[2:5]=arr.array('i',[4,6,8])
print(num)

# Delete Elements in array
num = arr.array('i',[1,2,3,4,5])
del num[2]
print(num)

# Concatenation 
a=arr.array('d',[1.0,2.0,3.0,4.0,5.0])
b=arr.array('d',[2.1,3.1])

c=arr.array('d')

c=a+b
print("C=",c)

