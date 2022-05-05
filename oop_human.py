class human:
    def __init__(self, age, gender, complexion="black"):
        self.age = age
        self.gender = gender
        self.complexion = complexion

    def add_age(self, increase: int) -> int:
        self.age += increase
        return self.age

    def sit(self):
        print(f'human with {self.complexion} is now sitting down')

    def menstruate(self):
        if self.gender == "female":
            print("I am now menstruating")
        else:
            print("I am not able to menstruate")


human_one = human(18, "queer")
print(f'The human is {human_one.complexion} of age {human_one.age} and gender {human_one.gender}.')
print(human_one.sit())

human_two = human(22, "male", "asian")
print(f'The human is {human_two.complexion} of age {human_two.age} and gender {human_two.gender}.')
print(human_two.menstruate())
human_two.gender = "female"
print(human_two.menstruate())

female_human = human(20, "female", "asian")
print(female_human.menstruate())
print(female_human.add_age(2))



