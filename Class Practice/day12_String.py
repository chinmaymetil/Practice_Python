# check the given string is palindrome or not in function ==>
'''
def palindrome():
    name=input("Enter any Name :")
    rev=(name[::1])
    if(rev==name):
        print(rev,"is palindrome")
    else:
        print(rev,"is not palindrome")

palindrome()'''


# Count the Vowels in given string ==>

s=input("Enter Any string :")
vowels ="aeiou"
count = 0
for char in vowels:
    if char in vowels:
        count=+1
print("Number of Vowels:", vowels(s))

