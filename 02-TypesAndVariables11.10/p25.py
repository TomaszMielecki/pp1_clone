age = int(input("Enter age: "))

if age <= 26:
    tax = True
else:
    tax = False

print(f"Exemption from paying taxes: {tax}")