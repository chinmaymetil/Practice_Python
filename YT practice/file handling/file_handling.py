# File Handling ==>
'''
with open("practice.txt", "r") as f:
    data = f.read()

n_data=data.replace("Java","Python")
print(n_data)


with open("practice.txt", "w") as f:
    f.write(n_data) 

def checkword():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("Not found")

checkword() 

def check_for_line():
    word = "learning"
    data=True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()'''


count = 0
with open("practice.txt","r") as f:
    data = f.read()

    num= data.split(",")
    for val in num:
        if(int(val) % 2==0):
            print(int(val))
            count += 1

print("total even number :",count)











