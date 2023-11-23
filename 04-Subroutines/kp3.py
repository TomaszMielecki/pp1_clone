def f(p):
    if len(p)>=6:
        for x in range(len(p)):
            if p.count(p[x])>1:
                return False
        return True
    else:
        return False
    
print(f("ax15"))
print(f("book123"))
print(f("A2water3"))