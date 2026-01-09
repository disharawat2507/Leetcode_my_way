# Calculate maximum points you can obtain from two cards.
# nums = [1,2,3,4,5,6,7,8,9] , k = 4
# Approach : The condition is the 4 numbers should be either from the back or front not from the middle.examples: [(1,2,3,4),(1,2,3,9),(1,2,9,8)....(6,7,8,9)]. We will first get sum of first k cards. Loop over the nums to keep on removing the cards from left sum
# and keep adding nums from the right side. this approach will give all the valid number sets. each time calculate the maxsum. At the end return maxsum.
# Time complexity : O(n)
# Space Complexity : O(1)


def maxpoints(nums,k):
    lsum = sum(nums[0:k])
    rsum = 0
    maxsum = lsum
    n = len(nums)
    ridx = n-1
    for i in range(k-1,-1,-1):
        lsum -= nums[k-1-i]
        rsum +=nums[ridx]
        ridx -=1
        maxsum = max(maxsum , lsum +rsum)
        print('maxsum::',maxsum)

    print(maxsum)
    return maxsum
