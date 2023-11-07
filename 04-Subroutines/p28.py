def f(binary_number):
    binary_number = str(binary_number)
    m = 0
    for letter in binary_number:
        if letter == "1" or letter == "0":
            continue
        else:
            m = m+1
    if m==0:
        return True
    else:
        return False
    

            
   
        
    
print(f(0))
print(f(11111))
print(f("101010101"))
print(f("0011111"))
print(f("13a234"))
print(f("000000002"))