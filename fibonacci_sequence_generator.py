# 11. Fibonacci Sequence Generator

n = int(input("Enter how many numbers you want: "))

a = 0
b = 1

for i in range(n):
    print(a)
    next_number = a + b
    a = b
    b = next_number
