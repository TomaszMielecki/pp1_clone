def f(card_number):
    card_number = str(card_number)
    if len(card_number) != 16:
        return "Invalid card number"
    stars = "**********"
    karta = f"{card_number[0]}{card_number[1]}{stars}{card_number[12]}{card_number[13]}{card_number[14]}{card_number[15]}"
    return karta

print(f("1234567891234567"))
