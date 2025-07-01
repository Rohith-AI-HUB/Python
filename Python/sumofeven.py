n = int(input("Enter a number:"))
i = 2
sum = 0
while i <= n:
    # sum = sum + i
    # i += 2
    if i % 2 == 0:
        sum += i
    i += 2
print("Sum of Even numbers: ",sum)