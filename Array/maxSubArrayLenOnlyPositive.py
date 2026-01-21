# Approach: We are considering if the given nums array have only positive integers. We will initialize sum to 0 and maxcount to 0. we will keep on adding nums until the sumn becomes greater than 0 or inbetween if we find
# any pairs where sum is equal to the target. if sum becomes greater than 0 , we will start to delete the elements from left for the  sum. at the end, we return maxcount
# Time Complexity : O(n)
# Space Complexity: O(1)

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        left = 0
        sumn = 0
        maxcount = 0
        for right in range(len(nums)):
            sumn += nums[right]

            while sumn > k and left <= right:
                sumn -= nums[left]
                left += 1
            if sumn == k:
                maxcount = max(maxcount, right - left +1)

        return maxcount  
