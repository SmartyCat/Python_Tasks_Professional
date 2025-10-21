from test import chars, dig


def verification(login, password, success, failure):
    if not chars(password):
        failure(login, "в пароле нет ни одной буквы")
    elif password.lower() == password:
        failure(login, "в пароле нет ни одной заглавной буквы")
    elif password.upper() == password:
        failure(login, "в пароле нет ни одной строчной буквы")
    elif not dig(password):
        failure(login, "в пароле нет ни одной цифры")
    else:
        success(login)
