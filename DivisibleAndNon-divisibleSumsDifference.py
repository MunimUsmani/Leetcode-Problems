class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # defining two nums
        num1 = 0
        num2 = 0
        
        # nums range to n
        for i in range(1, n+1):
            # fall conditions
            if i % m == 0: # != 
                num2 += i
            else:
                num1 += i
        return num1 - num2

        # time: O(n)
        # Space: O(1)
