# Leetcode 509
# Approach : I have kept one library where in every key have value as summation of its previous 2 fibonnaci series. This way double calulation is skipped and time complexity is reduced from O(n^2)
# Example : print(mainfunc(4))
# Time Complexity : O(n)
memo ={}
def callfibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] =  callfibonacci(n-1) +callfibonacci(n-2)
    return memo[n] 


def mainfunc(n):
    return callfibonacci(n)

    
