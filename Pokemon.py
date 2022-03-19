import random
import requests

pokemon_number = input("What is the Pokemon's ID? ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
pokemon = response.json()

print('your', pokemon['name'], 'height', pokemon['height'])
print('your', pokemon['name'], 'weight', pokemon['weight'])

height = pokemon['height']
weight = pokemon['weight']
moves = pokemon['moves']

points = 0
for move in moves:
    points += 1
print('Your', pokemon['name'], 'moves', points)
print('\n')
random_pokemon_number = random.randint(1, 493)
print("Computer's pokemon number is", random_pokemon_number)
random_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(random_pokemon_number)
random_response = requests.get(random_url)

random_pokemon = random_response.json()
print('Computer', random_pokemon['name'], 'height', random_pokemon['height'])
print('Computer', random_pokemon['name'], 'weight', random_pokemon['weight'])

random_moves = random_pokemon['moves']
random_points = 0
for random_move in random_moves:
    random_points += 1
print('Computer', random_pokemon['name'], 'moves', random_points)

random_height = random_pokemon['height']
random_weight = random_pokemon['weight']


if random_height > height:
    random_points += 1
elif random_height < height:
    points += 1
elif random_weight > weight:
    random_points += 1
elif random_pokemon < weight:
    points += 1

print('\n')
print('Your', pokemon['name'], 'points: ', int(points))
print('Computer', random_pokemon['name'], 'points: ', int(random_points))

if random_points > points:
    print('You have lost')
elif random_points < points:
    print('You have won')
else:
    print('Equal')
