#!/usr/bin/env python
'''some objects to notify other objects about changes in their state.'''

'''mostly used in GUI'''

# from __future__ import annotations
from abc import ABCMeta, abstractmethod
from random import randrange
from typing import List

class Subject(metaclass=ABCMeta):

    @abstractmethod
    def attach(self, observer):
        pass
    @abstractmethod
    def detach(self, observer):
        pass
    @abstractmethod
    def notification(self):
        pass

class ConcreteSubject(Subject):

    _state = None
    _observers = []

    def attach(self,observer):
        print("Subject: Attached an observer")
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notification(self):
        print("Subject: Notifying observers..")
        for observer in self._observers:
            observer.update(self)

    def business_logic(self):
        self._state = randrange(0, 10)
        print(f"Subject: my state has changed to {self._state} \n")
        self.notification()


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self,subject):
        pass

class ConcreteObserverA(Observer):
    def update(self,subject):
        if subject._state < 3:
            print("ConcreteObserverA: reacted to the event")

class ConcreteObserverB(Observer):
    def update(self,subject):
        if subject._state == 0 or subject._state >= 3:
            print("ConcreteObserverB: reacted to the event")
