import math,random,statistics
#area functions
def sqArea(a):
    return pow(a,2)

def recArea(l,b):
    return l*b

def triArea(b,h):
    return 0.5*b*h

def cirArea(r):
    return math.pi*math.pow(r,2)

#perimeter functions
def sqPeri(a):
    return 4*a

def recPeri(l,b):
    return 2*(l+b)

def triPeri(a,b,c):
    return a+b+c

def cirCir(r):
    return 2*math.pi*r

#curved surface area function
def cylSurf(r,h):
    return 2*math.pi*r*h
