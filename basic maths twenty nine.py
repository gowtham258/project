# area of rectangle
def a(width,height):
    return width*height
print(a(5,10))
print(a(4,6))
print(a(7,3))
print(a(2,8))
print(a(0,10))
# area of triangle
def b(base,height):
    return base*height//2
print(b(6,8))
print(b(5,10))
print(b(4,7))
print(b(8,3))
print(b(10,0))
# volume of cube
def v(l):
    return l**3
print(v(3))
print(v(4))
print(v(5))
print(v(6))
print(v(0))
# area of circle
import math
def w(r):
    return math.pi*r**2
print(w(3))
print(w(5))
print(w(7))
print(w(2))
print(w(0))
# meters to kilometers
def k(q):
    return q/1000
print(k(1000))
print(k(2500))
print(k(500))
print(k(20000))
print(k(0))