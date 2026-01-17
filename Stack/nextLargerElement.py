# Leetcode 496: Next Greater Element I
# Approach : we start checking from the end of the array so that in advance we know what are the big numbers towards the right of any number from the left. We initialise res array with -1 and its len is equal to the length of the array. while iterating we have to
# check that the element in stack is greater than the current element, if yes, put the value in result at the jth index else pop the elements from the array until you found some big element. At the end, return the result.
# Time complexity : O(n)
# Space Complexity : O(n)
  
class Solution:
    def nextLargerElement(self, arr):   
        j = len(arr) - 1
        stack =[]
        res = [-1] * len(arr)

        while j >= 0:
            while stack and stack[-1] <= arr[j]:
                stack.pop()
            if stack :
                res[j] = stack[-1]
            stack.append(arr[j])
            j -=1
        return res   
