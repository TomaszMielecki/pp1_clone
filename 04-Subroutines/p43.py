def f(name):
    name=str(name)

    wynik=name[0]+""

    spacja = name.find(" ")
    pierwsza=spacja+1
    wynik=wynik+str(pierwsza)

    return wynik

    

print(f("Internet of Things") )