#!/usr/bin/env python3
# def client( handler):
from chain_resp.chain_resp_example import *

for players in ["ramos", "modric", "cristiano"]:
    print( f"wo want the {players}")
    result =  handle(players)
    if result:
        print (f"  {player}" , end="")
    else:
        print (f" {player} was left untouched.", end="")
