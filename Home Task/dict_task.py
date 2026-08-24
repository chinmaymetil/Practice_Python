# Dictinory ==>
stud={}
n=int(input("How Many Students..?"))

for i in range(n):
    name=input("Enter Student Name :")
    marks=int(input("Enter Marks :"))
    stud[name]=marks

    print("stud Dict :",stud)