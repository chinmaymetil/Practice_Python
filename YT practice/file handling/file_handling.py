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

with open("demo.txt","r") as f:
    data = f.read()
    print(data)

    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num+=data[i]











