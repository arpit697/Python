def maxmin(l):
    max = l[0]
    min = l[0]
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
        if l[i] < min:
            min = l[i]
    return max,min

l = [8]
print(maxmin(l))