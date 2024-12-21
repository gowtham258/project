# rectangle perimeter
def p(w,h):
    return (w+h)*2
print(p(5,10))
print(p(4,6))
print(p(7,3))
print(p(2,8))
print(p(0,10))
# circle circumference
import math
def d(r):
    return 2*math.pi*r
print(d(3))
print(d(5))
print(d(7))
print(d(2))
print(d(0))
#  volume of a cylinder
def q(g,f):
    return math.pi*f*g**2
print(q(3,7))
print(q(5,10))
print(q(2,5))
print(q(7,4))
print(q(0,10))
# simple interest
def si(p,r,t):
    return p*r*t//100
print(si(1000,5,2))
print(si(2000,3,4))
print(si(1500,7,3))
print(si(500,10,1))
print(si(0,5,5))
# conversion
def con(f):
    return 5/9*(f-32)
print(con(32))
print(con(100))
print(con(212))
print(con(0))
print(con(-40))
