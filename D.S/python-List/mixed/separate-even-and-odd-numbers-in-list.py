# def evenodd(l):
#     even=[]
#     odd=[]
#
#     for i in l:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#
#     return even,odd
#
# l = [1,2,3,4,5,6,7,8,9,10]
#
# even,odd = evenodd(l)
# print(even)
# print(odd)

############ question through list comprehensions ##########
def evenodd(l):
    l1 = [x for x in l if x%2==0]
    l2 = [x for x in l if x%2!=0]
    print(l1)
    print(l2)

l = [1,2,3,4,5,6,7,8,9,10]
evenodd(l)
