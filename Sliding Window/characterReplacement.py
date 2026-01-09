# Leetcode : 424 Longest Repeating Character Replacement
# Approach : We have taken a map where we are storing each character and their occurence. for each of them we are checking if the window size - their maxfreq > k, then we are subscrtracting 1 from their value until the condition
# is not satisfied. finally we calculate the max size and return it.
# Time Complexity : O(n)



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxfreq , maxcount =0,0
        cmap ={}

        for r in range(len(s)):
            cmap[s[r]] = cmap.get(s[r],0) +1
            maxfreq = max(maxfreq,cmap[s[r]])

            while r-l+1 - maxfreq > k:
                cmap[s[l]] -= 1
                l += 1
            maxcount = max(maxcount, r-l+1)
        return maxcount   
