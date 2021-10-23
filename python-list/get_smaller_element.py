# def che(l,inpval):
#     smaller = []
#
#     for i in l:
#         if i < inpval:
#             smaller.append(i)
#
#     return smaller
#
#
# l = [10,50,22,11,1,3,4,6,100,51,74,345,23,63,734,23,3,6,7]
#
# inpval = int(input('enter a number to get smaller element list\n'))
#
# smaller = che(l,inpval)
#
# print(smaller)



####### through list comprehensions #######

def che(l,inpval):

    smaller = [x for x in l if inpval > x]
    return smaller

l = [10,50,22,11,1,3,4,6,100,51,74,345,23,63,734,23,3,6,7]
inpval = int(input('enter a number to get smaller element list\n'))

smaller = che(l,inpval)

print(smaller)
