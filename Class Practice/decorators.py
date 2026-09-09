# Decorators 
'''
def wish(name):
    print("Hello", name, "Good Morning")
wish("Chinmay") 
wish('Bunny')
wish("sunny")


def decor(func):
    def inner(name):
        if name=="sunny":
            print("Hello sunny Bad Morning")
        else:
            func(name)
    return inner

@decor # decorator Calling sathi use kartat 
def wish(name):
    print("Hello", name, "Good Morning")

wish("chinmay") 
wish("Bunny")
wish("sunny")

# we should not use @decor 
def decor(func):
    def inner(name):
        if name=="sunny":
            print("Hello sunny Bad Morning")
        else:
            func(name)
    return inner

def wish(name):
    print("Hello",name,"Good Morning")

decorfunction=decor(wish)

wish("Durga") # decorator wont be executed
wish("sunny") # decorator wont be executed

decorfunction("Durga") # decorator will be executed
decorfunction("sunny") # decorator wil be executed'''

# decor la call karun 3rd number ghyaycha
def decor(func):
    def num3(a,b):
        c=int(input("Enter 3rd Number :"))
        func(a,b,c)
    return num3
@decor
def add(a,b,c):
    print("Addition is :", a+b+c)

a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
add(a,b)

