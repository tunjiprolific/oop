class animal:
    __no_of_legs = 0
    has_horns = False
    is_carnivore = False
    can_be_pet = False

    def __init__(self, name="john doe"):
        self.name = name

    def set_can_be_pet(self, can_be_pet: bool):
        self.can_be_pet = can_be_pet

    def set_no_of_legs(self, no_of_legs=2):
        self.__no_of_legs = no_of_legs

    def get_no_of_legs(self):
        return self.__no_of_legs

    def eat(self):
        print(f'animal with name {self.name} is now eating')

    def walk(self):
        print(f'animal with name {self.name} is now walking')

    def make_sound(self):
        print(f'animal with name {self.name} is now making sound')

class wolf(animal):
    def __init__(self, name):
        super().__init__(name) # Calls the parent's constructor by passing all required parameters of the parent

    def eat(self):
        print(f'{self.name} is now scattering its food')
        print(f'{self.name} is now eating its food')

class goat(animal):
    def __init__(self, name):
        super().__init__(name)

class lion(animal):
    def __init__(self, name):
        super().__init__(name)

class seal(animal):
    def __init__(self):
        super().__init__()

class fish(animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print(f'oops, i am a fish, i cannot walk')

bad_wolf = wolf("Tricia")
bad_wolf.set_no_of_legs(4)
bad_wolf.set_can_be_pet(False)
print(bad_wolf.get_no_of_legs())
bad_wolf.eat()
bad_wolf.walk()

the_fish = fish("Octofish")
the_fish.eat()
the_fish.walk()

the_seal = seal()
print(the_seal.name)
