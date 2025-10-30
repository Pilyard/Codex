name = str(input('Whats your name: '))
menu = ['🍔 Cheeseburger', '🍟 Fries', '🥤 Soda', '🍦 Icecream', '🍪 Cookie']

def welcome():
    print('Welcome to the McDonalds {}!'.format(name))
    return

def get_item(x):
    return menu[x - 1]

welcome()
option = int(input('What would you like to order? '))
print(get_item(option))

