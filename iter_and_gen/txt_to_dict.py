def txt_to_dict():
    with open("/home/kostya/Загрузки/planets.txt", "r", encoding="utf-8") as file:
        data = "".join(i if not i.isspace() else "," for i in file.readlines()).split(
            ","
        )
        return (
            {i.split(" = ")[0]: i.split(" = ")[1] for i in d.split("\n") if "=" in i}
            for d in data
        )


planets = txt_to_dict()
print(*planets)
