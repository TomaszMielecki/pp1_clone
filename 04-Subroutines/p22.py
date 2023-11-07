def month(n):
    months = ['Styczen','Luty',"Marzec","kwiecien","maj","czerwiec","lipiec","sierpien","wrzesien","pazdziernik","listopad","grudzien"]
    return f"The name of month {n} is "+months[n-1]

u = int(input("Enter month number: "))
print(month(u))