gryffindor = 0
slytherin = 0
ravenclaw = 0
hufflepuff = 0

q1 = int(input('''Q1) Do you like Dawn or Dusk?
1) Dawn
2) Dusk
'''))
if q1 == 1:
  gryffindor += 1 
  ravenclaw += 1
elif q1 == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print('Wrong input.')

q2 = int(input('''Q2) When im dead, i want people to remember me as:
1) The Good
2) The Great
3) The Wise
4) The Bold 
'''))
if q2 == 1:
  hufflepuff += 2
elif q2 == 2:
  slytherin += 2
elif q2 == 3:
  ravenclaw += 2
elif q2 == 4:
  gryffindor += 2
else:
  print('Wrong input.')

q3 = int(input('''Q3) Wich  king of instrument most pleases your ear? 
1) The violin
2) The trumpet
3) The piano
4) The drum
'''))

if q3 == 1:
  slytherin += 4
elif q3 == 2:
  hufflepuff += 4
elif q3 == 3:
  ravenclaw += 4
elif q3 == 4:
  gryffindor += 4
else:
  print("Wrong input.")

print('Gryffindor points: {}'.format(gryffindor))
print('Ravenclaw points: {}'.format(ravenclaw))
print('Hufflepuff points: {}'.format(hufflepuff))
print('Slytherin points: {}'.format((slytherin)))
total_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if total_points == gryffindor:
  print('The highest score is Gryffindor with {} points.'.format(total_points))
elif total_points == ravenclaw:
  print('The highest score is Ravenclaw with {} points'.format(total_points))
elif total_points == hufflepuff:
  print('The highest score is Hufflepuff with {} points'.format(total_points))
else:
  print('The highest score is Slytherin with {} points'.format(total_points))
  
