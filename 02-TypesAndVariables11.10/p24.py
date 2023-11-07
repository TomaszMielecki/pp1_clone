vehicle = str(input("Enter vehicle registration number: "))

letter1 = vehicle[0]
letter2 = vehicle[1]

if letter1 == "K" and letter2 == "R" or letter1 == "K" and letter2 == 'K':
    car = True
else:
    car = False

print(f"Car is from Cracow: {car}")