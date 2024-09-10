"""Facade Pattern The Facade pattern provides a unified interface to a set of interfaces in a subsystem.
It defines a higher-level interface that makes the subsystem easier to use.
"""


class SubSystemA:
    def operation_a(self):
        print("SubSystemA.operation_a()")


class SubSystemB:
    def operation_b(self):
        print("SubSystemB.operation_b()")


class Facade:
    def __init__(self):
        self.subsystem_a = SubSystemA()
        self.subsystem_b = SubSystemB()

    def operation(self):
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()


# Usage
facade = Facade()
facade.operation()
