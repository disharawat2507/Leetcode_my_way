# Leetcode 18. 4Sum
# Approach : we will follow the same approach as that in 3 sum. In this we will first make i and j as constant and move k and l. once that is done we will move j for each i. and finally we will move i. We have sorted the
# nums in advance so that there is no duplicate issue later. we will also keep on increasing k and decreasing l until they are not same as their previous value
# Time Complexity : O(n^3)
# Space Complexity : O(n)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res =[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j +1
                l = len(nums)-1
                while k < l:
                    sumn = nums[i]+nums[j]+nums[k]+nums[l]
                    if sumn == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k +=1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k +=1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif sumn > target:
                        l -= 1
                    elif sumn < target:
                        k += 1

        return res                                        

        
