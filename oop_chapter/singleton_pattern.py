""" The Singleton Pattern ensures that a class has only one instance
and provides a global point of access to it
"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)
