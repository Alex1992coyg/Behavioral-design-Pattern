#!/usr/bin/env python3
'''different type of sorting using
strategy design pattern'''

from abc import ABCMeta, abstractmethod

class Context():
    '''it defines the interface of interest to clients '''
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        '''the context allow replacing a startegy obj at runtime'''
        self._strategy = strategy

    def new_logic(self):
        ''' this context delegates some wrk to the strategy
        obj instead of implementing multiple
        version of the algorith,'''

        print("Context: Sorting data using the strategy")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))



class Strategy(metaclass=ABCMeta):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data):
        return reversed(sorted(data))
