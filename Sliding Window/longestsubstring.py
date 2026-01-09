# Find the longest substring without repetition.
# Approach: iterate on the string, keep on adding the characters than doesnot pre-exits in the set. If some repeating characters occurs, keep remove the characters from the left of the string until the repeating character is gone, after that add the character into the
# set. Everytime add the character into the set and calculate the maxlength
# Time Complexity : O(n)
# Space Complexity : O(n)

def longestsubstring(chars):
    l=0
    maxlen = 0
    str = set()
    for r in range(len(chars)):    
        while chars[r] in str :
            str.remove(chars[l])
            l +=1
        str.add(chars[r])  
        maxlen = max(maxlen, r-l +1)   

    return maxlen
