# 1.ratiio
def d(a,b):
    if a==0 or b==0:
        print('infinity')
    return a/b
print(d(6,3))
print(d(9,4))
print(d(10,5))
print(d(15,3))
print(d(8,2))
# print(d(1,0))
#  2.exponent calculation
def c(p,q):
    return p**q
print(c(2,3))
print(c(5,2))
print(c(7,0))
print(c(10,1))
print(c(3,4))
print(c(0,0))
# 3.square root calculation
import math
def s(t):
    if t<0:
        return 'NaN'
    return math.sqrt (t)
print(s(16))
print(s(25))
print(s(49))
print(s(9))
print(s(100))
print(s(0))
print(s(-9))
# 4.discount calculation
def q(r,s):
    return r-r*s/100
print(q(100,20))
print(q(250,15))
print(q(500,10))
print(q(800,25))
print(q(1200,5))
print(q(500,100))
print(q(500,0))
# 5.random number
import random
def g(a,b):
    if a>=b:
        return 'data invalid'
    return random.randint(a,b)
print(g(1,10))
print(g(5,15))
print(g(10,20))
print(g(30,40))
print(g(100,200))
print(g(10,10))
