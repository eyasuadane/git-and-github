
from countries_list import countries
from pprint import pprint
#import pandas as pd
#print(countries_list.countries)

new_list = []

for country in countries:
    print(country)
def get_countries_with_land():
    new_list = []
    for c in countries:
        if 'land' in c:
            new_list.append(c)
    return(new_list)
print(get_countries_with_land())

'''def get_countries_with_ia():
    new_list = []
    for c in countries:
        if 'ia' in c:
            new_list.append(c)
        return new_list
    print(get_countries_with_ia())'''

def get_countries_with_five_letter():
    new_list = []
    for c in countries:
        if c.startswith('F'):
            new_list.append(c)
    return new_list
print(get_countries_with_five_letter())




