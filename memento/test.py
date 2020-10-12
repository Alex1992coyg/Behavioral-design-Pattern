#!/usr/bin/env python3

from memento.memento_ex import *

originator = Originator("00000")
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
