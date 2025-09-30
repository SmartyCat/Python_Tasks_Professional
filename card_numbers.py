def hide_card(card_number):
    card_number = card_number.replace(" ", "")
    return "*" * 12 + card_number[12:]


card = "1234567890123456"
print(hide_card(card))
card = "3456 9012 5678 1234"
print(hide_card(card))
