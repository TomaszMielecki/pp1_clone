name = input("What is your name?")
age = input("What is your age?")
height = input("What is your height?")
age6= input("How old will you be in 6 years?")

x = 'My name is {}. I am {} yo, and my height is {}. In 6 yo ill be {}'

#print(f"My name is {name}, I am {age} years old, and my height is {height}cm. In 6 years I will be {age6} years old.")

print(x.format(name, age, height, age6))