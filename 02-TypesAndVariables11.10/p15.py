celcius = int(input("Podaj temperature w Celcjuszach: "))

#Temperatura w kelvinach liczy się od zera absolutnego czyli -273C

kelvin = celcius + 273

#Fahrenheit ma swoj schemat na przeliczanie

fahrenheit = celcius*9/5 + 32

print(f"Temperature in Kelvins is {kelvin} and in Fahrenheit is {fahrenheit}")