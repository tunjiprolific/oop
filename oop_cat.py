class cat:
    __mood = 10
    __hungry = 10
    __energy = 10

    def __meow(self):
        print("meow")

    def get_mood(self):
        return self.__mood

    def get_hunger(self):
        return self.__hungry

    def get_energy(self):
        return self.__energy

    def sleep(self):
        self.__energy += 1
        self.__hungry += 1

    def play(self):
        self.__mood += 1
        self.__energy -= 1
        self.__meow()

    def feed(self):
        self.__hungry -= 1
        self.__mood += 1
        self.__meow()


billy = cat()
print(billy.get_mood())
print(billy.get_hunger())
print(billy.get_energy())
billy.play()

