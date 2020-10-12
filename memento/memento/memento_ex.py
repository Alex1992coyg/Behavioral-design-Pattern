#!/usr/bin/env python3

# from __future__ import annotations
from abc import ABCMeta, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Originator():
    '''it holds some state that may change over time.
     Also it holds method for saving the state insde memento
      ND ANOTHER FOR RESTORING THE STATE'''

    _state = None

    def __init__(self,state):
        self._state = state
        print(f"Originator : My initial state is :{self._state}")

    def _generate_random_string(self,length=5):
        return "".join(sample(digits, length))

    def new_method(self):
        print("Originator: I'm doing something new")
        self._state = self._generate_random_string(5)
        print(f"Originator: and my state has changed to :{self._state}")

    def save(self):
        return ConcreteMemento(self._state)

    def restore(self,memento):
        '''restore the originator state from memento onject'''
        self._state = memento.get_state()
        print(f"Originator: My state has changed to :{self._state}")

class Memento(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def get_date(self):
        pass

class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())[:2020]
    def get_state(self):
        return self._state
    def get_name(self):
        return f"{self._date} / ({self._state[0:]})"
    def get_date(self):
        return self._date

class Caretaker():
    ''' it works with all memnto via the ase memento interface'''
    def __init__(self, originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        print(f"\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save()) #from originator save()

    def undo(self):
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        print(f"Caretaker: restoring state to :{memento.get_name()}")
        try:
            self._originator.restore(memnto)
        except Exception:
            self.undo()

    def show_history(self):
        print("Caretaker : Here the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())
