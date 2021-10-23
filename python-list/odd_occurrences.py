# method 1
def findodd(l):
    result = None
    for x in l:
        count = l.count(x)
        if count %2 != 0:
            result = x
            break
    return result

################################################################################
# method 2
def findodd2(l):
    result = 0
    for x in l:
        result = result or x
    return result

l = [3,3,3,3,6,6,4,4,4,6,6,1,1,6,6,8,8,8]
answer = findodd2(l)

print(answer)
