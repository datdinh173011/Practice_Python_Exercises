"""The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
It lets the algorithm vary independently from clients that use it.
"""


class Strategy:
    def execute(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        print(f"Executing strategy A with data: {data}")


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        print(f"Executing strategy B with data: {data}")


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self, data):
        self.strategy.execute(data)


# Usage
strategy_a = ConcreteStrategyA()
strategy_b = ConcreteStrategyB()
context = Context(strategy_a)
context.execute("Hello")
context.set_strategy(strategy_b)
context.execute("World")
