#!/usr/bin/env python3
from template.template_example import *


print("Same client code can work with different subclasses:")
client_code(ConcreteClass1())
print("")

print("Same client code can work with different subclasses:")
client_code(ConcreteClass2())
