# Leetcode 402: Remove K Digits
# Approach : keep on checking if the value in stack is greater than the current value, if yes, pop it out decrease k counter and then add the current element to the stack. There are certain edge cases, like what if k >= length of array or k is not yet zero and all
# elements are added in the stack or there are few zeros in the begining that are making no sense ('00200'). for that we have used lstrip, if k is not zero , we are only considering the stack from 0 till -k. in end we are return the stack in string form.
# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def removeKdigits(self, nums, k):  
        stack = []
        for i in nums:
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1    
            stack.append(i)  
        fin_stack = stack[0:-k] if k >0 else stack   
        res = ''.join(fin_stack).lstrip('0')

        return res if len(res) >0 else '0' 
