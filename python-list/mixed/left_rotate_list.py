# method 1
def leftr(l):
    nl= l[1:] + l[0:1]
    return nl
################################################################################
# method 2
def leftr1(l):
    temp = l[0]
    for x in range (1,len(l)):
        l[x-1]=l[x]
    l.append(temp)
    return l
l = [1,2,3,4,5,6,7,8,9,10]
print(leftr1(l))
