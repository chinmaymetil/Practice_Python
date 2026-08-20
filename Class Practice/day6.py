# loops ==> for loop

'''for i in range(0,11):
    print("Python")

for j in range(0,11,2):
    print(j)

for c in range(10,0,-1):
    print(c)'''


for i in range(1,11):
    if(i%2==0):
        print("even Number",i)
    else:
        print("Odd Number", i)


e_sum = 0
for j in range(1,11):
    if(j%2==0):
        e_sum+=j
print("Even number sum =", e_sum)
if(e_sum%2==0):
    print("Sum is even ", e_sum)
else:
    print("Sum is Odd")


o_sum = 0
for j in range(1,11):
    if(j%2!=0):
        o_sum+=j
print("odd number sum =", o_sum)


for i in range(1,11):
    square=i**2
    print(square)

for j in range(1,11):
    cube=j**3
    print(cube)

print("Even Number Square and Odd Number Cube ==>")
for i in range(1,11):
    if(i%2==0):
        print("even no square is", i**2)
    else:
        print("Odd no cube is", i**3)

for i in range(1,11):
    if(i%2==0):
        print("even no square is", i**2)

for i in range(1,11):
    if(i%2!=0):
        print("Odd no square is", i**3)








