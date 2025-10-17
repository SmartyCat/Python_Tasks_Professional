l = []
while True:
    l.append(int(input()))
    if l[-1] == 0:
        break


def func(l):
    def another(n):
        if n > -1:
            print(l[n])
            another(n - 1)

    another(len(l) - 1)


func(l)
