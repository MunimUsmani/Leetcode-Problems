class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        total = sum(range(length+1))
        return total - sum(nums)
