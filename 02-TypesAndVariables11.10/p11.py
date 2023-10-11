father = int(input("Enter fathers income :"))
mother = int(input("Enter mothers income: "))
people = int(input("Enter number of people in family: "))
income = int(father+mother)
incomeperson = income/people

print(f"Total income: {income}")
print(f"Income per person: {incomeperson}")