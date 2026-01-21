# In this question, the number of positive numbers and negative numbers are not same.
# Approach : We have used brute force method for solving this question. First find out all positive and negative numbers . iterate on list till both arrays have values. after that just use extend to store the remaining values
# from both the arrays. Return the result array.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def alternateNumbers(self, nums):
        pos_res =[]
        neg_res =[]
        res =[]
        for i in range(len(nums)):
            if nums[i]>0:
                pos_res.append(nums[i])
            else:
                neg_res.append(nums[i])
        i = 0
        while i < len(pos_res) and i<len(neg_res):
            res.append(pos_res[i])
            res.append(neg_res[i])
            i += 1

        res.extend(pos_res[i:])
        res.extend(neg_res[i:])

        return res 
