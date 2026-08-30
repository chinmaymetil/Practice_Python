# check the given string is palindrome or not in function ==>
'''
def palindrome():
    name=input("Enter any Name :")
    rev=(name[::1])
    if(rev==name):
        print(rev,"is palindrome")
    else:
        print(rev,"is not palindrome")

palindrome()


# Count the Vowels in given string ==>

s=input("Enter Any string :")
vowels ="aeiou"
count = 0
for char in vowels:
    if char in vowels:
        count=+1
print("Number of Vowels:", vowels(s))

 print the vowel in given string
def print_vowels(text):
    vowels = "aeiou"
    text = text.lower()
    for character in text:
        if character in vowels:
            print(character)
string = input("Enter a string: ")
print_vowels(string)


print the positive,negative indexing plus character
a=input("enter a string:")
length=len(a)

for i in range(length):
    print(a[i],i,i-length)

count the frequency of given character
a=input("enter a string:")
b=input("enter a character to count:")
count=a.count(b)
print("freqvency of ",b,"is:",count)

count the wide space in given string
a=input("enter a string:")
count=a.count(" ")
print("count is:",count)

index and find and are index are find

s=krishn
and i want output k|r|i|s|n

s = "krishna"
b = "|".join(s)
print(b)
'''
