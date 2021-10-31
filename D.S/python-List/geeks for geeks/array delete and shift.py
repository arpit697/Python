def ArrayDeleteAndShift(l,ind):
    # l.pop(ind)
    for i in range(len(l)):
        if i == ind:
            continue
        print(l[i],end="")
    return l
l = [1,2,4,5,6,7,8,9,2]
ind = int(input('enter index where you want to delete the element\n'))
(ArrayDeleteAndShift(l,ind))