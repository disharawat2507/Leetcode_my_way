# LeetCode #155: Min Stack
# Approach : In push method we are maintaining the lowest val till now by using the tuples,tuples(val added, min of all the added value), this is useful in gettop method, as now we just have to see the last tuple and return the value. In all the methods we used the concept of stack 
# ie; LIFO.
# Time Complexity : O(1) for each method
# Space Complexity : O(n) , number of elements inserted

class Solution():
    def __init__(self):
        self.stack =[]
    def push(self,val):
        if len(self.stack) == 0 :
            self.stack.append((val,val))
        else:
            self.stack.append((val, min(val,self.stack[-1][1])))

    def getMin(self):
        return self.stack[-1][1]

    def getTop(self):
        return self.stack[-1][0]

    def deletetop(self):
        if self.stack:
            self.stack.pop()
        return self.stack                    
        
