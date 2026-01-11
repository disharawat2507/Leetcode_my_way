# Leetcode 78
# Approach : Here we are using backtracking and recurrsion method. whenever the idx is less the length of the array, we are adding element at that idx of the array to our result and and calling the function with next array. 
# Once it reaches the length of the array, we start removing the elements from there and then again calling the same function so that next subsequence could be added.
# Time Complexity : O(n . 2^n)

def callsubsequenceRecursion(idx,n, arr, result):
    if (idx >= n):
        print(result)
        return
    result.append(arr[idx])
    callsubsequenceRecursion(idx+1,n,arr, result)
    result.remove(arr[idx])
    callsubsequenceRecursion(idx+1,n,arr, result)

def subsequenceRecursion(arr):
    return callsubsequenceRecursion(0, len(arr), arr,[])
