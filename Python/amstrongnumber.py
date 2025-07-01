n = int(input("Enter your numbers of even No. = "))
i = n
count = 0
while (i>0):
    i = i // 10
    count = count + 1
print("Number of digits = ", count)

i = n
sum = 0
while (i > 0):
    sum = sum + (i % 10)**count
    i = i // 10
print("Sum of digits = ", sum)
if(sum==n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")