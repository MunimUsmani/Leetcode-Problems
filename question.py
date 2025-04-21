class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)              # Initialize result with the max element (important if all numbers are negative)
        curMin, curMax = 1, 1        # Track current min and max product

        for n in nums:
            temp = curMax * n        # Save current max * n before updating curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)   # Update result if curMax is greater
        return res
