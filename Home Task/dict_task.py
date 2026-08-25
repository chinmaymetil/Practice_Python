# Dictinory ==>
stud={}
n=int(input("How Many Students..?"))

for i in range(n):
    name=input("Enter Student Name :")
    marks=int(input("Enter Marks :"))
    stud[name]=marks
    print("stud Dict :",stud)


# Set ==> in set print only original element without set function 



    # Methods in dict 
    # Python Dictionary Methods Examples

# 1. clear()
student = {"name": "Rahul", "age": 21}
student.clear()
print("clear():", student)  

# 2. copy()
student = {"name": "Rahul", "marks": 85}
new_student = student.copy()
print("copy():", new_student)  

# 3. fromkeys()
keys = ["name", "age", "marks"]
new_dict = dict.fromkeys(keys, 0)
print("fromkeys():", new_dict)  

# 4. get()
student = {"name": "Rahul", "marks": 85}
print("get(marks):", student.get("marks"))  
print("get(address):", student.get("address"))  

# 5. items()
student = {"name": "Rahul", "age": 21}
print("items():", student.items()) 

# 6. keys()
student = {"name": "Rahul", "marks": 85}
print("keys():", student.keys()) 

# 7. values()
student = {"name": "Rahul", "marks": 85}
print("values():", student.values())  

# 8. pop()
student = {"name": "Rahul", "age": 21}
removed = student.pop("age")
print("pop(): Removed:", removed)  
print("After pop:", student)  

# 9. popitem()
student = {"name": "Rahul", "marks": 85}
student.popitem()
print("popitem():", student) 

# 10. setdefault()
student = {"name": "Rahul"}
student.setdefault("marks", 80)
print("setdefault():", student)  

# 11. update()
student = {"name": "Rahul", "marks": 85}
student.update({"marks": 90, "address": "Pune"})
print("update():", student)  

