class Solution:
    def climbStairs(self, n: int) -> int:
        return int(pow(((a:=sqrt(5))+1)/2, n+1)/a+0.5)
