# Leetcode 455. Assign Cookies
# Approach : we are given 2 list, one has the number of children and other have the number of cookies. each child can hve cookies greater than equal to its value. so i sort the the number of children and no. of cookies.
# then i used 2 counter approach to traverse on each list, if the number of cookies and greater than equal to no. of children, we will make both counters move else only the cookies counter. finally we return the index of 
# children counter to see how many children got cookies.
# Time Complexity: O(mlog m + nlog n)
# Space Complexity : O(1)

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r = 0,0
        g.sort()
        s.sort()
        while l < len(g) and r < len(s):
            if g[l] <= s[r]:
                l +=1
                r += 1
            elif g[l] > s[r]:
                r+=1
            
        return l  
