# 1.perimeter of rectangle
null=0
def p(a,b):
    if a>0 and b>0:
        return 'Sufficient data.perimeter:'+str((a+b)*2)
    else:
        return 'Insufficient d'
print(p(5,4))
print(p(null,10))
print(p(7,0))
print(p(9,6))
print(p(8,null))
# 2.date difference 
from datetime import datetime
import math
def a(c,d):
    z="%Y-%m-%d"
    c=datetime.strptime(c,z)
    d=datetime.strptime(d,z)
    return abs((d-c).days)
print(a("2024-01-01","2024-01-10"))
print(a("2024-12-31","2025-01-01"))
print(a("2024-02-28","2024-03-01"))
print(a("2023-09-18","2024-09-18"))
print(a("2024-09-18","2024-09-10"))
# 3.calculate day 
from datetime import datetime
def s(m):
    f='%Y-%m-%d'
    d=datetime.strptime(m,f)
    return d.strftime(('"%A"'))
print(s("2024-01-01"))
print(s("2024-09-18"))
print(s("2023-12-25"))
print(s("2025-07-04"))
print(s("2022-02-28"))
# 4.boolean and operation
def t(p,q):
    if p=='true'and q=='true':
        return 'true'
    else:
        return 'false'
print(t('true','true'))
print(t('true','false'))
print(t('false','false'))
print(t('false','true'))
print(t('true','true'))
# 5.boolean OR operation
def u(v,w):
    if v=='true' and w=='false' or w=='true':
        return 'true'
    elif v=='false' and w=='true':
        return 'true'
    else:
        return 'false'
print(u('true','true'))
print(u('true','false'))
print(u('false','false'))
print(u('false','true'))
print(u('false','false'))
# 6.directions
def d(a,b):
    if a=='north' and b=='left'or a=='south' and b=='right':
        return 'west'
    elif a=='east' and b=='right'or a=='west' and b=='left':
        return 'south'
    elif a=='south' and b=='left' or a=='north' and b=='right':
        return 'east'
    elif a=='west' and b=='right' or a=='east' and b=='left':
        return 'north'
print(d('north','left'))
print(d('east','right'))
print(d('south','left'))
print(d('west','right'))
print(d('north','right'))
