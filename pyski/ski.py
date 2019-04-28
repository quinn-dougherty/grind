#!/usr/bin/env python
'''https://en.wikipedia.org/wiki/SKI_combinator_calculus

via chapter 3 of hindley,seldin'''
import re
from typing import List

atom = str
term = List[atom]
name = r'[a-z]+'
assigned = r'[A-Z]'

def ap(x: atom, y: atom) -> atom: return x + y

def I(xs: term) -> term:
    fst = xs.pop(0)
    rst = xs
    return [fst] + rst

def K(xs: term) -> term:
    fst = xs.pop(0)
    snd = xs.pop(0)
    rst = xs
    return [fst] + rst

def S(xs: term) -> term:
    fst = xs.pop(0)
    snd = xs.pop(0)
    thd = xs.pop(0)
    rst = xs
    return [fst, thd, ap(snd, thd)] + rst

def consume(xs: term) -> term:
    ''' where string refers to IO printout str '''
    rtrn = []
    if not xs:
        return rtrn
    else:
        fst = xs.pop(0)
        if fst in [C for C in "SKI"]:
            x = eval(fst)(xs)
            rtrn += x
        else:
            rtrn += fst + consume(xs)
        return rtrn

def show(xs: term) -> str:
    ''' '''
    s = ''
    for c in xs:
        if len(c)!=1:
            s+=f"({c})"
        else:
            s+=c
    return s

def programming(quit: str=':q') -> str:
    x = ''
    while x!=quit:
        x=input('SKI>')
        sout = consume([c for c in x])
        print(show(sout))

    return "later gator"

'''test:
consume(IaKbcSdef)==abdf(ef)'''
testinp = 'IaKbcSdef'
'''
if __name__=='__main__': 
    while True: 
        show(consume(input()))
        ''' 



