# Leetcode 56. Merge Intervals
# Approach : First, we sort the intervals by their start times. We then iterate through the intervals, comparing the current interval with the last one added to our result list.
# If the result list is empty or the end of the last interval is less than the start of the current one, there is no overlap, so we append the current interval. Otherwise, an overlap exists, and we merge 
# them by updating the end of the last interval to be the maximum of its current end and the end of the new interval.
# Time Complexity : O(n)
# Space Complexity : O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res =[]
        for i in range(len(intervals)):
            if len(res) == 0 or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]  

        return res          
        
