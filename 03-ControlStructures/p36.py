def f(n):
    koniec = str("")
    i = 0
    while i<10:
        i = i+1
        wynik = n*i
        koniec = koniec+f"{n} x {i} = {wynik} \n" 
    return koniec
    
print(f(6))