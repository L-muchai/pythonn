# mark=int(input("Enter Marks:"))
#
# if mark>=80 and mark<=100:
#     print("You have an A")
# elif mark>=60 and mark<=79:
#     print("You have an B")
# elif mark>=40 and mark<=59:
#     print("You have an C")
# elif mark>=0 and mark<39:
#     print("You have failed  terribly")
# else:
#     print("wrong inputs,check your marks")
#
num=int(input("Enter num"))
num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
num3=int(input("Enter num3"))
if num>num1 and num>num2 and num>num3:
    print(f"{num} is the largest number")
elif num1>num and num1>num2 and num1>num3:
    print(f"{num1} is the largest number")
elif num2>num and num2>num1 and num2>num3:
    print(f"{num2} is the largest number")
elif num3>num and num3>num1 and num3>num2:
    print(f"{num3} is the largest number")
else:
    print("All numbers are equal")
