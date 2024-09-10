"""Builder Pattern The Builder pattern separates the construction of a complex object from its representation,
allowing the same construction process to create various representations.
"""


class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def display(self):
        print("\n".join(self.parts))


class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_result(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A")

    def build_part_b(self):
        self.product.add("Part B")

    def get_result(self):
        return self.product


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()


# Usage
director = Director()
builder = ConcreteBuilder()
director.set_builder(builder)
director.construct()

product = builder.get_result()
product.display()
