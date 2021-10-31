def majority(l,x,y):
    c1 = 0
    c2 = 0
    for i in range(len(l)):
        if l[i] == x:
            c1 += 1
        if l[i] == y:
            c2 +=1
    if c1 > c2:
        return c1
    else:
        return c2

l = [1,2,3,4,5,6,7,8]
x = int(input('enter the second element\n'))
y = int(input('enter the second element\n'))
print(majority(l,x,y))