from random import randint


def exercise_1():
    shopping = ['sugar', 'butter', 'flour', 'cream', 'bread']
    print('First shopping list item:', shopping[0])
    print('Second shopping list item:', shopping[1])
    shopping[2] = 'butter'
    print('Last shopping list item:', shopping[-1])
    print('Second last shopping list item:', shopping[-2])


def exercise_2():
    winter_semester = ['Bazy danych', 'Etyka', 'Inzynieria oprogramowania', 'Teoria grafów i sieci',
                       'Algorytmy i struktury danych']
    print(winter_semester)

    summer_semester = ['Zarządzanie projektem informatycznym', 'Bazy danych II', 'Praktyka programowania',
                       'Laboratorium programowania: aplikacje w różnych środowiskach programistycznych']
    print(summer_semester)

    search_subject = input("Write subject to search:")

    if search_subject in winter_semester:
        print('Przedmiot z semestru zimowego')
    elif search_subject in summer_semester:
        print('Przedmiot z semestru letniego')
    else:
        print('Nie ma takiego przedmiotu na pierwszym roku studiów')

    first_year = winter_semester + summer_semester
    print('First year:', first_year)


def exercise_3():
    books = []
    books.append('A TIME TO KILL')
    books.append('EAST OF EDEN')
    books.append('A SCANNER DARKLY')
    books.append('NUMBER THE STARS')
    books.sort()
    print('First element:', books[0])
    print('Last element:', books[-1])
    print('Second last element:', books[-2])


def exercise_4():
    movie_title = ['Whispering Sons', 'The Hidden Snow', 'Word of Guardian', 'The Ends Lover', 'The Snow of the Swords',
                   'Spirit in the Heat',
                   'Trembling Teacher', 'The Silver Slaves', 'Dreams of Door', 'The Darknesss Healer']

    movie_title[3] = 'none'
    movie_title[4] = 'The Something of the Moons'
    movie_title.pop(6)
    print('Movie list:', movie_title)
    movie_title.insert(0, 'fav_movie_3')
    movie_title.insert(0, 'fav_movie_2')
    movie_title.insert(0, 'fav_movie_1')
    print('Movie list:', movie_title)
    movie_title.remove('The Something of the Moons')
    movie_title.remove('The Silver Slaves')
    print('Movie list:', movie_title)
    movie_title.clear()

    movie_title.append('Diamond Time')
    movie_title.append('The Obsessed Visions')
    movie_title.append('Princess of Butterfly')
    movie_title.append('The Game`s Princess')
    movie_title.append('The Truth of the Mage')
    movie_title.append('Star of Rose')
    movie_title.append('Storms in the Scent')

    movie_title[-1] = 'New_movie_title'

    print('First movie title:', movie_title[0])
    print('Second movie title:', movie_title[1])
    print('Third movie title:', movie_title[2])
    print('Last movie title:', movie_title[-1])
    print('Second last movie title:', movie_title[-2])
    print('Third last movie title:', movie_title[-3])

    if input('Write movie title:') in movie_title:
        print('This movie is in your list')
    else:
        print('I can`t find this movie')

    movie_title.append(input("Write first movie title:"))
    movie_title.append(input("Write second movie title:"))
    movie_title.append(input("Write third movie title:"))
    movie_title.append(input("Write fourth movie title:"))
    movie_title.sort()
    print(movie_title)
    movie_title.sort(reverse=True)
    print(movie_title)


def exercise_5():
    grades = [5.5, 4.5, 3.25, 5.25, 2.5, 2, 2, 5, 5]
    grades_semester_2 = [5.5, 2.5, 2, 2, 5, 5, 3.25, 5.25, 4.5, 5.25, 3.25, 2.25]
    grades.extend(grades_semester_2)
    print('Grades:', grades)
    add_grades = 0
    for grade in grades:
        add_grades = add_grades + grade
    print('Average of grades: {:.2f}'.format(add_grades / len(grades)))

    try:
        search_grade = float(input('Write grade to find:'))
        if grades.index(search_grade):
            print(grades.index(search_grade))
    except ValueError:
        print('Grade not found.')


def exercise_6():
    female_names = ['ala', 'lena', 'natalia', 'paulina', 'zofia']
    male_names = ['kuba', 'adrian', 'michal', 'filip', 'adam']

    male_names.append('sebastian')
    male_names.insert(1, 'example_name1')
    male_names.insert(2, 'example_name2')

    female_names.sort()
    male_names.sort()
    print(female_names)
    print(male_names)

    names = female_names + male_names
    names.sort()
    print(names)


