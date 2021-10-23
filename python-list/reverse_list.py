# method 1
def rev1(l):
    l.reverse()
    return l
################################################################################
# method 2
def rev2(l):
    new_l= l[::-1]
    return new_l
################################################################################
# method 3
def rev3(l):
    new_l = list(reversed(l))
    return new_l
################################################################################
# method 4
def rev4(l):
    l1 = []
    for x in range(len(l),0,-1):
        l1.append(x)
    return l1
################################################################################
# method 5
def rev5(l):
    s=0
    e= len(l)-1
    while s<e:
        l[s],l[e] = l[e],l[s]
        s = s+1
        e = e-1
    return l
    
l = [1,2,3,4,5,6,7,8,9,10]
print(rev5(l))
