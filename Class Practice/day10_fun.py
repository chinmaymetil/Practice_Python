# Funtion
# Non-Parameterzied Function ==>
'''def wish():
    print("Hii , I'm Chinmay")
wish()

def wish():
    print("Hii , I'm Chinmay")
wish()
print("Bye bye")
wish()


# Parameterzied Function ==>
def add(a,b):
    print("Addition of Two Numbers :", a+b)
add(10,20)
add(100,200)
add(1000,2000)

#Return Statementio
def addition(x,y):
    return x+y
print(addition(10,20))'''


def display(name):
    print("My name is :", name)
display("Chinmay")


#keyword Argument

def hello(name,age,city):
    print(name,age,city)

hello("chinmay",20,"kolhpur")


def info(name,age,city="Pune"):
    print(name,age,city)
info("Chinmay",22)
info("Bunny",22,"Mumbai")