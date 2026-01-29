# Leetcode 189. Rotate Array
# Approach: There can be a scenrio where the k > len(nums), so we have to find the modulo so that we will exactly know how many rotations are required. once we get the k, we will first reverse the first n-k elements.
# Then we will reverse the elements from n-k till end. finally we will reverse the whole array, to get the desired array
# Time Complexity: O(n)
# Space Complexity: O(1)
# class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        nums[:n-k] = nums[:n-k][::-1]
        nums[n-k:] = nums[n-k:][::-1]
        nums[:] = nums[::-1]
