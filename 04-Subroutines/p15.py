def keyboard():
    i = 0
    m = str("")

    while i<=3:
        i = i+1
        m = m+str(i)+" "
        if i == 3:
            m = m+"\n"
    while i>3 and i <=6:
        i = i+1
        m = m+str(i)+" "
        if i == 6:
            m = m+"\n"
    while i>6 and i<9:
        i = i+1
        m = m+str(i)+" "
    return m

print(keyboard())