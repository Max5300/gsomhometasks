code = int(input("Введите код города: "))
time = float(input("Введите длительность переговоров в минутах: "))
if code == 343:
    price = 15
elif code == 381:
    price = 18
elif code == 473:
    price = 13
elif code == 485:
    price = 11
print("Стоимость переговоров составила", time * price, "рублей")
