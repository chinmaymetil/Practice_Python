# if - elif ladder ==>
'''
distance=int(input("Enter Your Distance :"))
if(distance<=5):
    print("Charges 50rs")
elif(distance<=10):
    print("Charges 70rs")
elif(distance<=15):
    print("Charges 100rs")
else:
    print("Charges 200")


attendence = int(input("Enter Your Attendence :"))
if(attendence > 90 and attendence <= 100):
    print("Good Attendence..")
elif(attendence > 75 and attendence <= 90):
    print("Exam allowed..")
elif(attendence > 60 and attendence <= 75):
    print("Warning...")
else:
    print("Exam Not Allowed...")



experience = int(input("Enter Your Experience :"))
if(experience <= 1):
    print("Fresher..")
elif(experience <=3):
    print("Junior")
elif(experience <=5):
    print("Mid-Level")
else:
    print("Senior...")

    
    
print("Color = green/yellow/red")
signal = input("Enter Signal color :")
if(signal=="green"):
    print("Go")
elif(signal=="yellow"):
    print("Wait")
elif(signal=="red"):
    print("Stop..!")
else:
    print("Invalid Signal..")'''


a = int(input("Enter 1s Number :"))
b = int(input("Enter 2nd Number :"))
optr = input("Choose Opreator = (+, -, *, /, m %, **) :")

if(optr=="+"):
    print(a+b)
elif(optr=="-"):
    print(a-b)
elif(optr=="*"):
    print(a*b)
elif(optr=="/"):
    print(a/b)
elif(optr=="%"):
    print(a%b)
elif(optr=="**"):
    print(a**b)
else:
    print("Invalid Opreator..")
