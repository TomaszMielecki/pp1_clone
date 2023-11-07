def f(n):
    pierwsza = 2
    druga = 15
    if n>=pierwsza and n<=druga:
        return True
    else:
        return False
    
w = int(input('A number: '))

if f(w) == True:
    answer = "yes"
elif f(w) == False:
    answer = "no"

print(f"Number 7 in the range <2,15>: {answer}")