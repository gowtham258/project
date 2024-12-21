# 1.encode a string in base 64
import base64
def a(b):
    return base64.b64encode(b.encode()).decode()
print(a('Good morning'))
print(a('JavaScript is awesome!'))
print(a(''))
print(a(' '))
print(a('Encode123!'))
# 2.decode a base 64 string
import base64
def y(z):
    return base64.b64decode(z.encode()).decode()
print(y(("U2ltcGxlIFRleHQ=")))
print(y(("T25lIFJvY2s=")))
print(y(("SmF2YVNjcmlwdCBNYWdpYw==")))
print(y(("")))
print(y(("c2VjcmV0==")))
# 3.casear cipher
def d(string,shift):
    r=''
    for a in string:
        b=ord(a)
        if 65<=b<=90:
            c=((b+shift-65)%26)+65
            r+=chr(c)
            # b=ord(a)
        elif 97<=b<=122:
            b=ord(a)
            c=(b+shift-97)%26+97
            r+=chr(c)
        else:
            r+=a
    return r
print(d('abc',3))
print(d('open',2))
print(d('xyz',5))
print(d('HELLO',4))
print(d('pass123',3))
# 4.decipher a string
def d(string,shift):
    r=''
    for a in string:
        b=ord(a)
        if 65<=b<=90:
            c=((b-shift-65)%26)+65
            r+=chr(c)
            # b=ord(a)
        elif 97<=b<=122:
            b=ord(a)
            c=(b-shift-97)%26+97
            r+=chr(c)
        else:
            r+=a
    return r
print(d('def',3))
print(d('qrgo',2))
print(d('cde',5))
print(d('LIPPS',4))
print(d('sdvv123',3))
# 5.calculation of area of circle
import math
null=0
def a(r):
    if r>0:
        return 'sufficient data.Area:',math.pi*r**2
    else:
        return 'Insufficient data'
print(a(7))
print(a(0))
print(a(null))
print(a(10))
print(a(-5))