def InsertAtIndex(l,ind,ele):
    l.insert(ind,ele)
    return l

l = [1,2,4,5,6,7,8,9,2]
ind =int(input('enter index where you want to insert\n'))
ele = int(input('enter element which you want insert at end of list\n'))
print(InsertAtIndex(l,ind,ele))