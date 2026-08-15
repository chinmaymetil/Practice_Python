# Conditinal Statements =>

marks = int(input("Enter Your Marks :"))
print("marks :", marks)

if marks >= 80:
    print("Your Grade = A")
elif marks < 80 and marks >= 60:
    print("Your Grade = B")
elif marks <60 and marks >= 35:
    print("Your Grade = C")
else:
    print("Fail")