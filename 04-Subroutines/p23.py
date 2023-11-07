def check(zdanie, litera):
    zdanie = str(zdanie)
    w = zdanie.count(litera)
    return f"{zdanie} \n The number of letter '{litera}': {w}"

print(check("Czesc wchodze na bit elo elo 320", "b"))