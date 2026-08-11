# a = int(input("Enter a :"))
# b = int(input("Enter b :"))

# sum = a + b

# print("sum is :", sum)


name = "Chinmay Metil"

#String operstions => String operations in Python refer to various tasks performed on strings (such as concatenating, slicing, modifying, and searching lenth).
print(name.upper())
print(name.lower())

#find => ekhad char find karat variable madhal
print(name.find("nm"))
print(name.find("c"))
print(name.find("g"))

#Replace => aapn variable chi value change karta yete तात्पुर्ती 
print(name.replace("chinmay metil","sam"))
print(name.replace("chinmay", "pranav"))
print(name.replace("c", "v"))

#Check for presence => konta tr alphabate ahe ki nahi te check karta yet..asel tr TRUE OR FALSE Madhe show karat
print("X" in name)
print("M" in name)