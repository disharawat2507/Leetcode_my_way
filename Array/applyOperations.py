# Leetcode 2460. Apply Operations to an Array
# Approach : First is the simplest part, just check if element and its just next element are same or not. if yes, multiple the first one by 2 and make other as 0. Otherwise, skip the operation.
# for sort part where all zeros should be at the end, take one pointer j and make it 0. whenerver the element is not zero, just swap the elements and increment the j counter. on doing the same, the result will have all the zeros
# at the end of the nums
# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0
        
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[i], nums[j] = nums[j], nums[i]
                j +=1

        return nums 
