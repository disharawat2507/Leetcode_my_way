This is Longest Subarray with at most K distinct elements.
Approach : I have taken a hashmap so that i can keep track of unique keys and whenever unique key count is greater than K, i am removing the values by using 2nd pointer and moving it everytime(shrinkimg the window size)
Time Complexity : O(n)
Space Complexity : O(k)

def fruitintobasket(char,k):
    l = 0
    maxlength = 0
    nummap ={}
    for r in range(len(char)):
        if char[r] not in nummap :
            nummap[char[r]] = 1
        else:
            nummap[char[r]] +=1

        while len(nummap.keys()) > k:
            nummap[char[l]] -=1
            if nummap[char[l]] == 0:
                del nummap[char[l]]
            l +=1    
        maxlength = max(maxlength,r-l+1)

    return maxlength 
