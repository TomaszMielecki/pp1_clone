import random

r = random.randint(1,9)

u = int(input("Enter a number: "))

print(f"Computer number: {r}")

if r == u:
    print("You won the game!!")
else:
    print("You loose :(")