# Find all subsequence where the sum of elements in array is a given number.
# Approach : Think of this approach like making a series of "Yes/No" decisions for every number in your list: at each step, you either put a number into your "bag" or you leave it out. By the time you reach the end of the list, you simply look inside your bag to see if the numbers add up to your target sum.
# If they do, you record that combination; if not, you backtrack by taking the last number out and trying the other "Yes/No" options you haven't explored yet until every possible combination has been checked.
# Time complexity : O(n . 2^n)
# Space Complexity : O(n)
#Example : subsequence(0,[1,2,1],2,0,[])


def subsequence(idx,arr,sumn,targetsum, res):
    if idx == len(arr) :
        if sumn == targetsum:
            print(res)
        return

    res.append(arr[idx])
    targetsum += arr[idx]
    subsequence(idx+1,arr,sumn,targetsum,res)
    res.pop()
    targetsum -= arr[idx]
    subsequence(idx+1,arr,sumn,targetsum,res)
