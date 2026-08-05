marks = int(input("Enter your marks: "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=75 and marks<90:
    print("Grade B")
elif marks>=60 and marks<74:
    print("Grade C")
elif marks>=40 and marks<59:
    print("Grade D")
elif marks>=0 and marks<39:
    print("Grade F")
else:
    print("Invalid Marks")