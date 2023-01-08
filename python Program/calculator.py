#calculator
a = int(input("Enter 1st number"))
b = str(input("Enter operation to be done ie + - * / **"))
c = int(input("Enter 2nd number"))

if b == '+':
    print("Addition is ", a+c)
elif b == "-":
    print("subraction is", a-c)
elif b == "*":
    print("multiplication is", a*c)
elif b == "/":
    print("division is", a/c)
elif b == "**":
    print("exponential is", a**c)
else:
    print("invalid operator")