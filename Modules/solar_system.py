from math import pi
from random import choice as ch
pi_value = pi

planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn'
]

random_planet = ch(planets)


def area_surface(radius):
    area = 4 * pi_value * (radius ** 2)
    return area


if random_planet == 'Mercury':
    print(round(area_surface(2440)))

elif random_planet == 'Venus':
    print(round(area_surface(6052)))

elif random_planet == 'Earth':
    print(round(area_surface(6371)))

elif random_planet == 'Mars':
    print(round(area_surface(3390)))

elif random_planet == 'Saturn':
    print(round(area_surface(58232)))
