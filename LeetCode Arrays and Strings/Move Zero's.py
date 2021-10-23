
def movez(l):# my function using copy of list
    x = []
    y = []

    for i in range (len(l)):
        if l[i] != 0:
            x.append(l[i])
        else :
            y.append(l[i])
    return x+y
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            
        for x in range(j,len(nums)):
            nums[x] = 0
        print(nums)
# l = [0,2,0,4,6,0,0,0,1,2,3,0]
# z = str(movez(l))
# print(z.replace(" ", ""));

s = Solution()
s.moveZeroes([0,1,0,3,12])