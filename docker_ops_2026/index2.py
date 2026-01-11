print("simple calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+': 
    print (a+b)
elif operation=='-':
    print(a-b)
elif operation == '*':
    print(a*b)
elif operation == "/":
    print(a/b)
else:
    print("invaild operation")

    #docker file 
""""FROM python:3.11-slim
WORKDIR /app
COPY index2.py .
CMD ["python", "index2.py"]
"""
