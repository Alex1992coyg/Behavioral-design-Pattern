#!/usr/bin/env python3
"""
To create an iterator in Python, there are two abstract classes from the built-
in `collections` module - Iterable,Iterator. We need to implement the
`__iter__()` method in the iterated object (collection), and the `__next__ ()`
method in theiterator.
"""

'''Iterator is a behavioral design pattern
   that lets you traverse elements of a collection
   without exposing its
   underlying representation (list, stack, tree, etc.).'''
from collections.abc import Iterator, Iterable

class AlphabeticalOrderIterator(Iterator):
    _position= None #store current traversal position
    _reverse= False #indicate the traversal direction

    def __init__(self, collection, reverse= False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self): #it must return next item in the sequence
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value

class WordsCollection(Iterable):
    """
    Concrete Collections provide one or several methods for retrieving fresh
    iterator instances, compatible with the collection class.
    """
    def __init__(self, collection=[]):
        self._collection = collection

    def __iter__ (self):
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)
