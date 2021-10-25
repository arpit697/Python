def InsertAtEnd(l,ele):
    l.append(ele)
    return l

l = [1,2,4,5,6,7,8,9,2]
ele = int(input('enter element which you want insert at end of list\n'))

print(InsertAtEnd(l,ele))