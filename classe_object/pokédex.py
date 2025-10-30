class Pokedex():
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self. description = description
        self.is_caught = is_caught

    def speak(self):
        return print(self.name + ', ' + self.name)

    def display_details(self):
        print('Entry Number: {}'.format(self.entry))
        print('Name: {}'.format(self.name))
        print('Type(s): {}'.format(self.types))
        print('Description: {}'.format(self.description))
        if self.is_caught == True:
            print('{} has already been caught!'.format(self.name))
        else:
            print('{} has not been caught yet!'.format(self.name))
        return


pokemon_212 = Pokedex(212, 'Scizor', [
    'Bug', 'Steel'], 'This Pokémon’s pincers, which contain steel, can crush any hard object they get ahold of into bits.', True)
pokemon_242 = Pokedex(242, 'Blissey', [
                      'Normal'], 'Anyone who takes even one taste of Blissey’s egg becomes unfailingly caring and pleasant to everyone.', False)
pokemon_484 = Pokedex(484, 'Palkia', [
                      'Water', 'Dragon'], 'It has the ability to distort space. It is described as a deity in Sinnoh-region mythology.', False)


pokemon_212.speak()
pokemon_212.display_details()

pokemon_242.speak()
pokemon_242.display_details()

pokemon_484.speak()
pokemon_484.display_details()
