def exercise_1_1():
    for x in range(5, 10):
        print("Liczba", x)


def exercise_1_2():
    for x in range(2, 20):
        if 0 == x % 2:
            print("Parzysta:", x)


def exercise_1_3():
    max_range = int(input("Wprowadz liczbe:"))
    for x in range(1, max_range + 1):
        print("Liczba:", x)


def exercise_1_4():
    max_range = int(input("Wprowadz liczbe:"))
    sum_number = 0
    for x in range(1, max_range + 1):
        sum_number = sum_number + x
    print("Suma liczb:", sum_number)


def exercise_1_5():
    max_range = int(input("Wprowadz liczbe:"))
    for x in range(1, max_range + 1):
        print(x, "*", x, "=", x * x)


def exercise_1_6():
    max_range = int(input("Wprowadz liczbe:"))
    for x in range(0, max_range):
        print(x * 3)


def exercise_1_7():
    max_range = int(input("Wprowadz liczbe:"))
    result = 0
    for x in range(0, max_range):
        result = result + max_range
    print("Wynik:", result)


def exercise_2_1():
    max_range = int(input("Podaj liczbę:"))
    while int(max_range) < 0:
        max_range = int(input("Spróbuj jeszcze raz:"))
    result = 0
    for x in range(0, max_range):
        result = result + max_range
    print("Wynik:", result)


def exercise_2_2():
    i = 1
    while i < 15:
        print("Liczba:", i)
        i += 1


def exercise_2_3():
    number = int(input("Podaj liczbę:"))
    i = 1
    while i < number:
        print("Liczba:", i)
        i += 1


def exercise_2_4():
    start_number = int(input("Podaj dolna liczbe:"))
    stop_number = int(input("Podaj gorna liczbę:"))
    i = start_number
    while i < stop_number:
        print("Liczba:", i)
        i += 1


def exercise_2_5():
    start_number = int(input("Podaj dolna liczbe:"))
    stop_number = int(input("Podaj gorna liczbę:"))
    while stop_number < start_number:
        start_number = int(input("Podaj ponownie dolna liczbe:"))
        stop_number = int(input("Podaj ponownie gorna liczbę:"))
    i = start_number
    while i < stop_number:
        print("Liczba:", i)
        i += 1


def exercise_2_6():
    month = int(input("Podaj numer miesiaca:"))
    while 12 < month or 0 > month:
        month = int(input("Podaj ponownie numer miesiaca:"))
    if month == 1:
        print("Styczen")
    elif month == 2:
        print("Luty")
    elif month == 3:
        print("Marzec")
    elif month == 4:
        print("Kwiecien")
    elif month == 5:
        print("Maj")
    elif month == 6:
        print("Czerwiec")
    elif month == 7:
        print("Lipiec")
    elif month == 8:
        print("Sierpien")
    elif month == 9:
        print("Wrzesien")
    elif month == 10:
        print("Pazdziernik")
    elif month == 11:
        print("Listopad")
    elif month == 12:
        print("Grudzien")
    else:
        print("Zly numer miesiaca")


def exercise_2_7():
    number = int(input("Podaj liczbe:"))
    sum = 0
    counter = 0
    while 0 != number:
        sum = sum + number
        counter += 1
        number = int(input("Podaj liczbe ponownie:"))
    print("Sum:", sum)
    print("Avg:", sum / counter)


def exercise_2_8():
    number = int(input("Podaj dlugosc boku kwadratu:"))
    while number < 0:
        number = int(input("Podaj dlugosc ponownie:"))
    print("Pole:", number * number)
    print("Obwod:", number * 4)


def exercise_3_1():
    for i in range(0, 5):
        symbol = "#"
        for j in range(0, 5):
            print(symbol, end='')
        print()


def exercise_3_2():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i, "*", j, "=", i * j, end='\t\t')
        print()


def exercise_3_3():
    counter = 0
    for i in range(0, 10):
        counter += 1
        for j in range(0, counter):
            print("*", end='')
        print()


def exercise_3_4():
    counter = 11
    for i in range(0, 10):
        counter -= 1
        for j in range(0, counter):
            print("*", end='')
        print()


def exercise_3_5():
    symbol = input("Wprowadz znak:")
    counter = 0
    for i in range(0, 10):
        counter += 1
        for j in range(0, counter):
            print(symbol, end='')
        print()


def exercise_3_6_1():
    number = int(input("Tabliczka mnozenia do liczny: "))
    for i in range(1, number + 1):
        for j in range(1, 11):
            print(i, "*", j, "=", i * j, end='\t\t')
        print()


def exercise_3_6_2():
    symbol = input("Wprowadz znak:")
    number = int(input("Wprowadz wysokosc:"))
    counter = 0
    for i in range(0, number):
        counter += 1
        for j in range(0, counter):
            print(symbol, end='')
        print()


def exercise_3_7():
    number = input("Wprowadz liczbe do sprawdzenia:")
    counter = 0
    result = 0
    while counter < len(number):
        result = result + int(number[counter]) ** 3
        counter += 1
    if result == int(number):
        print("Jest to liczba armstronga")
    else:
        print("Nie jest to liczba armstronga")


exercise_3_7()
