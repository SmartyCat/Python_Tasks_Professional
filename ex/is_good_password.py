def is_good_password(string):
    if (
        len(string) < 9  # не критикуй , для тренировки в самый раз, все в одном условии
        or string.isdigit()
        or string.isalpha()
        or string == string.lower()
        or string == string.upper()
    ):
        return False

    return True


print(is_good_password("41157082"))
print(is_good_password("Мойпарольсамыйлучший1"))
print(is_good_password("МойПарольСамыйЛучший111"))
