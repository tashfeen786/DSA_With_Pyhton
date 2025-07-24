n = 157
num = n
num_of_digit = len(str(n))

total = 0
while num > 0:
    large_digit = num %10
    total += large_digit ** num_of_digit
    num = num // 10
if total == n:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")