def different(n1,n2,n3):
    if n1==n2==n3:
        return False
    else:
        return True

n1 = input("Enter first number: ...")
n2 = input("Enter second number: ...")
n3 = input("Enter third number: ...")

if different(n1,n2,n3)==True:
    print(f"Numbers {n1}, {n2} and {n3} are different")
else:
    print(f"Numbers {n1}, {n2} and {n3} are not different")

