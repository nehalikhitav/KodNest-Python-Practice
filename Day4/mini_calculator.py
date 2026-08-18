def mini_calc(num1,num2,operator):
    if operator=='+':
        return num1+num2
    elif operator=='*':
        return (num1*num2)
    elif operator=='-':
        return num1-num2
    elif operator=='/':
        return num1//num2
    else:
        return "Invalid operator."

num1=int(input("Enter number:"))
num2=int(input("Enter number:"))
operator=input("Enter operator:")
result=mini_calc(num1,num2,operator)
print("result: ",result)