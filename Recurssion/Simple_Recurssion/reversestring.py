# Reverse a string.
# Approach : main function calls the recursive function for the very first time only. in recursive function, we check if the length of nums is greater than -1 , append the nth element into the result, and again call itself but now the n will be changed to n-1.
# The break condition in this recursive function is when n becomes -1, that means all the nums are covered and donot restart again. If this condition is satisfied return the result.
# Example :  print(mainf([1,2,3]))
# Time Complexity : O(n)
# Space Complexity : O(n)

def reversearray(n, nums, res):
    if n >-1:
        res.append(nums[n])
        return reversearray(n-1, nums, res)
    else:
        return res    


def mainf(nums):
    return reversearray(len(nums)-1, nums,[])


print(mainf([1,2,3]))
