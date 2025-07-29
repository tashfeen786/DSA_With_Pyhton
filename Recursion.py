count = 0
def func():
    if count == 4:
        return
    print("Tashfeen")
    count += 1
    func()
func()
