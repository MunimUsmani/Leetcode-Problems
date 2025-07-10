from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n          # a ⊕ a = 0, 0 ⊕ b = b
        return xor
