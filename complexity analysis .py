# 1.writing first element
def a(b,c):
    return b[c]
print(a([5,10,15],0))
# # 2.logarthimic time complexity
import math
def logarithmic_run(n):
    count = 0
    while n > 1:
        n //= 2 
        count += 1
    return count
print(logarithmic_run(100))
print(logarithmic_run(1000))
# 3.linear time complexity
def i(j):
    a=0
    for r in range (len(j)):
        if j[r]>a:
            a=j[r]
    return a
print(i([4,1,7,2,9]))
# 4.linear time complexity
def m(n):
    k=0
    for f in range (len(n)):
        if n[f]%2==0:
            k+=1
    return k
print(m([1,2,3,4,5]))
# 5.quadratic time complexity
def k(l,u):
    c=[]
    for m in range (len(l)):
        for n in range (m+1,len(l)):
            if l[m]+l[n]==u:
                c.append((l[m],l[n]))
    return c
print(k([1,2,3,4,5],6))
print(k([0, -1, 2, -3, 1], -2)) 
# 6.cubic time complexity
def d(a):
    result = []
    for i in a:       
        for j in a:   
            for k in a:  
                result.append((i, j, k))
    return result
print(d([1,2,3]))
# 7.fibonacci series
def f(n):
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)
print(f(5)) 
print(f(6))  
# 8.writing duplicate element
def duplicate_elements(arr):
    result = []
    for num in arr:
        result.append(num)
        result.append(num)
    return result
print(duplicate_elements([1, 2, 3]))
