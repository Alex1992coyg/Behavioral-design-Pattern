#!/usr/bin/env python3
from chain_resp.chain_resp_example import *

class DefenceHandler(Abstracthandler):
    def handle(self,request):
        if request == "ramos":
            return f" defence : I will take {request}"
        else:
            return super().handle(request)

class MidfieldHandler(Abstracthandler):
    def handle(self,request):
        if request == "modric":
            return f" Midfield : I will take {request}"
        else:
            return super().handle(request)

class ForwardHandler(Abstracthandler):
    def handle(self,request):
        if request == "cristiano":
            return f" Forward : I will take {request}"
        else:
            return super().handle(request)

def client(handler):
    for players in ["ramos", "modric", "cristiano"]:
        print( f" \nLot : who want the {players}")
        result = handler.handle(players)
        if result:
            print (f"  {result}" , end="")
        else:
            print (f" {players} was left untouched.", end="")

if __name__ == '__main__':
    defencelist = DefenceHandler()
    midfieldlist= MidfieldHandler()
    forwardlist = ForwardHandler()

    defencelist.set_next(midfieldlist).set_next(forwardlist)
    print("chain: defence > midfield > forward")
    client(defencelist)
    print("\n")

    print("subchain : midfield > forward")
    client(midfieldlist)
