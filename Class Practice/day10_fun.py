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

#Return Statement
def addition(x,y):
    return x+y
print(addition(10,20))'''

# Recursion ==> swatala call karato jo paraynt condition satishfied hot nhi to praynt
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


'''# Required Arguments
def display(name):
    print("My name is :" +name)
display("Chinmay")

#keyword Argument
def hello(name,age,city):
    print(name,age,city)

hello("chinmay",20,"kolhpur")

# defualt Argument 
def info(name,age,city="Pune"):
    print(name,age,city)
info("Chinmay",22)
info("Bunny",22,"Mumbai")'''

