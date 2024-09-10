"""The Adapter pattern allows objects with incompatible interfaces to collaborate by wrapping
its own interface around that of an already existing class.
"""


class Target:
    def request(self):
        print("Target.request()")


class Adaptee:
    def specific_request(self):
        print("Adaptee.specific_request()")


class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()


# Usage
adaptee = Adaptee()
adapter = Adapter(adaptee)
adapter.request()  # Adaptee.specific_request()
