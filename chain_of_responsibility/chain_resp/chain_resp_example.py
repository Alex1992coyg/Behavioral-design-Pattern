#!/usr/bin/env python3
from abc import ABCMeta ,abstractmethod

'''Chain of Responsibility is behavioral design pattern
    that allows passing request along the chain of potential handlers
    until one of them handles request.
'''
class Handler(metaclass=ABCMeta):

    @abstractmethod
    def set_next(self,handler):
        pass
    @abstractmethod
    def handle(self,request):
        pass

class Abstracthandler(Handler):
    nxt_handler = None

    def set_next(self,handler):
        self.nxt_handler = handler
        return handler

    def handle (self,request):
        if self.nxt_handler:
            return self.nxt_handler.handle(request)
        return None
