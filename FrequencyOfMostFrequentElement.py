class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        ans = 0
        left = 0
        sum = 0

        for right in range(len(nums)):
            target = nums[right]
            sum += target

            while (right - left + 1) * target - sum > k:
                sum -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans
