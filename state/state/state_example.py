#!/usr/bin/env python3

'''State is a behavioral design pattern
 that lets an object alter its behavior
 when its internal state changes.
 It appears as if the object changed its class.'''

from abc import ABCMeta, abstractmethod

class Context(metaclass=ABCMeta):
    ''' this is the interface of interest to client.also
    maintain the current state of the context'''
    _state = None

    def __init__(self,state):
        self.transition_to(state)

    def transition_to(self, state):
        print(f"Context: Transition to {type(state).__name__}")
        self._state =state
        self._state.context = self

    def request1(self):
        self._state.handle1()
    def request2(self):
        self._state.handle2()

class State(metaclass=ABCMeta):
    @property
    def context(self):
        return self._context
    @context.setter
    def context(self,context):
        self._context = context
    @abstractmethod
    def handle1(self):
        pass
    @abstractmethod
    def handle2(self):
        pass

class ConcreteStateA(State):
    def handle1(self):
        print("ConcretestateA handles req 1.")
        print("concretestateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())
    def handle2(self):
        print("ConcreteStateA handles req 2.")

class ConcreteStateB(State):
    def handle1(self):
        print("ConcreteStateB handles req 1.")
    def handle2(self):
        print("ConcretestateB handles req 2.")
        print("concretestateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())
