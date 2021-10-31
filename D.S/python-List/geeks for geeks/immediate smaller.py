def issmaller(l,x):
    smaller = 0
    for i in range(len(l)):
        if l[i]<x:
            if smaller < l[i]:
                smaller = l[i]
    return smaller

l = [1,2,3,4,5,6,7,8,9,0]
x = 5
print(issmaller(l,x))