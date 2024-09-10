"""Composite Pattern The Composite pattern allows you to compose objects into tree structures to represent part-whole hierarchies.
It lets clients treat individual objects and compositions of objects uniformly.
"""


class Component:
    def operation(self):
        pass


class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(f"Leaf: {self.name}")


class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        for child in self.children:
            child.operation()


# Usage
leaf_a = Leaf("A")
leaf_b = Leaf("B")
composite = Composite()
composite.add(leaf_a)
composite.add(leaf_b)
composite.operation()
