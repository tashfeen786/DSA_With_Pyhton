# This code prints the factors of a given number
# Input: A number from the user
num = int(input("Enter a number: "))
# Code to print factors of a given number
result = []
for i in range(1, num+1):
    if num % i ==0:
        result.append(i)

print("Factors of", num, "are:", result)
# Better solution 

num = int(input("Enter a number: "))
result = []
for i in range(1, num //2):
    if num % i == 0:
        result.append(i)
result.append(num)  # Include the number itself as a factor
print("Factors of", num, "are:", result)
# This code checks if a number is an Armstrong number20

# Optimal solution
num = int(input("Enter a number: "))

result = []
from math import sqrt
for i in range (1, int(sqrt(num)) + 1):
    if num % i ==0:
        result.append(i)
        if num // i !=i:
            result.append(num // i)
print(result)