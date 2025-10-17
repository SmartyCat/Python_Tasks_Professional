def func(l):
    def another(index):
        if index < len(l):
            print(f"Элемент {index}: {l[index]}")
            another(index + 1)

    another(0)


l = [1, 2, 3, 4, 5]
func(l)
