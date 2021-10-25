def majority(l,x,y):
    a,b = 0,0
    for i in range (len(l)):
        if l[i] == x:
            a = a+1
        else:
            pass
        if l[i] == y:
            b = b+1
        else:
            pass

    return a,b

l = [1,2,3,4,5,6,7,8]
x = 4
y = 5
ele1,ele2 = majority(l,x,y)

if ele1 < ele2:
    print(ele2)
else:
    print(ele1)


