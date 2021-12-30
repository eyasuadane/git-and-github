# Functions are used for resuse, testing, and readability.

def name_of_function():
    print('I am a function')

name_of_function()

def add_two_nums(a, b):
    print(a + b)
add_two_nums(1, 3)
add_two_nums(1, 99)

def add_two_nums(a, b):
    total = a + b
    return total

def make_square(n):
    square = n**2
    return square
print(make_square(2))
print(make_square(4))



def calculate_weight(mass, gravity):
    weight = mass*gravity
    return f'{weight} N'
print(calculate_weight(5,1.6))
print(calculate_weight(10,9.8))

