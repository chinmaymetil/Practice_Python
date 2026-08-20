# While loop ==> we dont know the advance condition then we use while loop..
#                this is entry control loop.

print("Print 1 to 10")
i=1
while(i<=10):
    print(i)
    i+=1

print("\nprint 10 to 1")
i=10
while(i>=1):
    print(i)
    i-=1


# 234 cha revers number 
num=int(input("Enter any Number :"))
rev=0
while(num>0):
    rem=num%10  # ethe pratek veli 10 ch ghyaych karan 10 ne proper reminder yeto
    rev=rev*10+rem
    num=num//10  # flore divison mhanje aaplyala questiont(Bhagakar) float nhi tr int madhe return yeto
print("Reverse Number is :", rev)

#Palindrome Number  232==232 mhanje palindrome
num=int(input("Enter any Number :"))
rev=0
temp=num
while(num>0):
    rem=num%10 
    rev=rev*10+rem
    num=num//10 
if(temp==rev):
    print("Given Number is Palindrome no :",temp)
else:
    print("Given Number is not Palindrome no :",temp)


# Armstrong Number 
num=int(input("Enter any number :"))
temp=num
sum = 0
while(num > 0):
    rem=num%10
    sum=sum +rem ** 3
    num=num//10
if(temp==sum):
    print("This is armstrong")
else:
    print("this is not armstrong")






