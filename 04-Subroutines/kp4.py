def f(w):
    w = str(w)
    dl = len(w)

    wynik=""
    count=0

    for letter in w:
        count=count+1
        if count == 1 and dl>1:
            wynik=wynik+str(letter)+"+"
        elif count>1 and count<dl and count%2==0:
            wynik=wynik+str(letter)+"-"
        elif count>1 and count<dl and count%2!=0:
            wynik=wynik+str(letter)+"+"
        elif count == dl:
            wynik=wynik+str(letter)
    return wynik

print(f("abcdfghi"))
print(f("xyz"))
print(f("k"))
print(f(""))

