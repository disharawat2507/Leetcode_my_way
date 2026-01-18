# Find nearest smallest number from the left
# Approach: start from the left. in the stack keep on checking if the last element is greater than equal to the current element in the list, if yes, keeping on poping the elements until it becomes small as we are finding small elements.Then place the element in the
# jth position in result and append the element to the stack.
# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution:
    def nextSmallerElements(self, arr): 
        j = 0
        res = [-1] * len(arr)
        stack =[]
        while j < len(arr):
            while stack and stack[-1] >= arr[j]:
                stack.pop()
            if stack:
                res[j] = stack[-1]    
            stack.append(arr[j])
            j+=1  

        return res   
