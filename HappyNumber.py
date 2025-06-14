class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
 
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sum_of_squares(n)
        return n == 1

    def sum_of_squares(self, n):
        total = 0
        while n:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total
