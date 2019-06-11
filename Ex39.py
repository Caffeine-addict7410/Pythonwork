states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print("Michigan has: ", cities[states['Michigan']])
print("Flordia has: ", cities[states['Flordia']])

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{states} is abbrevited {abbrev}")
    
print('-' * 10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {cities}")
    
print('-' * 10)
for abbrev,city in list(states.items()):
    print(f"{states} state is abbrevited {abbrev}")
    print(f"and has city {cities[abbrev]}")
    
print('-' * 10)
state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")
    
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is {city}")
