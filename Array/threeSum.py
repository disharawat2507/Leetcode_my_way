# Leetcode 15. 3 Sum
# Approach : we will sort the numbers in the first place so that we donot have to sorting and will be helpful in not adding duplicates. We will iterate on the list and keep i idx fixed and check if there are any other 2 numbers
# which can be added to element at ith index to make it 0. This we have to do till k > j. as j is i+1 but k is the len of nums -1. if the sum is greater than 0, we have to move k to left, if sum is less than 0 we have to move j 
# towards right and if the sum is 0, we will append the 3 numbers in the form of list in result. now once added we will move j by 1 and reduce k by 1 to find new pairs with element at ith index. now, there can be possibility that 
# the elements are repeating. so , we will move j and k till they are not similar from the past.
# Time Complexity : O(n^2)
# Space Complexity : O(n)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums) -1
            while j < k:
                sumn = nums[i] + nums[j] + nums[k]
                if sumn < 0:
                    j +=1
                elif sumn > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j +=1
                    k -=1
                    while j < k and nums[j] == nums[j-1]:
                        j +=1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return res                        

