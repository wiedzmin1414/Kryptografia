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
        print("Cos sie, cos sie popsulo i nie ma odwrotnosci dzielenia modulo z liczb: {} i {}".format(b,n) )
        return 0
 
def hackerman(v):
    r = []
    for i in range(5):
        r.append(v[i+1] - v[i] )
    t = []
    for i in range(3):
        t.append(abs(r[i+2]*r[i] - r[i+1]*r[i+1]))
    n1 = gcd( gcd(t[0],t[1]), t[2] )
    n = n1
    #print("n= ",n)
    m = ((v[2] - v[1]) * modinv((v[1] - v[0]+n)%n,n) ) % n
    c = ( v[1] - v[0] * m ) % n
    proba = lcg(v[0],m,c,n,6)
    #return m,c,n
    dzielnik = 1
    while(proba != v[1:7]):
        dzielnik +=1
        n = n1 // dzielnik
        print("n= ",n," m= ",m, "c= ",c)
        o = int(input("przerwa"))
        m = ((v[2] - v[1]) * modinv((v[1] - v[0]+n)%n,n) ) % n
        c = ( v[1] - v[0] * m ) % n
        proba = lcg(v[0],m,c,n,6)
   
def hackerman2(v):
    r = []
    for i in range(5):
        r.append(v[i+1] - v[i] )
    t = []
    for i in range(3):
        t.append(abs(r[i+2]*r[i] - r[i+1]*r[i+1]))
    n1 = gcd( gcd(t[0],t[1]), t[2] )
    n = n1
    #print("n= ",n)
    m = ((v[2] - v[1]) * modinv((v[1] - v[0]+n)%n,n) ) % n
    c = ( v[1] - v[0] * m ) % n
    proba = lcg(v[0],m,c,n,6)
    if (proba != v[1:7]) and len(v) > 6:
        v = [ i for i in v[1:]]
        return hackerman2(v)
    else:
        if len(v) < 7:
            print("Nie pyklo")
            return False
    return(m,c,n)
        
    
    
   # print('m= ', m)
   # print('c= ', c)
    #print('n= ', n)
    return m,c,n
    
def isthisrandom(v):
    if hackerman(v)[2] <= max(v):
        return True
    return False 

w = lcg(1511,21231,1467,123111,10)
z = hackerman(w)
print(z)
#for k in range(100):
#    d = []
 #   for i in range(7):
#       d.append(random.randint(0,6*k+10) )
#    if( isthisrandom(d) == False):
#        print(d, ' nie jest losowa', hackerman(d)) 