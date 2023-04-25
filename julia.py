from graphics import *
from math import *
from customtools import *
phi,psi = (1+sqrt(5))/2, (1-sqrt(5))/2
def fastplot(x,y,col):
    win.create_line(x,y,x+2,y+2, fill=col)
def fractal(dim,r,it,di,fun,k,jit=1):    
    mapa = lattice(r,r,[dim,dim])
    puntos = [[convergence(z,fun,k,it,di)  for z in l]for l in mapa] #holii, si cambias convergence por convergnce 2 pasan cosas chulas( aveces)
    print("fractal calculado, representando puntos:")
    dx,dy = lrandomlist(dim,jit),lrandomlist(dim,jit)
    [[fastplot(dx[i],dy[j], puntos[i][j]) for j in range(0,dim+1)] for i in range(0,dim+1)]
    return mapa
def convergence(p,fun,k,it,di):
    a,i = p,0
    while mod(a)<di and i<=it:
        i = i + 1
        a = fun(a,k)
    if it < i and mod(a)<di:
        return color_rgb(int(mod(a)*100)+50,int(mod(a)*100)+50,30)
    return color_rgb(0,int(200*i/it),int(200*i/it))
def localizarmand (p):
    print("por hacer")
def convergence2(p,fun,k,it,di):
    a,i = p,0
    while mod(a)<di and i<it:
        i = i + 1
        a = fun(a,k)
    if i == 20:
        return "black"
    return color_rgb(0,10*i,8*i)
dim,fun,it,jitt = 300,lambda x,k: x**2 + k,20,1
win = GraphWin("hola!",dim,dim)
m = fractal(dim,[-1.5,1.5],100,2,fun,complex(phi-2,-psi))
while __name__ == "__main__":
     #donde pone complex se puede cambiar los números para cambiar el fractal puntos guays: (psi,0) (psi,psi) (1-sqrt(pi),0.1))
    input()
