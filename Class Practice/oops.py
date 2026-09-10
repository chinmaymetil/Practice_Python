# OOPS ==>
# Non-parameter 
class Student:
    def __init__(self): # init is Constructor 
        self.name="Chinmay" # this intance variable 
        self.age=22
        self.marks=90

    def display(self): # intance methods
        print("Name Of Student is :",self.name)
        print("Age Of Student is :",self.age)
        print("Marks Of Student is :",self.marks)

s1=Student() # this is object 
s1.display()


# Parameter 
class Student:
    def __init__(self,name,age,marks): # init is Constructor 
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print("Name Of Student is :",self.name)
        print("Age Of Student is :",self.age)
        print("Marks Of Student is :",self.marks)

s1=Student("Adi",21,70) # this is object 
s2=Student("Rohan",22,80)    
s1.display()
s2.display()
    

