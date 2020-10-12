#!/usr/bin/env python3

from memento.memento_ex import *
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


originator = Originator("Starting.")
caretaker = Caretaker(originator)

caretaker.backup()
originator.new_method()

caretaker.backup()
originator.new_method()

caretaker.backup()
originator.new_method()

print()
caretaker.show_history()

print("\nClient: Now, let's rollback!\n")
caretaker.undo()

print("\nClient: Once more!\n")
caretaker.undo()
