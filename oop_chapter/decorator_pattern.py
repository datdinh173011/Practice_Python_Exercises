"""Decorator Pattern The Decorator pattern allows behavior to be added to an individual object, either statically or dynamically,
without affecting the behavior of other objects from the same class."""


class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent.operation()")


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        print("ConcreteDecoratorA.operation()")
        self.component.operation()


class ConcreteDecoratorB(Decorator):
    def operation(self):
        print("ConcreteDecoratorB.operation()")
        self.component.operation()


# Usage
component = ConcreteComponent()
decorator_a = ConcreteDecoratorA(component)
decorator_b = ConcreteDecoratorB(decorator_a)
decorator_b.operation()
