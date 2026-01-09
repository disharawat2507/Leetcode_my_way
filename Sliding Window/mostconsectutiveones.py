# Find the maximum number of ones in the given array.
# Approach: Used Sliding Window and 2 Pointers approach here. Take 2 pointers and move one pointer until you get max of k zeros. Once the limit exceeds, start removing 0 from the other side of the array and keep incrementing th
# second pointer. Always calculate the maximum length using r-l +1 . return the maxlength.
# Time Complexity : O(n)
# Space Complexity : O(1)


chars =[1,1,1,0,0,0,1,1,1,1,0]
k = 2
def mostconsectutiveones(chars,k):
    l = 0
    maxcount = 0
    zerocount = 0
    for r in range(len(chars)):
        if chars[r] == 0:
            zerocount +=1
        while zerocount > k:
            if chars[l] == 0:
                zerocount -=1
            l +=1    
        maxcount = max(maxcount,r-l+1)
    return maxcount


print(mostconsectutiveones(chars,k))  
