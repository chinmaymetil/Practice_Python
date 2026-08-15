# Calculator =>

a = float(input("Enter Your 1st No :"))
b = float (input("Enter Your 2nd No :"))
op = input("Enter Operator (+, -, *, /, m %, **):")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '%':
    print(a % b)
elif op == '**':
    print(a ** b)
else:
    print("Invalid Operator ")






