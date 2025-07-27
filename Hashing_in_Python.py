
# Brute Solution to Count Occurrences of Elements in a List
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10, 1, 1, 1]
m = [10, 111, 1, 9, 5, 67, 2]

for num in m:
    count = 0
    for x in n:
        if x ==num:
            count += 1
    print(f"Number {num} occurs {count} times in the list n.")

print("Optimal solution")
# Optimal Solution to Count Occurrences of Elements in a List using Hashing 
hash_list = {0} * 11
for num in n:
    hash_list[num]+= 1
for num in m:
    if num< 1 or num >10: 
        print(0)
    else:
        print(hash_list[num])



