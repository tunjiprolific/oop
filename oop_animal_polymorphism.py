class animal:
    def eat(self):
        pass

    def walk(self):
        pass

    def make_sound(self):
        pass


class wolf(animal):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is now scattering its food')
        print(f'{self.name} is now eating its food')

bad_wolf = wolf("Tammy")
bad_wolf.eat()