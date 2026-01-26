# Leetcode 350. Intersection of Two Arrays II
# Approach : make a map with the elements and number of times it is repeated in any one array. then iterate on second array and check if the map contains that elementa nd count of it is greater than 0, then add that element
# to the result array and decrease its count. This will insure that if there is a repeating array in one list and not in other , it will come only once
# Time Complexity : O(m+n)
# Space Complexity : min(O(m,n))

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        res =[]
        for i in nums2:
            if count[i] >0:
                res.append(i)
                count[i] -= 1

        return res   