def exercise_7():
    def equipment_info(hero):
        print('Amount of equipment items: ', len(hero.equipment))
        print('Items in equipment:', hero.equipment)

    def open_chest(hero, chest_to_open):
        print('You found', end=' ')
        for item_in_chest in chest_to_open:
            print(item_in_chest, end=' ')
            hero.equipment.append(item_in_chest)
        print('in chest.')
        chest_to_open.clear()

    def use_item_from_equipment(hero, item_to_use):
        if item_to_use in hero.equipment:
            print("You use", item_to_use)
            hero.equipment.remove(item_to_use)
        else:
            print("You don't have this item.")

    def change_item(hero, item_to_exchange, item_to_add):
        if item_to_exchange in hero.equipment:
            hero.equipment.remove(item_to_exchange)
            hero.equipment.append(item_to_add)
            print(item_to_add, 'added to equipment for', item_to_exchange)
        else:
            print(item_to_exchange, ' not found in equipment.')

    def fall_into_trap(hero_, damage):
        if hero_.health_points > 0:
            hero_.health_points = hero_.health_points - damage
            if hero_.health_points < 0:
                print('You are death.')
                del hero_
            else:
                print('You lose', damage, 'health.')

    class Heroes:
        equipment = ['healing potion', 'sword', 'armor', 'shield']
        health_points = 100

        def drink_potion(self):
            potion = 'healing potion'
            heal_value = 35
            if potion in self.equipment:
                self.health_points += heal_value
                print('You use', potion, 'and heal for', heal_value,
                      'heal points', 'your health now is', self.health_points)
                self.equipment.remove(potion)
            else:
                print("You don't have any potion.")

    black_knight = Heroes()

    chest = ['gold', 'magic ball']
    equipment_info(black_knight)

    print('Items found in chest:', chest)
    open_chest(black_knight, chest)
    equipment_info(black_knight)

    use_item_from_equipment(black_knight, 'healing potion')
    change_item(black_knight, 'magic ball', 'healing potion')

    chest.append('food')
    open_chest(black_knight, chest)

    equipment_info(black_knight)

    fall_into_trap(black_knight, 80)
    black_knight.drink_potion()
    fall_into_trap(black_knight, 35)
    fall_into_trap(black_knight, 30)


def exercise_8():
    def below_and_above_average(array):
        average = sum(array) / len(array)
        above = []
        below = []
        for point in array:
            if point > average:
                above.append(point)
            else:
                below.append(point)
        print('Above average:', len(above))
        print('Above list:', above)
        print('Below average:', len(below))
        print('Below list:', below)

    points = []
    print()
    for x in range(15):
        points.append(randint(0, 100))

    for x in range(5):
        points.append(randint(0, 100))

    points.sort()
    print(points)

    search_point = int(input("Write points to search:"))

    if search_point in points:
        print(search_point, 'is in points array.')
    else:
        print(search_point, 'not found in array.')

    print('Avg value of points:', sum(points) / len(points))
    below_and_above_average(points)

    points.clear()
    for x in range(15):
        points.append(randint(0, 100))
    for x in range(5):
        point_to_input = int(input("Write points value:"))
        while 0 > point_to_input or point_to_input > 100:
            point_to_input = int(input("Wrong input value, try again:"))
        points.append(point_to_input)

    points.sort()
    print(points)


def exercise_9():
    def more_than_input(income_list, value):
        amount = 0
        for item in income_list:
            if value < item:
                amount += 1
        return amount

    monetary_income_2018 = []
    monetary_income_2019 = []
    monetary_income_2020 = []

    for i in range(12):
        monetary_income_2018.append(randint(2300, 3500) + randint(1, 99) / 100)
        monetary_income_2019.append(randint(2300, 3500) + randint(1, 99) / 100)

    for j in range(4):
        monetary_income_2020.append(randint(2300, 3500) + randint(1, 99) / 100)

    monetary_income_by_year = [sum(monetary_income_2018), sum(monetary_income_2019), sum(monetary_income_2020)]
    avg_monetary_income_by_year = [sum(monetary_income_2018) / len(monetary_income_2018),
                                   sum(monetary_income_2019) / len(monetary_income_2019)
        , sum(monetary_income_2020) / len(monetary_income_2020)]

    print('Monetary income in 2018:', monetary_income_2018)
    print('Monetary income in 2019:', monetary_income_2019)
    print('Monetary income in 2020:', monetary_income_2020)

    print('Sum of monetary income in 2018: {:.2f}'.format(sum(monetary_income_2018)))
    print('Sum of monetary income in 2019: {:.2f}'.format(sum(monetary_income_2019)))
    print('Sum of monetary income in 2020: {:.2f}'.format(sum(monetary_income_2020)))

    print('Sum of monetary income from 2018 to now:', sum(monetary_income_by_year))

    print('Average monetary income in 2018: {:.2f}'.format(sum(monetary_income_2018) / len(monetary_income_2018)))
    print('Average monetary income in 2019: {:.2f}'.format(sum(monetary_income_2019) / len(monetary_income_2019)))
    print('Average monetary income in 2020: {:.2f}'.format(sum(monetary_income_2020) / len(monetary_income_2020)))

    print('Largest monetary income was in', 2018 + monetary_income_by_year.index(max(monetary_income_by_year)))
    print('Largest avg monetary income was in',
          2018 + avg_monetary_income_by_year.index(max(avg_monetary_income_by_year)))

    user_input = float(input("Input:"))

    print('Largest than input in 2018:', more_than_input(monetary_income_2018, user_input))
    print('Largest than input in 2019:', more_than_input(monetary_income_2019, user_input))
    print('Largest than input in 2020:', more_than_input(monetary_income_2020, user_input))

    monetary_income_2018_I = monetary_income_2018[:3]
    monetary_income_2018_II = monetary_income_2018[3:6]
    monetary_income_2018_III = monetary_income_2018[6:9]
    monetary_income_2018_VI = monetary_income_2018[9:12]

    print(monetary_income_2018_VI)

    print('Sum in I quarter:: {:.2f}'.format(sum(monetary_income_2018_I)))
    print('Sum in II quarter:: {:.2f}'.format(sum(monetary_income_2018_II)))
    print('Sum in III quarter:: {:.2f}'.format(sum(monetary_income_2018_III)))
    print('Sum in VI quarter:{:.2f}'.format(sum(monetary_income_2018_VI)))


