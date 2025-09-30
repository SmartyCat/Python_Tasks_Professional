def likes(names):
    d = {
        0: "Никто не оценил данную запись",
        1: f"{names[0]} оценил(а) данную запись" if len(names) == 1 else None,
        2: (
            f"{names[0]} и {names[1]} оценили данную запись"
            if len(names) == 2
            else None
        ),
        3: (
            f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
            if len(names) == 3
            else None
        ),
    }
    return (
        d[len(names)]
        if len(names) in d
        else f"{names[0]}, {names[1]} и {len(names)-2} оценили данную запись"
    )


print(likes(["Дима", "Алиса"]))
print(likes(["Эндрю", "Тоби", "Том"]))
print(likes([]))
