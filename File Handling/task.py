# task 1 ==> 1.Create a file named student.txt and write "Welcome to Python" into it using w mode.
'''
f = open("File Handling/student.txt", "w")
f.write("Welcome to Python")
f.close()


#Task 3 ==> Create a file named data.txt and write your name, age, and city into it.
f = open("File Handling/data.txt", "w")

f.write("Name: Chinmay\n")
f.write("Age: 21\n")
f.write("City: KOlhapur")
f.close()


# task 3 ==> Open student.txt in read mode (r) and display its complete content.
f = open("File Handling/student.txt", "r")

data = f.read()
print(data)
f.close() 

# task 4 ==> Write a Python program to count the number of characters in student.txt.
f = open("File Handling/student.txt", "r")

data = f.read()
count = len(data)

print("Number of characters:", count)
f.close()


# task 5 ==> Open student.txt in append mode (a) and add "Python File Handling" at the end of the file.
f = open("File Handling/student.txt", "a")

f.write("\n Python File Handling")
f.close()


# task 6 ==> Create a file named marks.txt and write the following:
# Python: 80
# Java: 75
# Mern Stack: 85
f=open("File Handling/marks.txt","w")

f.write("Python: 80\n")
f.write("Java: 75\n")
f.write("Mern Stack: 85")
f.close() 

# task 7 ==> Read marks.txt and display each line separately.
f = open("File Handling/marks.txt", "r")

for line in f:
    print(line)
f.close()

# task 8 ==> Create a file named message.txt using x mode and write "Hello Students" into it
f=open("File Handling/message.txt","x")

f.write("Hello Student")
f.close()

# task 9 ==> Open student.txt and check whether the word Python is present in the file or not
f = open("File Handling/student.txt", "r")
data = f.read()

if "Python" in data:
    print("present in the file")
else:
    print("not present in the file")

f.close()'''


# task 10 ==> Create a file named numbers.txt and write numbers 1 to 10, each on a new line. Then read and display them
f = open("File Handling/numbers.txt", "w")

for i in range(1, 11):
    f.write(str(i),"\n")

f = open("File Handling/numbers.txt", "r")

for line in f:
    print(line)

f.close()