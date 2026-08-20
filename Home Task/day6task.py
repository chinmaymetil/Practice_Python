# Class practice code here ==>
'''
For the numbers 1 to 10, I need the following:
1) check Even numbers and Odd numbers 
2) then check The sum of the even numbers 
3) then check The sum of the odd numbers 
4) then Check the sum of the even and odd numbers is even or odd.

even_sum = 0
print("Even Numbers :")
for i in range(1,11):
    if(i%2==0):
        print(i)
        even_sum = even_sum + i 

odd_sum = 0
print("Odd Numbers :")
for i in range(1,11):
    if(i%2!=0):
        print(i)
        odd_sum = odd_sum + i

print("Sum of even no :", even_sum)
print("sum of odd no :", odd_sum)

total=even_sum + odd_sum
print("Even And Odd Numbers sum is :", total)
if(total%2==0):
    print("Total sum is Even")
else:
    print("Total Sum is Odd")'''


print("Find Square of 1 to 10")
for i in range(1,11):
    print(i**2)

print("Find Cube of 1 to 10")
for i in range(1,11):
    print(i**3)


print("Display table of Number :")
num1=int(input("Enter Any Number of 1 - 10 :"))
for i in range(1,11):
    print(i*num1)


print("Even no - square and Odd no - Cube ==>")
for i in range(1,11):
    if(i%2==0):
        print("Even Numbers Suqare :", i**2)
    else:
        print("Odd Numbers Cube :", i**3)

sum=0
for i in range(1,11):
    sum=sum+i
print("1 to 10 number sum is :", sum)