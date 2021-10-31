from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) -1
        boats_number = 0

        while left <= right:
            if left == right:
                boats_number += 1
                break

            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats_number += 1
        

        return boats_number

s = Solution()
print(s.numRescueBoats([2,3,2,4,3,4,1,2,3,3,3,3,3,3,3,33],4))

