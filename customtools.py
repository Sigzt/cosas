import random
from math import *
def randomlist(n):
    l1 = [i for i in range(n)]
    return random.shuffle(l1)
def lrandomlist(n,f):
    nv,el = floor(n/f),[]
    l = [[i for i in range(f*k,f*(k+1))] for k in range(0,nv)]
    for p in l:
        random.shuffle(p)
        for j in p:
            el.append(j)
    el.append(n+1)
    return el
def lattice(x,y,n,c=False): #x = [a,b], y = [c,d] n = [nx,ny]
    px,py = [round(((n[0]-i)/n[0])*x[0] + (i/n[0])*x[1],3) for i in range(0,n[0]+1)], [complex(0,round(((n[1]-i)/n[1])*y[0] + (i/n[1])*y[1],3)) for i in range(0,n[1]+1)] 
    latmap = [[a+b for a in py[::-1]] for b in px]
    return latmap
def mod(z): 
    return sqrt(z.real**2+z.imag**2)
def fmod(z):
    return abs(abs(z.real)+abs(z.imag))
def ccos(z):
    a,b = z.real,z.imag
    return complex(cos(a)*cosh(b),-sin(a)*sinh(b))