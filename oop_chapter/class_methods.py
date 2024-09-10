class Animals:
    # class attribute
    home = 'Zoo'

    # creating instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # creating a class method
    # two ways to create a class method:
    # the first is to use the classmethod() function
    # the second method is to use @classmethod decorator
    # cls means referring to the class
    @classmethod
    def animals_home(cls, home):
        cls.home = home

    # creating instance method
    # Instance methods are used more often than class methods
    # because they can access both class and instance attributes
    def insta_method(self):
        # modifying the class attribute
        self.home = "jungle"
        return f'Name: {self.name}, Age: {self.age}, ' \
               f'Location: {self.home}'

    # static methods cannot access class attributes or instance attributes
    @staticmethod
    def check_age(age):
        if age > 5:
            return 'Adult'
        else:
            return 'Not adult'


animal1 = Animals("Lion", 5)
print(f'The animal is a {animal1.home}')
Animals.animals_home("Jungle")
print(f'The animal is a {animal1.home}')
# calling static method using class instance
print(animal1.check_age(4))

# creating Animals instances
print(animal1.insta_method())
