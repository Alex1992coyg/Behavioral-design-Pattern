#!/usr/bin/env python3
from state.state_example import *

context = Context(ConcreteStateB())
context.request1()
context.request2()
print("\n")
context = Context(ConcreteStateA())
context.request1()
context.request2()
