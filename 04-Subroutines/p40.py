def f(number):
    number = str(number)
    wynik = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0

    for cyfra in number:
        if cyfra == "1":
            count1+=1
        elif cyfra == "2":
            count2+=2
        elif cyfra == "3":
            count3+=3
        elif cyfra == "4":
            count4+=4
        elif cyfra == "5":
            count5+=5
        elif cyfra == "6":
            count6+=6
        elif cyfra == "7":
            count7+=7
        elif cyfra == "8":
            count8+=8
        elif cyfra == "9":
            count9+=9
        
    
    if count1>1:
        wynik+=count1
    elif count2>2:
        wynik+=count2
    elif count3>3:
        wynik+=count3
    elif count4>4:
        wynik+=count4
    elif count5>5:
        wynik= wynik+count5
    elif count6>6:
        wynik+=count6
    elif count7>7:
        wynik+=count7
    elif count8>8:
        wynik+=count8
    elif count9>9:
        wynik+=count9

    return wynik

print(f(1027))
print(f(230335) )
print(f(513553007) )


        
            

