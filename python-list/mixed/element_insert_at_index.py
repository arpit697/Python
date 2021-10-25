def ins(l,i,e):
    l.insert(i,e)
    return l


l = [1,2,3,4,5,6,7,8,9,10]
i = int(input('enter a index no where you want to insert a degit:-\t'))
e = int(input('enter a element:-\t'))

if i > len(l):
    print("index not found")

else:
    print(ins(l,i,e))
