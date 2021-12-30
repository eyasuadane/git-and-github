
from countries_data import countries_data
from pprint import pprint 
for c in countries_data:
    print(c['name'], c['capital'], c['population'])


populations = []

for country in countries_data:
    populations.append(country['population'])



