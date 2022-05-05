class cat:
    __mood = 10
    hungry = 10
    energy = 10

    def __meow(self):
        print("meow")

    def get_mood(self):
        return self.__mood


    def sleep(self):
        self.energy += 1
        self.hungry += 1

    def play(self):
        self.__mood += 1
        self.energy -= 1
        self.__meow()

    def feed(self):
        self.hungry -= 1
        self.__mood += 1
        self.__meow()


billy = cat()
print(billy.get_mood())
billy.play()

