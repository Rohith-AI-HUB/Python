i = int(input("Enter your number = "))
fib_array = []  # Initialize empty array to store fibonacci numbers
x = 0
y = 1
z = 0

while z <= i:
    fib_array.append(z)  # Add current number to array
    x = y
    y = z
    z = x + y

print("Fibonacci series is completed:", fib_array)  # Print the entire array
