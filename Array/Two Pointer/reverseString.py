# Leetcode : 344. Reverse String
# Approach : Take 2 pointers , one at begining of list and the other at the end of list. while the end pointer is greater than the begining pointer, keep on swapping the valies at those indexes. increment the left pointer
# and decrement the right pointer after every swap.
# Time Complexity : O(n)
# Space Complexity : O(1)
  
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while j > i:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1

        return s    
