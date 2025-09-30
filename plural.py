def choose_plural(amount, declensions):
    s = str(amount)
    d = {
        (11, 12, 13, 14): s + " " + declensions[2],
        (1,): s + " " + declensions[0],
        (2, 3, 4): s + " " + declensions[1],
        (5, 6, 7, 8, 9, 0): s + " " + declensions[2],
        
    }
    for i in d:
        if int(s[-2:]) in i or int(s[-1]) in i:
            return d[i]


print(choose_plural(21, ("пример", "примера", "примеров")))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(112, ('яблоко', 'яблока', 'яблок')))