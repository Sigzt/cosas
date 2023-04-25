from graphics import *
from math import *
from customtools import *
import random
dim = 800
bound = lambda x,y : sqrt((dim/2- x+50)**2 + (dim/2 - y+50)**2)
win = GraphWin("hola!",dim+200,dim+200)
p = Point(dim/2+100,dim/2+100)
dx,dy = dim/40,dim/40
def move(p,col,td):
    d = bound(p.x,p.y)
    x,y = p.x,p.y
    if d >td and 1000>d:
        x = x+(dim/2 - p.x + 50)/d*dx
        y = y+(dim/2 - p.y + 50)/d*dy
    th = random.random()*2*pi
    x,y = x + dx*cos(th),y + dy*sin(th)
    #x,y = x + dx*(abs(sin(th))<abs(cos(th)))*sign(cos(th))*0.5,y + dy*(abs(sin(th))>abs(cos(th)))*sign(sin(th))*0.5
    #th2 = random.random()*2*pi
    #x,y = x + dx*(abs(sin(th2))<abs(cos(th2)))*cos(th2)*0.5,y + dy*(abs(sin(th2))>abs(cos(th2)))*sin(th2)*0.5
    p.undraw()
    win.create_line(p.x,p.y,x,y,fill = col)
    p = Point(x,y)
    p.draw
    return p



for k in range(1):
    p = Point(dim/2+50,dim/2+50)
    for j in range(10000):
        p = move(p,"black",dim/2)
    move(p,"red",dim/2)

"""
for j in range(30):
    p = Point(dim/2+50,dim/2+50)
    co = color_rgb(random.randint(10,80),0,0)
    for i in range(400):       
        p = move(p,co,dim/2)   
    co = color_rgb(random.randint(100,255),0,0)
    for i in range(600):        
        p = move(p,co,dim/2)
for j in range(12):
    p = Point(dim/2+50,dim/2+50)
    dx,dy = dim/12,dim/12
    for i in range(40):
        co = color_rgb(random.randint(150,255),random.randint(150,255),0)        
        p = move(p,co,dim/2)
"""
input()