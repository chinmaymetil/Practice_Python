# using function check the given number palindrome or not
def palindrome():
    num=int(input("Enter Any Number :"))
    temp=num
    rev=0
    while(num>0):
        digit=num % 10
        rev = rev*10 + digit
        num = num//10
    if(temp==rev):
        print(temp, "is palindrome number")
    else:
        print(temp, "is Not palindrome number")

palindrome()


# using function check the given number armstrong or not
def armstrong():
    num=int(input("Enter any number :"))
    temp=num
    sum=0
    while(num>0):
        rem=num % 10
        sum=sum+rem**3
        num=num//10
    if(temp==sum):
        print(temp,"is armstrong")
    else:
        print(temp,"is not armstrong")

armstrong()