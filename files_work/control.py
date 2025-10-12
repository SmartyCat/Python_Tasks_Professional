import pickle


def control(filename, number):
    with open(filename, "rb") as file:
        data = pickle.load(file)
        if isinstance(data, dict):
            result = sum(d for d in data if isinstance(d, int))
        else:
            result = [d for d in data if isinstance(d, int)]
            if result:
                result = min(result) * max(result)
        return (
            "Контрольные суммы совпадают"
            if result == number
            else "Контрольные суммы не совпадают"
        )


print(control(input(), int(input())))
