n = int(input("Enter a Number:"))
if n < 2:
    print("Not Prime")
for i in range(2,n):
    if (n%i==0):
        print("Not prime")
        break
else:
    print("Prime")

