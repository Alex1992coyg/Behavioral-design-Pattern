#!/usr/bin/env python3

from mediator.example2 import *

c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

print("Client triggers operation A.")
c1.do_a()

print("\n", end="")

print("Client triggers operation D.")
c2.do_d()
