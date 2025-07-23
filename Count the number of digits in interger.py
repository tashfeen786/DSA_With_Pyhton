n = 54383456
num = n 
count = 0
while num > 0:
    value = num % 10
    count += 1
    num = num // 10 
print("Number of digits:", count)


# solution to count the number of digits in an integer by logarithmic method
import math
n = 543
if n == 0:
    count = 1
else:
    count = int(math.log10(n)) + 1
print("Number of digits:", count)

# another solution using string conversion
from math import *
n = 5433456789
def count_digits(n):
    return int(log10(n)+1)
print("Number of digits:", count_digits(n))