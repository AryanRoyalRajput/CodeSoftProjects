print("*** Simple Calculator ***")
a = float(input("Enter first number : "))
b = float(input("Enter second number : "))

print("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiply\nPress 4 for Division")
choice = int(input("Enter your choice : "))
if choice == 1:
    print("The Addition is ", a+b)
elif choice == 2:
    print("The Subtraction is ", a-b)
elif choice == 3:
    print("The multiply is ", a*b)
elif choice == 4:
    print("The Division is ", a/b)
else:
    print("Invalid Input")

