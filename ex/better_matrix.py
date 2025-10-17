from is_good_password_2 import is_good_password

while True:
    s = input()
    try:
        if is_good_password(s):
            print("Success!")
            break
    except Exception as e:
        print(e)
