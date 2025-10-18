def frogs(n):
    if n == 1:
        return 77
    else:
        return  3*(frogs(n-1)-30)
    
print(frogs(int(input())))    