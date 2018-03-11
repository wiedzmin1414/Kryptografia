#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:27:20 2018

@author: lpolakiewicz
"""
ddd = 2**31-1
eee = 16807
fff = 2**32
def glibcgen(seed,ile):
    r = [seed]
    for i in range(30):
        seed = eee*seed % ddd
        r.append(seed)
    for i in range(3):
        r.append(r[i])
    for i in range(310+ile):
        r.append( (r[+31] + r[i+3]) % fff)
    return [i>>1 for i in r[344:] ]


print(glibcgen(1,62))

dane = glibcgen(1,62)

def zlam(dane,ile):
    if len(dane) < 30:
        print("Za malo danych")
        return 0
    else:
        ggg = 2**31
        r = dane[:30]
        for i in range(ile):
            if i%2 == 1:
                r.append( (r[i] + r[i+28]) %  ggg)
            else:
                r.append( (r[i] + r[i+28] + 1) %  ggg)
    return r[30:]

nowe = zlam(dane[:50],10)
print(nowe)
print(dane[50:])
