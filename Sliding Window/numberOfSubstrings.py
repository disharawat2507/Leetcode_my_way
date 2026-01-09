# LeetCode #1358: Number of Substrings Containing All Three Characters.
# Approach : since we know there are only 3 characters a,b,c. we created a map with these as keys. Iterating on the string and increasing their values. once all three keys have values greater than 1. we are
# calculating count by substracting the r index from the length of the string and removing the character from the left.Finally we return the count
# Time complexity : O(n)
# Space Complexity : O(n)

def numberOfSubstrings(s):
    l = 0
    count = 0
    cmap = {'a': 0, 'b': 0, 'c': 0}
    
    for r in range(len(s)):
        cmap[s[r]] += 1
        while cmap['a'] > 0 and cmap['b'] > 0 and cmap['c'] > 0:
            count += (len(s) - r) 
            cmap[s[l]] -= 1
            l += 1
            
    return count

char = 'bbacba'
print(numberOfSubstrings(char)) # Output: 7 
