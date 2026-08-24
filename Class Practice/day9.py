# Dictionary 

d=dict()
print(type(d))  # Empty Dictinary 

s=set()
print(type(s))

#Dictionary in py
d={1:'Chinmay', 2:'Hitesh', 3:'Rohan', 4:'Raj'}

#Printing Dict
print(d)

#Accending Value Using Keys
print("1st Name is :" +d[1])
print("2nd Name is :" +d[4])

print(d.keys())
print(d.values())


#set
s={2,1,3,6,4,5,3,2,6,1}
print("Set is :", s)

#Create Empty Set
set1=set()
set2={'Abc', 2, 3, 'Xyz'}

#Printing Set Value
print(set2)

#adding element to the set

set2.add(10) #using add we can add only one element and update madhe aapn multiple element add kru shaktoS
print(set2)

#removing element from the set 
set2.remove(2)
print(set2)

#Duplicate 
a={2,1,3,4,4,3,2,1,3,4,2}


#intersection_update
x={'a','b','c'}
y={'c','d', 'e'}
z={'f','g','c'}

x.intersection_update(y,z)
print(x)