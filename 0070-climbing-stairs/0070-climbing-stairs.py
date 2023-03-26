class Solution:
    def climbStairs(self, n: int) -> int:
        x = 0
        y = 1
        for i in range(1, n+1):
            x, y = y, x+y
        return y
        