def getmax(l):             # function no 1

    for x in l:
        for y in l:
            if y > x:
                break
        else:               # else statement with for loop
            return x
    return None

def getmax2(l):             # function no 2

    if not l:
        return None
    else:
        temp = l[0]

        for x in range(1,len(l)):
            if l[x] > temp:
                temp = l[x]
    return temp


l = [1,2,3,4]

maxval2 = getmax2(l)
maxval = getmax(l)

print(maxval)
print(maxval2)
