empty_dict = {}
print(empty_dict)
print(type(empty_dict))
dict()

user = {
    'first_name': 'John',
    'last_name': 'Adebo'
}

person = {
    'first_name': 'Eyasu',
    'last_name': 'Adane',
    'age': 31,
    'is_married': False
}

print(person['first_name'])
print(person['last_name'])
person['Nationality'] = 'Ethiopian'
print(person['Nationality'])
person['hobbies'] = ['Jogging', 'Biking']

if 'hobbies' in person:
    print(person['hobbies'])

print(person.keys())
print(person.values())

for key in person:
    print(key, person[key])

person['age'] = '25'
print(person)

person2 = person.copy()
print(person2)


