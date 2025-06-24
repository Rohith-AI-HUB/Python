print("Welcome to basic calculator")
Num1 = int(input("Enter first number: "))
Operator = input("Enter operator (+, -, *, /, %): ")
Num2 = int(input("Enter second number: "))

if Operator == "+":
    print("Result: " + str(Num1 + Num2))
elif Operator == "-":
    print("Result: " + str(Num1 - Num2))
elif Operator == "*":
    print("Result: " + str(Num1 * Num2))
elif Operator == "/":
    print("Result: " + str(Num1 / Num2))
elif Operator == "%":
    print("Result: " + str(Num1 % Num2))
else:
    print("Invalid operator")