book = float(input("Enter Book Price :"))
pen = float(input("Enter Pen Price :"))
pencil = int(input("Enter Pencil Price :"))

total = book + pen + pencil
print("total bill =", total)

#avarage 
avarage = total/3
print("Avarage Price =", avarage)


# take a superhero nama as input
hero = input("Enter your fav super hero name :")

if hero[0].lower() == "s":
    print("Super hero name start with S/s")
else:
    print("Super hero does not start with S/s")


