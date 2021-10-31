def isgreater(l,x):
    greater = float('inf')
    for i in range(len(l)):
        if l[i] > x:
            if greater > l[i]:
                greater = l[i]
    return greater

l = [1,2,3,4,5,6,7,8,9,0]
x = 2
print(isgreater(l,x))