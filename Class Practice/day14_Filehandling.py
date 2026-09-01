# File Handling in python ==>
#first 12 letter  print hotat
'''
f=open("Class Practice/demo.txt", "r")
print(f.read(12))
f.close()

# whole data read krun deto list type madhe 
f=open("Class Practice/demo.txt", "r")
print(f.readlines())


# pratek line seprerate print hote
f=open("Class Practice/demo.txt", "r")
print(f.readline())
print(f.readline())
f.close()


# For loop for multilines 
f=open("Class Practice/demo.txt", "r")
for x in f:
    print(x)

# Write = w overwrite hote file madhe 
f=open("Class Practice/demo.txt", "w")
f.write("Hello My Name is Chinmay \n")
f.write("I'm Student")
f.close()

# Append = existing data chya nantr print hoto data
f=open("Class Practice/demo.txt", "a")
f.write("\n Now the file has more Content..!")
f.close()

# Create File = using X mode
f=open("sample.txt","x")

# Remove file = file remove karnya sarthi
import os
os.remove("sample.txt")'''


# with 
with open("Class Practice/demo.txt", "r") as f:
    data=f.read()
    print(data)








