# Leetcode 151. Reverse Words in a String
# Approach: Split the string to form a list. iterate on the list and add the elements to the result list where element is not null. Reverse the list, convert it into string form and return.
# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        revstring = s.split()
        res =[]
        for i in range(len(revstring)):
            if revstring[i] !='':
                res.append(revstring[i])
        return ' '.join(res[::-1])        
        
              


        
