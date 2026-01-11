# Simple Calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose operation")
print("+  -  *  /")

op = input("Enter operator: ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")

