def f():
    m = str("")
    i = 0
    s = 5
    while i<5:
        i = i+1
        m = m+i*"* "+"\n"
    while i>=5 and i<10:
        i=i+1
        s=s-1
        m= m+s*"* "+"\n"
    return m
print(f())
    


