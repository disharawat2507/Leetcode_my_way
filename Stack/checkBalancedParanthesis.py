# Leetcode 20 Valid Paranthesis
# Approach : If ahve created a map of valid paranthesis which will be used in the method to find out if the closing n opening bracjets are correct. Then we are preserving opening brackets in a stack. whenever some closing brackets come, we see if the last opening bracjet
# is its pair. If yes, we pop it out from the stack, if not we return False. At the end we return true or false based on the size of stack, it is used because there can be a condition where number of brackets in the given string is even. so even if every bracket opening and closing
# are same, there might be one which doesnot have any pair.
# Time Complexity : O(n) , n is the number of brackets in the string
# Space Complexity : O(n)

class Solution():
    def checkBalancedParanthesis(self,str):
        stack =[]
        pmap ={'}':'{',')':'(',']':'['}
        for i in str:
            if i in pmap.values():
                stack.append(i)
            else:
                if stack and stack[-1] == pmap[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0 
