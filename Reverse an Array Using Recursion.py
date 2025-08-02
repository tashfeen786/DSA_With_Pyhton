num = [5, 7, 3,9,5,3, 8,9, 2, 1]
def func(num, left, right):
    if left >= right:
        return
    num[left], num[right] = num[right], num[left]
    func(num, left + 1, right - 1)
    return num
var = func(num, 0, len(num) - 1)
print(var)  # Output: [1, 2, 9, 8,

