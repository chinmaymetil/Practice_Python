#if else 5 code ==>

'''username = (input("Enter Username :"))
password = int(input("Enter Password :"))
if(username=="chinmay" and password==1234):
    print("Log in Succesfully...!")
else:
    print("Chcek Username and Password..")



attendence = int(input("Enter Your Collage Attendence :"))
if(attendence >= 75):
    print("Exam Allowed..!")
else:
    print("Attendance Short..")


print("Ans only yes/no ")
ticket = input("Do you have valid Ticket :")
if(ticket=="yes"):
    print("Check In Allowed..")
else:
    print("Check in not allowed..")



seats =int(input("Enter Available Seats :"))
if(seats > 0):
    print("ticket Confirmed...!")
else:
    print("Waiting List..")'''



amount = int(input("Tell me how much you spent on shopping :"))
if(amount >= 2000):
    print("Coupon Applied")
else:
    print("Minimum Amount Not Reached")