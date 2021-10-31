def GetElementAtIndex(l,ind):
    if ind > len(l):
        return -1
    else:
        return l[ind]

l = [1,2,4,5,6,7,8,9,2]
ind = int(input('enter the index to find the element\n'))
print(GetElementAtIndex(l,ind))