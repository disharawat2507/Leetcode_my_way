# Leetcode 128. Longest Consecutive Sequence
# Approach: Convert the nums list into set so that there is no duplicates and easy to find out the length. iterate on the set, if num -1 doesnot exists , make count as 1 and then keep on increasing the count till num +1 
# exists and always change num to num+1. calculate the highest count. return maxcount
# Time Complexity : O(n)
# Space Complexity : O(1)

class Solution:
    def longestConsecutive(self, nums):
        numset = set(nums)
        maxcount = 0
        for num in numset:
            if num -1 not in numset:
                count = 1
                current = num
                while current+1 in numset:
                    count +=1
                    current = current+1
                maxcount = max(maxcount, count) 
        return maxcount 
