class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum=0

        for i in range:
            if curSum < 0:
                curSum = 0
                maxSub = max(maxSub, curSum)
        return maxSub
