"""The Flyweight pattern aims to minimize memory usage by sharing data with similar characteristics.
"""


class Flyweight:
    def __init__(self, data):
        self.data = data

    def operation(self, extrinsic_data):
        print(f"Flyweight ({self.data}): {extrinsic_data}")


class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, key):
        if key not in self.flyweights:
            self.flyweights[key] = Flyweight(key)
        return self.flyweights[key]


# Usage
factory = FlyweightFactory()

flyweight_a = factory.get_flyweight("A")
flyweight_a.operation("Extrinsic Data 1")

flyweight_b = factory.get_flyweight("B")
flyweight_b.operation("Extrinsic Data 2")

flyweight_a.operation("Extrinsic Data 3")
