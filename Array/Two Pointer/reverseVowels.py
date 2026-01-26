# Leetcode 345. Reverse Vowels of a String
# Approach : convert the string into list because string is immutable and i wont be able to swap elements in it. then take 2 pointers approach, one at start and one at end,keep on swaping where both the elements are 
# vowels. finally return the list that is converted into string
# Time Complexity: O(n)
# Space Complexity : O(n)


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels =['a','e','i','o','u']
        i = 0
        slist = list(s)
        j = len(slist) - 1
        while i < j:
            if slist[i].lower() not in vowels and slist[j].lower() not in vowels:
                i +=1
                j -= 1
            elif slist[i].lower() in vowels and slist[j].lower() in vowels:
                slist[i], slist[j] = slist[j],slist[i]
                i += 1
                j -= 1    
            elif slist[i].lower() in vowels and slist[j].lower() not in vowels:
                j -= 1
            elif  slist[i].lower() not in vowels and slist[j].lower()  in vowels:  
                i +=1   
        return ''.join(slist)             
