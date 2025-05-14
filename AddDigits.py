class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            val = 0
            while num > 0:
                val += num % 10
                num = num // 10
            num = val
        return num 
