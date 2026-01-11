# Check whether a string is palindrome or not using recursion.
# Approach : from main function, call recursive function where we send the start index, string and the end index. keep on calling until start is less than end and the element at start and end index of the string are equal.Otherwise return False.
# Example: print(mainf('ABBA'))
# Time Complexity : O(n)
# Space Complexity : O(n)


def checkpalindrome(start, string, end):
    if start < end:
        if string[start] == string[end]:
            return  checkpalindrome(start+1, string, end -1) 
        else:
            return False
    return True                    



def mainf(string):
    return checkpalindrome(0,string,len(string)-1)


print(mainf('ABBA'))
