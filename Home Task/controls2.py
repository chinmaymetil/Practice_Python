#nested if 5 programs ==>
# 1
balance=5000
amount=int(input("Enter Your Withdraw Amount :"))

if(balance >= 5000):
    if(amount <= balance):
        print("Withdrawal Possible")


#   2
username=input("Enter your Username :")
password=int(input("Enter Your Password :"))

if(username=="chinmay"):
    if(password==9696):
        print("Successfully Log In..")

#    3
salary=int(input("Enter Salary :"))
experience = int(input("Enter Experience :"))

if (salary > 30000):
    if (experience > 2):
        print("Eligible For Bonus...")


#   4
age=int(input("Enter Your Age :"))
price=int(input("Enter Ticket Price :"))
if(age >= 18):
    if(price >500):
        print("Ticket Price is High...")
        

#   5
amt = int(input("Enter Purchase amount :"))
member = input("Are You Member :")

if(amt>1000):
    if(member=="yes"):
        print("Discount Available...")
