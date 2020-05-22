import math

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("You can't divide by 0!")
        return 0
    else:
        return a / b


def platon(n):
    if 0 <= n < 10:
        result = math.factorial(n)
        if n < 7:
            print("Not enough inhabitants: " + str(result))
        elif n > 7:
            print("Too many inhabitants: " + str(result))
        else:
            print("Perfect!  " + str(result))
    else:
        print("Input out of range!")


def pythagoras(a, b, c):
    sideLengths = [a, b, c]
    sideLengths.sort()
    result = sideLengths[0] ** 2 + sideLengths[1] ** 2
    if result == sideLengths[2] ** 2:
        print('This is pythagoras triangle. ' + str(sideLengths))
    else:
        print('This isn`t pythagoras triangle. ' + str(sideLengths))


def login(inputPassword):
    defaultPassword = "admin123"
    resultList = []
    if inputPassword == defaultPassword:
        print("Password correct")
    else:
        for char in inputPassword:
            if defaultPassword.find(char) == -1:
                resultList.append(char)
        print("Wrong password! This characters not needed: " + str(resultList))


def eur_to_pln(a=1):
    driver = webdriver.Chrome("E:\\Python\\chromedriver.exe")
    driver.get(
        "https://www.google.com/search?q=euro+kurs&oq=euro+kurs&aqs=chrome..69i57j0l7.3169j1j7&sourceid=chrome&ie=UTF-8")
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    start_cut = "data-value="
    end_cut = ">"
    euro_exchange_rate = soup.find_all('span', class_='DFlfde SwHCTb')
    print(a * float(str(euro_exchange_rate)[
                    str(euro_exchange_rate).index(start_cut) + len(start_cut) + 1:str(euro_exchange_rate).index(
                        end_cut) - 1]))


def BMI(weight, hight):
    return round(weight / (hight / 100) ** 2, 2)


def exercise_7(a, b):
    result = 0
    for x in range(a ** b):
        result = result + x
    return result


def exam_result(points):
    if 0 <= points <= 100:
        if points <= 50:
            print("Result: 2")
        elif points <= 70:
            print("Result: 3")
        elif points <= 90:
            print("Result: 4")
        else:
            print("Result: 5")
    else:
        print("Points amount out of range!")


def show_number(a, b, c, parameter):
    number_list = [a, b, c]
    number_list.sort()
    if parameter == "DESC":
        print(str(number_list))
    elif parameter == "ASC":
        number_list.reverse()
        print(str(number_list))
    else:
        print("Wrong parameter!")


def PKP(km):
    if 0 < km <= 10:
        return 20
    elif 11 <= km <= 30:
        return 10 + km * 0.1
    elif 30 < km:
        return 1 + 0.08 * km
    else:
        return 0


def office_open_time(day):
    switcher = {
        1: "Pn: 10 – 14",
        2: "Wt: 10 – 19",
        3: "Śr – Pt: 11 – 16",
        4: "Śr – Pt: 11 – 16",
        5: "Śr – Pt: 11 – 16",
        6: "So – Nd: Nieczynne",
        7: "So – Nd: Nieczynne",
    }
    print(switcher.get(day, "Invalid day"))


def exercise_12(n):
    list_of_number = []
    for x in range(n):
        list_of_number.append(x + 1)
    print("Elements: " + str(list_of_number))
    print("Add: " + str(sum(list_of_number)))


def exercise_13(string: str, char) -> int:
    result = 0
    for element in string:
        if element == char:
            result = result + 1
    return result


def exercise_14(string: str) -> int:
    result = 0
    for element in string:
        if string.count(element) == 1:
            result += 1
    return result


def exercise_15(string_list: list) -> list:
    shorterString = string_list[0]
    longerString = string_list[0]
    for element in string_list:
        if len(element) > len(longerString):
            longerString = element
        if len(element) < len(shorterString):
            shorterString = element
    return [shorterString, longerString]


def exercise_16(person_list: list, cars_list: list) -> dict:
    if len(person_list) != len(cars_list):
        return []
    else:
        return {person_list.pop(0): cars_list.pop(0) for i in range(len(cars_list))}


def exercise_17(int_list: list) -> int:
    result = 0
    for element in int_list:
        result += element
    return result


def exercise_18(int_list: list) -> float:
    return exercise_17(int_list) / len(int_list)


def exercise_19(*arguments: int) -> int:
    result = 0
    for number in arguments:
        result += number
    return result


def exercise_20(phone_numbers: list) -> dict:
    global contact
    for number in phone_numbers:
        name = input()
        contact = {name: name}
    return contact


def exercise_21(dic: dict, numb: int):
    for x in dic:
        if dic[x] > numb:
            print(x)


# dictionary = {
#    "szesc": 6,
#    "piec": 5,
#    "cztery": 4,
#    "trzy": 3
# }

# exercise_21(dictionary, 4)

def exercise_22(set_1: set, set_2: set):
    for element in set_1:
        if element in set_2:
            print(element + " exist in set_2")


def exercise_23(list_: list):
    for element in list_:
        print("Hello " + element)


def exercise_24(list_1: list, list_2: list) -> dict:
    return {list_1.pop(0): list_2.pop(0) for i in range(len(list_1))}


def exercise_25(invoice_amounts: list, number: float) -> list:
    list_ = []
    for element in invoice_amounts:
        if element > number:
            list_.append(element)
    return list_


def exercise_26(*arguments: str) -> str:
    result = arguments[0]
    for string in arguments:
        if len(string) > len(result):
            result = string
    return result


def exercise_27(number_: int) -> bool:
    res = [int(x) for x in str(number_)]
    result = 0
    for element in res:
        result += element ** 3
    if result == number_:
        return True
    else:
        return False
