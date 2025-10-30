import random
my_numbers = []
winning_numbers = []
drawn_numbers = 0

# Loop to fill both lists with randomInt numbers;
for i in range(0, 5):
    my_numbers.append(random.randint(1, 69))
    winning_numbers.append(random.randint(1, 69))
my_numbers.append(random.randint(1, 26))
winning_numbers.append(random.randint(1, 26))

# Loop to know if the number in *my_numbers* and *winning_numbers* are equal;
for number in my_numbers:
    if number in winning_numbers:
        drawn_numbers += 1  # If True, drawn numbers get iterate;
        print(number)

# If *drawn_numbers* was higher or lower than this options below, the player get rewarded or not;
if drawn_numbers == 5:
    print('You won R$500.000,00')
elif drawn_numbers == 3:
    print('You won R$250.000,00')
elif drawn_numbers == 4:
    print('You won R$350.000,00')
elif drawn_numbers == 6:
    print('You won R$1.000.000,00')
elif drawn_numbers == 1 or 2:
    print('You won nothing!')
print('My Numbers: {}'.format(my_numbers))
print('Winning Numbers: {}'.format(winning_numbers))
