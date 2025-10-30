class Restaurant:
    name = ''
    category = ''
    rating = float
    delivery = False


bobs_burger = Restaurant()

bobs_burger.name = 'Bob\s Burgers'
bobs_burger.category = 'American Diner'
bobs_burger.rating = 4.7
bobs_burger.delivery = False

sadia = Restaurant()

sadia.name = 'Sadia'
sadia.category = 'Brazilian Lunch'
sadia.rating = 4.0
sadia.delivery = False

tonho_de_martinha = Restaurant()

tonho_de_martinha.name = 'Tonho de Martinha'
tonho_de_martinha.category = 'Brazilian Breakfast and Lunch'
tonho_de_martinha.rating = 4.5
tonho_de_martinha.delivery = True

print(vars(tonho_de_martinha))
print(vars(sadia))
print(vars(bobs_burger))
