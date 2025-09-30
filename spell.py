def spell(*args):
    args = tuple(map(lambda x: x.lower(), args))
    return {i[0]: max([len(j) for j in args if i[0] == j[0]]) for i in args}


words = ["россия", "Австрия", "австралия", "РумыниЯ", "Украина", "КИТай", "УЗБЕКИСТАН"]
print(spell(*words))
print(spell("Математика", "История", "химия", "биология", "Информатика"))
words = ["fruit", "football", "February", "forest", "Family"]
print(spell(*words))
print(spell())