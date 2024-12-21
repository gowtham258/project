# 1.write a function to check given number is odd or even
def a(b):
    # if it's a even number it will return give output as even
    if b%2==0:
        return 'Even'
    # if it's a odd number it will return give output as odd
    else:
        return 'Odd'
print(a(4))
print(a(7))
print(a(0))
print(a(-3))
# 2.sum of elements in array
def c(d):
    b=0
    # we are itrating over given list and adding the elements to a variable and returning it
    for y in range (len(d)):
        b+=d[y]
    return b
print(c([1,2,3]))
print(c([-1,-2,-3]))
print(c([]))
print(c([0]))
# 3.maximum number in array
def i(j):
    # we should take a variable which will be less than given numbers
    a=-1000
    # if there are no elements in array then it should return and it should not go to for loop also so we  are writing it before for loop and it will return null 
    if len(j)==0:
            return 'null'
    for r in range (len(j)):
        # we are itrating over given list if given number is greater than -1000 then it will be updated as given variable will be updated
        if j[r]>a:
            a=j[r]
    return a
print(i([1,2,3]))
print(i([-5,-1,-10]))
print(i([5]))
print(i([]))
# 4.check given no is positive or negative or zero
def y(z):
    # we are checking given number is positive if it is greater than 0
    if z>0:
        return 'Positive'
    # we are checking given number is positive if it is less than 0
    elif z<0:
        return 'Negative'
    # if it's 0 we returning as zero
    else:
        return 'Zero'
print(y(3))
print(y(-1))
print(y(0))
# 5. Number of odd elements in array
def s(t):
    g=0
    # if there are no elements in array then it should return and it should not go to for loop also so we  are writing it before for loop and it will return 0
    if len(t)==0:
        return 0
    for h in range (len(t)):
        # we are itrating over given list and checking if it is divided by 2 and give remainder which is not 0 then it is odd number
        if (h[t])%2!=0:
            g+=1
    return g
print(s([1,2,3,4,5]))
print(s([2,4,6]))
print(s([]))
print(s([1,3,5,7,9]))