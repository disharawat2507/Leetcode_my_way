# Leetcode 503 (Next Greater Element II)
# Approach : Since, we have to see if there is no greater element in the right side, check the left side as well if there exists any, we will use the concept of circular array. hence we take j as 2(len(array)) - 1. we will everytime check if the array at (j%n) position is 
# greater than the stack[-1] element or not, if not pop the elements out.
# Time complexity : O(n). n is the number of elements
# Space Complexity : O(n) . n is the number of elements

class Solution:
    def nextGreaterElements(self, arr): 
        n = len(arr)  
        j = 2 * len(arr) -1
        stack =[]
        res = [-1] * len(arr)
        while j >= 0:
            curr_val = arr[j%n]
            while stack and stack[-1] <= curr_val:
                stack.pop()
            if j < n:
                res[j] = stack[-1] if len(stack) > 0 else -1

            stack.append(curr_val) 
            j -=1
        return res   
