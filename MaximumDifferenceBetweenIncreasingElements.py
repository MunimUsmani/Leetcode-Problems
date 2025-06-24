class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        xMin, n = 10**9, len(nums)  # Initialize min value and length
        maxD = -1                   # Store max difference, default -1

        for x in nums:             # Loop through all elements
            if x <= xMin:
                xMin = x           # Update min if current x is smaller or equal
            else:
                maxD = max(maxD, x - xMin)  # Calculate difference with min seen so far

        return maxD
