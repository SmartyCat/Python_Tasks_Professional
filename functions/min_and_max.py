func = input()
x, y = input().split()
result = [
    (
        eval(func.replace("x", str(i)))
        if i > 0
        else eval(func.replace("x", "(" + str(i) + ")"))
    )
    for i in range(int(x), int(y) + 1)
]
print(
    f"Минимальное значение функции {func} на отрезке [{x}; {y}] равно {min(result)}",
    f"Максимальное значение функции {func} на отрезке [{x}; {y}] равно {max(result)}",
    sep="\n",
)
