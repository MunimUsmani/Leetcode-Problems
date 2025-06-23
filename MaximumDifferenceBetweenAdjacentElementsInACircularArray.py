class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_so_far = abs(nums[0] - nums[n - 1])  # circular comparison

        for i in range(n - 1):
            current_diff = abs(nums[i] - nums[i + 1])
            max_so_far = max(max_so_far, current_diff)

        return max_so_far
