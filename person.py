from typing import List  # Import the List type

class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name


# This function takes an argument person which is of type Person
def greet_person(person: Person):
    print(f"Hello {person.name}")

jane = Person(13, "Jane")
greet_person(jane)

# greet_people takes a list of people as an argument
def greet_people(people: List[Person]):
    for person in people:
        greet_person(person)

tom = Person(15, "Tom")
rick = Person(30, "Rick")
amanda = Person(18, "Amanda")

list_of_persons = [tom, rick, amanda]

greet_people(list_of_persons)
