def issmaller(l,x):
    nl = []
    for i in range(len(l)):
        if l[i] < x:
            nl.append(l[i])
    return nl

l = [1,2,4,5,6,7,8,9,2]
x = int(input("enter a element\n"))
print(issmaller(l,x))
