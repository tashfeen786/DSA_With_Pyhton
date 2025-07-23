n = 54383456
num = n 
count = 0
while num > 0:
    value = num % 10
    count += 1
    num = num // 10 
print("Number of digits:", count)