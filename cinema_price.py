def price(film, time):
    if film == "Пятница":
        if time == 12:
            return 250
        elif time == 16:
            return 350
        elif time == 20:
            return 450
    elif film == "Чемпионы":
        if time == 10:
            return 250
        elif time == 13 or time == 16:
            return 350
    elif film == "Пернатая банда":
        if time == 10:
            return 350
        elif time == 14 or time == 18:
            return 450

print("Программа для подсчета стоимости билетов в кино.")
film = input("Выбрать фильм: ")
date = input("Выбрать день (сегодня, завтра): ")
time = int(input("Выбрать время: "))
people = int(input("Выбрать количество билетов: "))
if price(film, time) == None:
    print("Ошибка ввода.")
else:
    if people >= 20:
        print("Выбрали фильм:", film, "День:", date, "Время:", time, "Количество билетов:", people)
        print("Результат:", 0.8 * price(film, time) * people, "руб.")
    elif 1 <= people < 20:
        if date == "завтра":
            print("Выбрали фильм:", film, "День:", date, "Время:", time, "Количество билетов:", people)
            print("Результат:", 0.95 * price(film, time) * people, "руб.")
        elif date == "сегодня":
            print("Выбрали фильм:", film, "День:", date, "Время:", time, "Количество билетов:", people)
            print("Результат:", price(film, time) * people, "руб.")
        else:
            print("Ошибка ввода.")
    else:
        print("Ошибка ввода.")
