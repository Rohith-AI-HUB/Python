n = int(input("Enter a number of rows: "))
# pattern = []
# for i in range(n):
#     pattern.append(" " * (n - i) + "*" * (2 * i + 1))
# print("\n".join(pattern))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print('*',end='')
        j += 1
    print()
    i += 1
print("Pattern is completed")