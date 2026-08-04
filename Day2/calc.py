a=int(input("Enter a number: "))
b= int(input("Enter a number: "))
op = (input("Enter operator like *,-, +,/: "))
c=None
if op == '+':
    c = a + b
elif op == '-':
    c = a - b
elif op == '*':
    c = a * b
elif op == '/':
    c = a / b
else:
    print("Invalid operator")
print(f"result is: {c}")
    