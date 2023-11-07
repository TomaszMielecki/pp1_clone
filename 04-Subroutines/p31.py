def f(x,y):
    
    x=int(x)
    y=int(y)

    m=0

    for number in range(x,y):
        if int(number)<0 and int(number)%2 == 0:
            m = m+1
        else:
            continue
    return m

print(f(-7,8))
print(f(-1,11))