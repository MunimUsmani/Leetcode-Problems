class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        sides = len(set(nums))
        if sides == 1:
            return "equilateral"
        if sides == 2:
            return "isosceles"
        else:
            return "scalene"
