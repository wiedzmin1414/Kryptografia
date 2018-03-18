#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:27:20 2018

@author: lpolakiewicz
"""
ddd = 2**31-1
eee = 16807
fff = 2**32
h31 = 2**31
h32 = 2**32
ile_dostaje = 85+10
ile_ma_zwrocic = 200
def glibcgen(seed,ile):
    r = [seed]
    for i in range(30):
        seed = eee*seed % ddd
        r.append(seed)
    for i in range(3):
        r.append( r[i] )
    for i in range(310+ile):
        r.append( (r[i+31] + r[i+3]) % fff)
    return [i>>1 for i in r[344:] ]


dane = glibcgen(72213122,ile_dostaje + ile_ma_zwrocic)

def zlam2(dane,ile):
    dlugosc = len(dane)
    w = [0] * dlugosc
    for i in range(dlugosc - 31):
        if( ( (dane[i] + dane[i+28]) % h31 ) != dane[i+31] ):
            w[i] = 1
            w[i+28] = 1
        else:
            if w[i] == 1 or w[i+28] == 1:
                w[i+31] = 1
    r = [2*k for k in dane]
    for i in range(dlugosc):
        r[i] += w[i]
    #for i in range( dlugosc - 31):
     #   if ( (r[i] + r[i+28]) % fff ) != r[i+31]:
      #      r[i+31] =( r[i] + r[i+28]) % fff 
    
    for i in range(ile):
        r.append( (r[-31] + r[-3]) % h32)
    return [i>>1 for i in r[-ile: ] ] 
    
dane_wejsciowe = dane[:ile_dostaje]
mial_dostac = dane[ile_dostaje:]
nowe = zlam2(dane_wejsciowe,ile_ma_zwrocic)
#print("Dane na wejsciu: ", dane)
#print("#"*10)
print("Mial otrzymac",mial_dostac)
print("#"*15)
print("Dane wyestymowane", nowe)
ile_zle = 0
for i in range(ile_ma_zwrocic):
    if(mial_dostac[i] != nowe[i]):
        ile_zle += 1
print("procent zlych danych: {}".format(ile_zle / ile_ma_zwrocic))