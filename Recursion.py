count = 0
def func():
    global count
    if count == 4:
        return
    print("Tashfeen")
    count += 1
    func()
func()
