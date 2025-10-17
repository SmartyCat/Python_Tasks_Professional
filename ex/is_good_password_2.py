from practice import chars, digit


class LengthError(Exception):
    pass


class LetterError(Exception):
    pass


class DigitError(Exception):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    elif not chars(string):
        raise LetterError
    elif not digit(string):
        raise DigitError
    return True


try:
    print(is_good_password("Short7"))
except Exception as err:
    print(type(err))

print(is_good_password("еПQSНгиfУЙ70qE"))

try:
    print(is_good_password("sfgvsDSDFSDFLM"))
except Exception as err:
    print(type(err))
