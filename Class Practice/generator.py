'''
what is generator in python.
it is a special type of iterator that allows you to 
iterate over a sequence of value without storing the entire sequence 
in memeory at once. generatorsare defined using function and the "yield" statement,
which produces a value and suspends the functions state, allowing it to be resumend later.
this makess generators memory-efficient and suitable for working withlarge database or streams of data
Real time    E.g = Bus Ticket
'''



def mygen():
    yield "A"
    yield "B"
    yield "C"

g=mygen()
print(type(g))

print(next(g))
print(next(g))
print(next(g))
#print(next(g)) # ha stop karnya sathi use kartat


# second 

def countdown(num):
    print("Start Count Down")
    while(num>0):
        yield num
        num=num-1 

values=countdown(5)
for x in values:
    print(x) 