def check_prime(num):
    if num%2==0:
        return "Not prime"
    for i in range(3,num):
        if num %i==0:
            return "Not Prime"
    return "Prime"
number=int(input("Enter number:"))
res=check_prime(number)
print(f"Result:{res}")