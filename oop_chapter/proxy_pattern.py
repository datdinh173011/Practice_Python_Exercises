"""Proxy Pattern The Proxy pattern provides a surrogate or placeholder for another object to control access to it.
"""


class Subject:
    def request(self):
        print("Subject.request()")


class Proxy:
    def __init__(self, subject):
        self.subject = subject

    def request(self):
        if self.check_access():
            self.subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy.check_access()")
        return True

    def log_access(self):
        print("Proxy.log_access()")


# Usage
subject = Subject()
proxy = Proxy(subject)
proxy.request()
