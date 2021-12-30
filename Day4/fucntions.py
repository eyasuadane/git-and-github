#What are functions

print('Hello world'.split())

def name_of_func():
    print('This is a func and its name_of_func')
name_of_func()

def do_something():
    print('I am doing something')
do_something()

'''def get_person_info():
    first_name = input('What is your first name? ')
    last_name = input('What is your last name? ')
    country = input('Where are you from? ')
    city = input('What is the capital city? ')
    year_born = int(input('When were you born'))
    current_year = 2021
    age = int(current_year-year_born)

    gender = input('What is your gender ? ')

    pronoun = ''
    if gender == 'female':
        pronoun == 'She'
    else:
        pronoun == 'He'

    return f'{pronoun} is {first_name} {last_name}. {pronoun} is {age} years old. {pronoun} live in {city}, {country}.'
print(get_person_info)'''

'''def calculate_area_circle():
    import math
    pi = math.pi
    radius = float(input('Enter the radius'))
    area = pi * radius * radius
    return (area, 2)
print(calculate_area_circle())'''

def create_fullname(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name
print(create_fullname('Josh', 'Adeb'))
print(create_fullname('Asab', 'Yeta'))

'''def add_two_nums(a, b):
    total = a + b
    return total
print(add_two_nums(1,1))'''
""" 
1. The name of the function is calculate_area_rectangle. It takes lenght and widht as parameters and it returns the area. Formulat of area = length * width
2. Calculate perimeter of a reactangle. It takes lenght and width as parameters and it should return the perimeter of the rectangle. Formula of perimeter = 2 * (lenght + width)

 """

def calculate_area_rectangle(l, w):
    area = l * w
    return area
print(calculate_area_rectangle(2, 3))
print(calculate_area_rectangle(100, 200))

def calculate_perimeter_rectangle(l, w):
    perimeter = 2 * (l + w)
    return perimeter
print(calculate_perimeter_rectangle(4, 5))
print(calculate_perimeter_rectangle(100, 200))