def func(i, n):
    if i>n:
        return
    func(i+1, n)
    print(i)

func(1, 4)

def func1(n):
    if n == 0:
        return
    print(n)
    func1(n-1)

func1(4)

print("Using Backtracking: Print 1 to N in reverse order")
def func2(n):
    if n == 0:
        return
    func2(n - 1)
    print(n)
func2(4)