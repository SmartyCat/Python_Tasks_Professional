def clock(number, count):
    if count >= 4:
        print(str(number) * count)
        clock(number + 1, count - 4)
        if count != 4:
            print(str(number) * (count))


clock(1, 16)
