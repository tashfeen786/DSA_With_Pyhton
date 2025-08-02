num = [5, 7, 3,9,5,3, 8,9, 2, 1]
left = 0
right = len(num) - 1
num[left], num[right] = num[right], num[left]
left += 1
right -= 1  

