num = [5, 7, 3,9,5,3, 8,9, 2, 1]
def func(num, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    func(arr, left + 1, right - 1)
def reverse_array(num, left, right):
    self.func(num, 0, len(num) - 1)
    return num

print(num)