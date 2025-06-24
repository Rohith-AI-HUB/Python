print("Swap two numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: a = " + str(a) + ", b = " + str(b))
temp = a
a = b
b = temp
print("After swapping: a = " + str(a) + ", b = " + str(b))