
def func(sum, i, n):
    if i > n:
        print("Sum of 1 to", n, "is", sum)
        return
    func(sum+i, i + 1, n)

func(0, 1, 4)