# Python dictionaries
# A dictionary is a collection of key/value pairs
# Python dictionaries allow you to work with related sets of data
planet = {
    'name': 'Earth',
    'moons': 1
}
# print(planet.get('name')) # OR
# print(planet['name'])

# modify dictionary values
# using update
# planet.update({
#     'name': 'Jupiter',
#     'moons': 79
# }) # OR
# planet['name'] = 'Jupiter'
# planet['moons'] = 79

# print(planet['name'])
# print(planet['moons'])

# # add and remove keys
# # add
# planet['orbital period'] = 4333
# # print(planet['orbital period'])
# # remove
# planet.pop('orbital period')
# print(planet.get('orbital period'))

# # complex data types
# planet['diameter (km)'] = {
#     'polar': 133709,
#     'equitorial': 142984
# }

# # print(planet['diameter (km)'])
# print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')


# Dynamic programming with dictionaries
# retrieve all keys and values usin the keys() method
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

# for key in rainfall.keys(): 
#     print(f'{key}: {rainfall[key]}cm')

# determine if a key exists in a dictionary
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# print(rainfall['december'])

# retrieve all values using values() method
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quater')

