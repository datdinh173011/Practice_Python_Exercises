"""Chain of Responsibility Pattern The Chain of Responsibility pattern allows an event to be passed along a chain of objects,
with each object having a chance to handle the event.
"""


class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, request):
        pass


class ConcreteHandler1(Handler):
    def handle(self, request):
        if request >= 0 and request < 10:
            print(f"ConcreteHandler1 handled request: {request}")
        elif self.successor:
            self.successor.handle(request)


class ConcreteHandler2(Handler):
    def handle(self, request):
        if request >= 10 and request < 20:
            print(f"ConcreteHandler2 handled request: {request}")
        elif self.successor:
            self.successor.handle(request)


class ConcreteHandler3(Handler):
    def handle(self, request):
        if request >= 20 and request < 30:
            print(f"ConcreteHandler3 handled request: {request}")
        else:
            print(f"Request {request} was not handled")


# Usage
handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2(handler1)
handler3 = ConcreteHandler3(handler2)

handler3.handle(5)   # ConcreteHandler1 handled request: 5
handler3.handle(15)  # ConcreteHandler2 handled request: 15
handler3.handle(25)  # ConcreteHandler3 handled request: 25
handler3.handle(35)  # Request 35 was not handled
