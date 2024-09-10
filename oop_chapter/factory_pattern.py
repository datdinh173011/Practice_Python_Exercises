"""The Factory pattern provides an interface for creating objects in a super-class,
but allows subclasses to alter the type of objects that will be created
"""


class Animal:
    def __init__(self, special):
        self.special = special

    def show(self):
        print(f"I'm a {self.special}")


class AnimalFactory:
    def create_animal(self, species):
        return Animal(species)


# Usage
factory = AnimalFactory()
dog = factory.create_animal("Dog")
cat = factory.create_animal("Cat")
dog.show()
cat.show()
