def func(n):
    if n == 1:
        return 1
    return n + func(n - 1)
func(4)
print("Sum of 1 to N using functional recursion is:", func(4))