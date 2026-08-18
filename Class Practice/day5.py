# nested id else

'''num=int(input("Enter Any No :"))
if(num>0):
    print("Number is Positive")
    if(num%2==0):
        print("Number is Even")
    else:
        print("Number is Odd")
else:
    print("Number is Negative")


# elif ladder ==>
a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
c=int(input("Enter 3rd Number :"))

if(a>b and a>c):
    print("A is Greater")
elif(b>a and b>c):
    print("B is Greater")
else:
    print("C is Greater")'''



marks = int(input("Enter Your Marks :"))
print("marks :", marks)

if (marks > 90 and marks<=100):
    print("Your Grade = A")
elif (marks > 60 and marks <= 90):
    print("Your Grade = B")
elif (marks > 35 and marks <= 60):
    print("Your Grade = c")
else:
    print("Fail")