def exercise_10():
    incoming_transfers = []
    for i in range(10):
        incoming_transfers.append(randint(2300, 3500) + randint(1, 99) / 100)

    print('Numbers of incoming transfers:', len(incoming_transfers))

    for i in range(6):
        incoming_transfers.append(float(input("Write new transfer value:")))

    print('Update numbers of incoming transfers:', len(incoming_transfers))
    print('Sum:', sum(incoming_transfers), 'avg:', sum(incoming_transfers) / len(incoming_transfers))

    incoming_transfers.sort()
    incoming_transfers.reverse()
    print('Value higher than avg:', end='')
    for item in incoming_transfers:
        if item > sum(incoming_transfers) / len(incoming_transfers):
            print(item, end=', ')
    print()
    incoming_transfers.reverse()
    print('Value lower than avg:', end='')
    for item in incoming_transfers:
        if item < sum(incoming_transfers) / len(incoming_transfers):
            print(item, end=', ')
    print()

    search_incoming_transfer = float(input("Value to search"))
    if search_incoming_transfer in incoming_transfers:
        print(search_incoming_transfer, 'is incoming transfer')
    else:
        print(search_incoming_transfer, 'not found in incoming transfer')


# - - - - - - - - - - Homework - - - - - - - - - - #

def is_matrix_square(matrix):
    for column in matrix:
        if len(column) != len(matrix):
            return False
    return True


def add_matrix(matrix_1, matrix_2):
    if is_matrix_square(matrix_1) and is_matrix_square(matrix_2) and len(matrix_1).__eq__(matrix_2):
        x = 0
        for x in range(len(matrix_1)):
            y = 0
            for y in range(len(matrix_1[x])):
                matrix_1[x][y] = matrix_1[x][y] + matrix_2[x][y]
                y = y + 1
        x = x + 1
    else:
        print('Wrong input matrix.')
        return -1
    print('Result of adding matrix:')
    return matrix_1


def multi_matrix(matrix_1, matrix_2):
    result_matrix = [[] for i in range(len(matrix_1))]
    for new_row in result_matrix:
        for i in range(len(matrix_2[0])):
            new_row.insert(0, 0)

    for check_row in matrix_1:
        if len(check_row) != len(matrix_2):
            return -1
    j = 0
    i = 0
    while j < len(matrix_1):
        y = 0
        new_element = 0
        for y in range(len(matrix_1[0])):
            new_element = new_element + (matrix_1[j][y] * matrix_2[y][i])
            result_matrix[j][i] = new_element
            y = y + 1
        i = i + 1
        if i == len(matrix_2[0]):
            i = 0
            j = j + 1
    return result_matrix


def show_multi_matrix_result(matrix_1, matrix_2):
    print('First matrix:')
    print_matrix(matrix_1)
    print('Second matrix:')
    print_matrix(matrix_2)
    print('Multiplication result:')
    print_matrix(multi_matrix(matrix_1, matrix_2))


def print_matrix(matrix):
    if matrix != -1:
        x = 0
        for x in range(len(matrix)):
            y = 0
            for y in range(len(matrix[x])):
                print(matrix[x][y], end=',')
                y = y + 1
            print()
        x = x + 1
    else:
        print('Can`t draw matrix')

# matrix_a = [[1, 5, 3], [1, 5, 3], [1, 5, 3]]
# matrix_b = [[1, 2, 4], [1, 2, 3], [1, 2, 2]]
#
# show_multi_matrix_result(matrix_a, matrix_b)
# print_matrix(add_matrix(matrix_a, matrix_b))
