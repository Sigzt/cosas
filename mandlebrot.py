from graphics import *
from math import *
from customtools import *


def func(n,ex) :
    return [lambda x,c:x**ex+c, lambda x,c: (abs(x.real)+abs(x.imag)*1j)**2 + c][n]
def fastplot(x,y,col):
    win.create_line(x,y,x+2,y+2, fill=col)
def fractal(dim,r,it,di,fun,jit):    
    mapa = lattice(r,r,[dim,dim])
    puntos = [[convergence(z,fun,it,di)  for z in l]for l in mapa]
    print("fractal calculado, representando puntos:")
    dx,dy = lrandomlist(dim,jit),lrandomlist(dim,jit)
    [[fastplot(dx[i],dy[j], puntos[i][j]) for j in range(0,dim+1)] for i in range(0,dim+1)]
    return mapa
def convergence(p,fun,it,di):
    a,i = p,0
    while mod(a)<di and i<it:
        i = i + 1
        a = fun(a,p)
    if it == i:
        return "black"
    return color_rgb(0,10*i,8*i)
if int(input("pulse 1 para saltar configuración")) != 1:
    print("Hola!, introduzca las dimensiones de la ventana (recomendado 300):")
    dim = int(input())
    win = GraphWin("hola!",dim,dim)
    print("Pantalla creada, seleccione ahora el tipo de función, 0: mandlebrot, 1: burning ship; luego elija el exponente n  de la función x**n+c ")
    funs = [int(input("tipo:")), int(input("exponente:"))]
    fun = func(funs[0],funs[1])
    it = int(input("Seleccione el número de iteraciones: "))
    jitt = int(input("rango de jitter:"))
else:
    dim,fun,it,jitt = 300,func(0,2),20,1
    win = GraphWin("hola!",dim,dim)
m = fractal(dim,[-2,2],it,2,fun,jitt)
while True:
    a = win.getMouse()
    x,y = int(a.x),int(a.y)
    p0 = m[x][y]
    p = p0
    rp = [x,y]
    for i in range(10):
        p1 = fun(p,p0)
        rp1 = [(p1.real+2)*dim/4,dim-(p1.imag+2)*dim/4]
        win.create_line(rp[0],rp[1],rp1[0],rp1[1],fill="white")
        p = p1
        rp = rp1
    print(p)