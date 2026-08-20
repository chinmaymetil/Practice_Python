# while loop 
# sum of digits
num=int(input("Enter any number :"))
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



 


