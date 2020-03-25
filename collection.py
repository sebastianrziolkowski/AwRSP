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


matrix_a = [[1, 5, 3], [1, 5, 3], [1, 5, 3]]
matrix_b = [[1, 2, 4], [1, 2, 3], [1, 2, 2]]

show_multi_matrix_result(matrix_a, matrix_b)
print_matrix(add_matrix(matrix_a, matrix_b))
