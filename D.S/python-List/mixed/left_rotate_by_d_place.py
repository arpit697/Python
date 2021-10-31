# method 1 (list slicing)
def lr1(l,d):
    l = l[d:] + l[:d]
    return l
