def sum_of_digits(number):
    total = 0
    while number > 0:
        total = total + number % 10
        number = number // 10
    return total

def mul_of_digits(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if number == 0:
        return 0
    total = 1
    number = abs(number)  # Handle negative numbers
    while number > 0:
        digit = number % 10
        if digit != 0:  # Skip multiplication by zero digits
            total *= digit
        number = number // 10
    return total if total != 1 else 0  # Return 0 for numbers with only zero digits

def main():
    n = int(input("Enter a number: "))
    result1 = sum_of_digits(n)
    result2 = mul_of_digits(n)
    print("Sum of digits: ", result1,"Multiplication of digits: ",result2)

if __name__ == "__main__":
    main()
"""
This program calculates the sum of digits in a number.
"""