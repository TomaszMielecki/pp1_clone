def f(t,c,n):
    t=str(t)
    c=str(c)
    n=int(n)

    liczba=0

    for letter in t:
        if letter == c:
            liczba=liczba+1
        else:
            continue

    if liczba == n:
        return True
    else:
        return False
    
print(f("abc","b",1))
print(f("xxaxxbxx","x",6))
print(f("qwerty","b","0"))
print(f("abcdef","b",2))
print(f("book","o",1))


