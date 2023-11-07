def f():
    m = str("")
    for i in range(1,31):
        if i%3 == 0 and i%5 != 0:
            m = m +"THREE "
        elif i%5 == 0 and i%3 !=0:
            m = m +"FIVE "
        elif i%5 == 0 and i%3 == 0:
            m = m+"BINGO "
        else:
            m = m+str(i)+ " "
    return m

print(f())