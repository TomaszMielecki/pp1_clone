def f(n):
    n = int(n)
    n1 = 0
    n2 = 1
    count = 1

    while count < n:
        nth = n1+n2
        n1 = n2
        n2 = nth
        count +=1
    return n1

print(f(5))
print(f(9))

        
        

    


