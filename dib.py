from graphics import *
from math import *
from customtools import *
a = 300
win = GraphWin("hola!",a,a)
ajuste = lambda x: Point(x[0],a/2-x[1])
phi = (1+sqrt(5))/2
def curvas(n,r,funx,funy,perm):
    x = [(i-n)/n*r[0] + i/n*r[1] for i in range(1,n+1)]
    p = [ajuste([funx(a),funy(a)]) for a in x]
    for a in p:
        a.draw(win)
    li = [Line(p[i],p[i+1]) for i in range(len(p)-1)]
    for l in li:
        l.draw(win)
def oa ():
    Line(Point(0,a/2),Point(a,a/2)).draw(win)
def fractal(dim,r,it,di,palette):
    fun = lambda x,c:x**2+c
    fun2 = lambda x,c: (abs(x.real)+abs(x.imag)*1j)**2 + c
    mapa = lattice(r,r,[dim,dim])
    puntos = [[convergence(z,fun,it,di)  for z in l]for l in mapa]
    print("hola")
    dx,dy = lrandomlist(dim,3),lrandomlist(dim,3)
    [[fastplot(dx[i],dy[j], puntos[i][j]) for j in range(0,dim+1)] for i in range(0,dim+1)]
    return mapa
def fastplot(x,y,col):
    win.create_line(x,y,x+2,y+2, fill=col)
def convergence(p,fun,it,di):
    a,i = p,0
    while mod(a)<di and i<it:
        i = i + 1
        a = fun(a,p)
    if it == i:
        return "black"
    #return color_rgb(0,10*i,8*i)
    return color_rgb(int(100*abs((mod(a))))%255,int(80*abs((mod(a))))%255,int(100*abs((mod(a))))%255)
    return color_rgb(int(abs(110*tanh(fmod(a)/6)))+10,int(abs(100*(sin(mod(2*a))**2)+abs(cos(mod(a)))))+10,int(abs(120*cos(mod(2*a))))+15)
    if fmod(a-p)>3:
        return 3
    if fmod(a-p)>2:
        return 2
    if fmod(a-p)>0:
        return 1
    return 0        
#curvas(100,[0,5],lambda x: 400*log(x),lambda x: 40*sin(x),20)
win.plot(200,200,"red")
m = fractal(300,[-2,2],20,2,["black","teal","turquoise","blue"])
fun = lambda x,c: x**2+c
while True:
    a = win.getMouse()
    x,y = int(a.x),int(a.y)
    p0 = m[x][y]
    p = p0
    rp = [x,y]
    for i in range(10):
        p1 = fun(p,p0)
        rp1 = [(p1.real+2)*75,300-(p1.imag+2)*75]
        win.create_line(rp[0],rp[1],rp1[0],rp1[1],fill="white")
        p = p1
        rp = rp1
    print(p)
