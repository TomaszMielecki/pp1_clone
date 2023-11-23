def f(text):
    text = str(text)

    wynik= ""

    for letter in text:
        if letter == text[0]:
            wynik=wynik+str(letter)
        else:
            wynik=wynik+"-"+str(letter)
    return wynik

print(f("Univesity") )
print(f("UE") )
print(f("x"))
print(f(""))