
# first method
def check(l):
    i=1                   # to decleare starting index
    while i < len(l):     # to traverse the given list
        if l[i] < l[i-1]: # to compare with the previous element
            return False
        i = i+1           # to increase the value of i
    return True
################################################################################

# second method
def check2(l):
    if l==sorted(l):
        print("yes")
    else:
        print("no")
################################################################################


l=[1,2,3,4,5,6,7,8,9]

result = check (l)        # function call

print(result)

check2(l)
