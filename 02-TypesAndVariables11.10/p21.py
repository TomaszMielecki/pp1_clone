heightcm = int(input("Enter your height in cm: "))

foot = int(heightcm//30.48)
inch = int(heightcm/2.5)
inchrest = int(inch%30.48)

print(f"Your height in cm is: {heightcm}, or {foot} feet and {inchrest} inches")