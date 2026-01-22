# Approach: we have given 2 sorted arrays. what we can do is place one pointer at the end of nums1 and second pointer at the starting of nums2. if num1[last] < nums2[start], swap both of them. else break(this is optimization)
# as from here we understood that everything before this element in nums1 is smaller and in nums2 after that element is bigger.
# Time Complexity: O(min(m,n) + n.log n + m.log m)
# Space Complexity : O(1)

class Solution:
    def mergesortedarrays(self, nums1, nums2):
        n = len(nums1) - 1
        m = 0
        while n >= 0 and m <len(nums2):
            if nums1[n] > nums2[m]:
                nums1[n], nums2[m] = nums2[m],nums1[n]
            else:
                break    
            n -= 1
            m += 1
   
   
        nums1.sort()
        nums2.sort() 
