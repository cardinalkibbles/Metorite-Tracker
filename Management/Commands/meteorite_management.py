import json

fallen_meteorites = []

with open('meteorites.json', encoding='utf8') as json_file:
    # print(json_file)
    nasa_data = json.load(json_file)
    # nasa_data = json.dumps(nasa_data)
# print(type(nasa_data))
# change mass(g) to mass
# remove recclass, geolocation
# rename reclong and reclat to longitude and latitude

for data in nasa_data:
    fallen_meteorites.append({
        "name": data.get('name'),
        "id": data.get('id'),
        "nametype": data.get('nametype'),
        "mass": data.get('mass (g)'),
        "fall": data.get('fall'),
        "year": data.get('year'),
        "latitude": data.get('reclat'),
        "longitude": data.get('reclong')

    })  # targeting each dict
