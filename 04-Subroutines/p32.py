def f(n1,n2,n3):
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

    if n1<0 or n2<0 or n3<0:
        return True
    else:
        return False
    
print(f(11,6,-4))
print(f(5,4,14))
print(f(5,3,1))