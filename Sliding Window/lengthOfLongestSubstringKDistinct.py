# Leetcode 340
# Approach : to check the length and frequency of each elemnt in the string we will use a map. everytime the lenof map keys is greater than k, we will start removing the elements from the left and 
# calculate the maxlength.
# Time complexity: O(n)
# Space Complexity : O(k)


class Solution:
    def lengthOfLongestSubstringKDistinct(self, char: str, k: int) -> int:
        l = 0
        cmap ={}
        maxlength = 0
        for r in range(len(char)):
            if char[r] not in cmap:
                cmap[char[r]] =1
            else:
                cmap[char[r]] += 1

            while len(cmap.keys()) > k:
                cmap[char[l]] -= 1
                if cmap[char[l]] == 0:
                    del cmap[char[l]]  
                l +=1
            maxlength = max(maxlength, r-l+1)   
        return maxlength
