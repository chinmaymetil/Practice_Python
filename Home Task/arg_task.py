# Default Argument ==>
def greet(name, age):
    print("Hello", name ,"My age =", age)
greet("Chinmay" ,21)

# keyword Argument ==>

# 1. Cube of a number
cube = lambda x: x**3
print("Cube:", cube(5))

# 2. Square of a number
square = lambda x: x**2
print("Square:", square(6))

# 3. Add two numbers
add = lambda a, b: a + b
print("Addition:", add(10, 20))

# 4. Multiply two numbers
multiply = lambda a, b: a * b
print("Multiplication:", multiply(7, 8))

# 5. Find maximum of two numbers
maximum = lambda a, b: a if a > b else b
print("Maximum:", maximum(15, 25))

# 6. Reverse a string
reverse = lambda s: s[::-1]
print("Reverse:", reverse("Chinmay"))

# 7. Check even or odd
evenodd = lambda n: "Even" if n % 2 == 0 else "Odd"
print("Even/Odd:", evenodd(11))
