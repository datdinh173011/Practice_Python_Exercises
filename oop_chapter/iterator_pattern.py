"""The Iterator pattern provides a way to access the elements of
an aggregate object sequentially without exposing its underlying representation.
"""


class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass


class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        item = self.collection[self.index]
        self.index += 1
        return item


class Aggregate:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def iterator(self):
        return ConcreteIterator(self.items)


# Usage
aggregate = Aggregate()
aggregate.add("Item 1")
aggregate.add("Item 2")
aggregate.add("Item 3")

iterator = aggregate.iterator()
while iterator.has_next():
    item = iterator.next()
    print(item)
