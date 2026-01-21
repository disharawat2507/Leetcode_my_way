# Find the leaders of the array in same order they are. Leader is a element which doesnot have any larger element in its right.
# Approach: we will iterate from the end of the list, so we know that the last element will always be a leader. Now, starting moving from right to left, if there is any element that is graeter than the last max element, add it
# to the res, make it as maxelement and move towards the left until you reach 0.

# Example nums = [1, 2, 5, 3, 1, 2]
# output:[5,3,2]
# Time Complexity: O(n)
# Space Complexity: O(k) , k is the number of leaders.

class Solution:
    def leaders(self, nums):
        maxnum = nums[-1]
        res =[]
        res.append(nums[-1])
        j = len(nums) -2
        while j >= 0:
            if nums[j] > maxnum:
                maxnum = nums[j]
                res.append(nums[j])
            j -=1
        return res[::-1]
