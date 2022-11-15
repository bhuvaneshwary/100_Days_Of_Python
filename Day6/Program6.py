number = int(input("Enter a n = "))
factorial = 1
sum = 1
for i in range(1, number + 1):
    factorial = factorial * i
    sum = sum + 1 / factorial
print("Sum of sequence = ", sum)


