# Leetcode 392. Is Subsequence
# Approach : take 2 pointers and place then in the starting of both the strings. keep on moving and checking if order follows. at the end, if the len of s string == the first pointer, that means all the elements in the
# string is found and return True. For every other case return false
# Time Complexity : O(n)
# Space Complexity : O(1). no extra space used , just 2 pointers

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                j += 1
            elif s[i] == t[j]:
                i+=1
                j +=1

        if i == len(s):
            return True

        return False  
