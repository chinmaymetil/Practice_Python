# while loop 
# sum of digits
'''num=int(input("Enter any number :"))
sum_digits=0
while(num>0):
    digit=num%10
    sum_digits = sum_digits + digit 
    num = num//10
print("Sum of Digits :", sum_digits)


# Multiplication of Digits
num=int(input("Enter any number :"))
multi_digits=1
while(num>0):
    digit=num%10
    multi_digits = multi_digits * digit 
    num = num//10
print("Multiplication of Digits :", multi_digits)


# Armstrong Number 
num=int(input("Enter any number :"))
temp=num
digits = len(str(num))
sum = 0
while(num > 0):
    rem=num%10
    sum=sum +rem ** digits
    num=num//10
if(temp==sum):
    print("This is armstrong")
else:
    print("this is not armstrong")


num=int(input("Enter the Range :"))
even_sum=0
i=1
while(i<=num):
    if(i%2==0):
        print("Number is Even", i)
        even_sum=even_sum+i
    i=i+1

odd_sum=0
i=1
while(i<=num):
    if(i%2!=0):
        print("Number is Odd",i)
        odd_sum=odd_sum+i
    i=i+1

print("Even Sum is :", even_sum)
print("Odd Sum is :", odd_sum)

total=even_sum + odd_sum
print("Even Sum and Odd sum is :", total)
if(total%2==0):
    print("Sum is even")
else:
    print("Sum is odd")'''


print("Cube of Number")
num=int(input("Enter Any Number :"))
while(num>0):
    cube = num**3
    print("Cube is :", cube)
    num=num-1

print("Square Of Number ")
num=int(input("Enter Any Number :"))
while(num>0):
    square=num**2
    print("Square is :", square)
    num=num-1


print("Even No - square and odd Number - cube")
num=int(input("Enter Your Range :"))
i=1
while(i<=num):
    if(i%2==0):
        print("Even Number Square :", i**2)
    else:
        print("Oddd Number Cube :", i**3)
    i=i+1


sum=0
i=1
while(i<=10):
    sum=sum+i
    i=i+1
print("1 to 10 Numbers sum is :",sum)
      
      
      
     

 


