def f(detector):
    detector = str(detector)
    wynik = 0
    m = 0

    for cyfra in detector:
        if cyfra == "+":
            wynik = wynik+1
            if wynik == 3:
                m=m+1
            else:
                continue
        if cyfra=="-":
            wynik = wynik-1
        

    if m != 0:
        return True
    else:
        return False
        
    
    
    
    
print(f("+-+++-+---") )
print(f("+-+-+-+-") )
print(f("+-++-+--") )
print(f("+-++-++-+---") )