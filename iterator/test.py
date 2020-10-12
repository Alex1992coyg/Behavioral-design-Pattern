#!/usr/bin/env python3
from iterator_exampl.iterator_ex import *

collection = WordsCollection()
collection.add_item("First")
collection.add_item("second")
collection.add_item("Third")
collection.add_item("Fourth")
collection.add_item("Fifth")
collection.add_item("sixth")


print("Straight Travesal : ")
print("\n" .join(collection))
print("")


print("Reverse Travesal : ")
print("\n" .join(collection.get_reverse_iterator()),end="")
