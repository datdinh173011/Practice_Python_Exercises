"""Command Pattern The Command pattern encapsulates a request as an object, thereby allowing for the parameterization of clients
with different requests, queue or log requests, and support undoable operations.
"""


class Command:
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action()


class Receiver:
    def action(self):
        print("Receiver.action()")


class Invoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()


# Usage
receiver = Receiver()
command = ConcreteCommand(receiver)

invoker = Invoker()
invoker.add_command(command)
invoker.execute_commands()
