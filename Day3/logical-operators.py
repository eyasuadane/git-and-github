print(4 < 3 and 8 > 6)
print(not 4 > 3)
# Logical Operators: and, or, not
print(4 > 3 and 8 > 6) # True
print(4 > 3 and 8 < 6) # False
print(4 < 3 and 8 < 6) # False

print(4 > 3 or 8 > 6) # True
print(4 > 3 or 8 < 6) # True
print(4 < 3 or 8 < 6) # False

print('==== Negation  ===')
print(not 4 > 3)
print(not True)
print(not not True)

#if conditions

"""

He is Asabeneh Yetayeh. He is 250 years old. He live in Helsink, Finland. 

"""

a = 10
if a > 0:
    print(f'{a} is a positive  number')
elif a < 0:
    print(f'{a} is a negative number')
elif a == 0:
    print(f'{a} is zero')
else:
    print('We do not know about this number')


weather = input('What is the weather like to day? ').lower()
print(weather)

if weather == 'rainy' :
    print('Please take an umbrella or a raincoat')
elif weather == 'shiny':
    print('The day seems shiny go out freely')
elif weather == 'snowy':
    print('It might be slipper')
elif weather == 'cloudy':
    print('It is good to consider an umbrella')
elif weather == 'foggy':
    print('There might limited visibility')
else:
    print('No one know the weather')

"""

He is Asabeneh Yetayeh. He is 250 years old. He live in Helsink, Finland. 

"""


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

print(f'{pronoun} is {first_name} {last_name}. {pronoun} is {age} years old. {pronoun} live in {city}, {country}.')