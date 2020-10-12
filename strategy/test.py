#!/usr/bin/env python3

from stratergy.strategy_example import *


context = Context(ConcreteStrategyA())
print("Client: Strategy is set to normal sorting.")
context.new_logic()
print()

print("Client: Strategy is set to reverse sorting.")
context.strategy = ConcreteStrategyB()
context.new_logic()
