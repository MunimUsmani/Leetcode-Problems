class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        res = []
        nums.sort()  #Step 1: Sorting

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: 
                continue  #Step 2: Skip duplicates

            l, r = i + 1, len(nums) - 1  #Step 3: Two-pointer approach
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1  # Step 4: Move right pointer left
                elif threeSum < 0:
                    l += 1  # Step 5: Move left pointer right
                else:
                    res.append([a, nums[l], nums[r]])  #Step 6: Add triplet to result
                    l += 1
                    
                    while l < r and nums[l] == nums[l - 1]:  #Step 7: Skip duplicates
                        l += 1

        return res  # Step 8: Return result
