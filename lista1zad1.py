#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:29:47 2018

@author: lpolakiewicz
"""
import random
# s_n = m * s_(n-1) + c ( mod n )
def lcg(seed,m,c,n,how_much):
    l = []
    for i in range(how_much):
        seed = (m*seed + c) % n
        l.append(seed)
    return l

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(b, n):
    g, x, w = egcd(b, n)
    if g == 1:
        return x % n
    else:
        #print("Cos sie, cos sie popsulo i nie ma odwrotnosci dzielenia modulo!!!!!!11111one")
        return 0
 
def hackerman(v):
    r = []
    for i in range(5):
        r.append(v[i+1] - v[i] )
    t = []
    for i in range(3):
        t.append(abs(r[i+2]*r[i] - r[i+1]*r[i+1]))
    n = gcd( gcd(t[0],t[1]), t[2] )
    #print("n= ",n)
    m = (v[2] - v[1]) * modinv(v[1] - v[0],n) % n
    c = ( v[1] - v[0] * m ) % n
   # print('m= ', m)
   # print('c= ', c)
    #print('n= ', n)
    return m,c,n
    
def isthisrandom(v):
    if hackerman(v)[2] <= max(v):
        return True
    return False 

for k in range(100):
    d = []
    for i in range(7):
        d.append(random.randint(0,6*k+10) )
    if( isthisrandom(d) == False):
        print(d, ' nie jest losowa', hackerman(d)) 
