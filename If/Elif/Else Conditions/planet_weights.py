#destination weight = earth weight * relative gravity
earth_weight = float(input('Whats your weight on Earth planet? '))
planet = int(input('Tell me now a planet number: '))

if planet == 1:
  destination_weight = earth_weight * 0.38
  print('Your weight on Mercury would be {}.'.format(destination_weight))
elif planet == 2:
  destination_weight = earth_weight * 0.91
  print('Your weight on Venus would be {}.'.format(destination_weight))
elif planet == 3:
  destination_weight = earth_weight * 0.38
  print('Your weight on Mars would be {}.'.format(destination_weight))
elif planet == 4:
  destination_weight = earth_weight * 2.53
  print('Your weight on Jupter would be {}.'.format(destination_weight))
elif planet == 5:
  destination_weight = earth_weight * 1.07
  print('Your weight on Saturn would be {}.'.format(destination_weight))
elif planet == 6:
  destination_weight = earth_weight * 0.89
  print('Your weight on Uranus would be {}.'.format(destination_weight))
elif planet == 7:
  destination_weight = earth_weight * 1.14
  print('Your weight on Neptune would be {}.'.format(destination_weight))
else:
  print('Invalid planet number')