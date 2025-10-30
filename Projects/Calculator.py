import math
from time import sleep
print('=' * 18)
print('Area Calculator 📐')
print('=' * 18)
while True:
    shape = int(input('''1) Square 
2) Rectangle
3) Triangle 
4) Circle 
5) EXIT
Choose the shape or 5 to EXIT the program: '''))
    if shape == 5:
        print('Leaving the program...')
        sleep(1)
        break
    elif shape == 1:
        sizeSide = float(input('Side size: '))
        totalArea = sizeSide ** 2
        print('The area is {:.0f}.'.format(totalArea))
    elif shape == 2:
        lengh = float(input('Lengh: '))
        width = float(input('Width: '))
        totalArea = lengh * width
        print('The area is {:.0f}.'.format(totalArea))
    elif shape == 3:
        base = float(input('Base: '))
        heigh = float(input('Height: '))
        totalArea = (heigh * base) / 2
        print('The area is {:.0f}.'.format(totalArea))
    elif shape == 4:
        radius = int(input('Radius: '))
        totalArea = math.pi * radius ** 2
        print('The area is {:.1f}.'.format(totalArea))
