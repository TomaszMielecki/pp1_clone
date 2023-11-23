def f(sentence):
    sentence = str(sentence)
    wynik=""

    for letter in sentence:
        if letter == " ":
            continue
        else:
            wynik=wynik+str(letter)

    return wynik

print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs") )