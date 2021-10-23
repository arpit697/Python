def mxmin(l):
    mx = l[0]
    mn = l[0]
    for i in range(len(l)-1):
        if l[i] > mx:
            mx = l[i]
        if l[i] < mn:
            mn = l[i]

    return mx,mn

l = []
print (mxmin(l))

# not done yet