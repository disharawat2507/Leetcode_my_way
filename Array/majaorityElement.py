# Leetcode 169. Majority Element
# Approach : This is Boyer-Moore Voting Algorithm. In this algo, we will select an element from the index everytime count is 0. if that element repeats we increase the count, else we decrease the count. once, the element reaches the end, the majority
# element is in the candidate varriable.
# Time Complexity: O(n)
# Space Complexity: O(1) . just using one varriable and pointer to increment

class Solution:
    def majaorityElement(self,nums1):
        candidate = nums[0]
        count = 0
        for i in range(len(nums1)):
            if count == 0:
                candidate = nums1[i]
                count +=1
            elif candidate == nums[i]:
                count +=1    
            elif nums[i] != candidate:
                count -=1
        return candidate  
