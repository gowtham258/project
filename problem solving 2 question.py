# 1. second largest element 
def g(j):
    s=(set(j))
    if len(s)==1:
        return 'null'
    b=sorted(j)
    return b[len(j)-2]
print(g([1,2,3]))
print(g([5,1,2,4,3]))
print(g([3,3,3]))
print(g([1]))
# 2.reverse the string
def a(b):
    return b[::-1]
print(a('"hello"'))
print(a('"OpenAI"'))
print(a('""'))
print(a('"a"'))
# 3.finding common elements
def c(d,e):
    b=[]
    if len(d)==0 or len(e)==0:
        return b
    for v in d:
        for w in e:
            if v==w:
                b.append (v)
                e.remove(w)
    return b       
print(c([1,2,3],[2,3,4]))
print(c([1,5,7],[2,3,4]))
print(c([],[2,3,4]))
print(c([1,1,2],[1,2,2]))
# 4.sorting the array
def o(p):
    return sorted(p)
print(o([3,1,2]))
print(o([5,3,8,4,2]))
print(o([]))
print(o([1]))
# 5.majority element of array
def majority_element(arr):
    if not arr:
        return None
    candidate, count = None, 0
    for num in arr:
        if count == 0:
            candidate, count = num, 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    majority_count = len(arr) // 2
    count = 0 
    
    for num in arr:
        if num == candidate:
            count += 1
    if count > majority_count:
        return candidate
    else:
        return None
print(majority_element([3, 3, 4, 2, 4, 4, 2, 4]))  
print(majority_element([1, 2, 3, 4]))               
print(majority_element([1, 1, 2, 2, 1]))            
print(majority_element([]))                         
