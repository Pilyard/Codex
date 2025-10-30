class City:
    def __init__(self, name, country, population, landmakrs, founding_year, actual_mayor):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmakrs
        self.founding_year = founding_year
        self.actual_mayor = actual_mayor


paraiba = City('João Pessoa', 'Brazil', 897633, 'Natural Beaches', 1585, 'Cicero Lucena')
bahia = City('Salvador', 'Brazil', 15000000, 'Carvanal', 1549, 'Bruno Reis')

print(vars(paraiba))
print(vars(bahia))
