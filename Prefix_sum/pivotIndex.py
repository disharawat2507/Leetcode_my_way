# Leetcode 724. Find Pivot Index
# Approach : I have calculated the total sum in the begining, assigned leftsum as 0. now im iterating on the loop. adding element to leftsum, if leftsum == totalsum, i m returning i, else i m substracting element[i] from totalsum.
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            leftsum +=nums[i]
            if leftsum == totalsum:
                return i 
            else:
                totalsum -= nums[i]

        return -1   
