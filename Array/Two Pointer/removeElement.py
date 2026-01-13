# Leetcode 28 Remove Element
# Approach : Take a pointer(j) starting at zero and iterate over the nums list. If the element is not equal to the target value, put nums[j] = nums[i] and increase the j pointer. This will ensure that every element that is
# not equal to the target value, moves up in the array and remaining values(same as target value) are at the end.
# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j +=1
        return j  
