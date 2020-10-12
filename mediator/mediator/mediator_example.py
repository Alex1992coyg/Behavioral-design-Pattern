#!/usr/bin/env python3
'''
Mediator is a behavioral design pattern
that lets you reduce chaotic dependencies
between objects. The pattern restricts direct
communications between the objects and
forces them to collaborate only via
a mediator object.'''

class Mediator:

    def __init__(self):
        self._colleague_1 = Colleague1(self)
        self._colleague_2 = Colleague2(self)
class Colleague1:
    ''' communicate with mediator whenever it want
    otherwise with other colleauge'''
    def __init__(self, mediator):
        self._mediator = mediator

class Colleague2:
    def __init__(self, mediator):
        self._mediator = mediator


def main():
    mediator = Mediator()


if __name__ == "__main__":
    main() 
