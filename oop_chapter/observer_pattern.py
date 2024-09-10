"""The Observer pattern defines a one-to-many dependency between objects so that
when one object changes state, all its dependents are notified and updated automatically.
"""


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)


class Observer:
    def update(self, data):
        pass


class ConcreteObserver(Observer):
    def update(self, data):
        print(f"Received data: {data}")


# Usage
subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()
subject.attach(observer1)
subject.attach(observer2)
subject.notify("Hello, World!")
