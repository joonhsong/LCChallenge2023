class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*101 for _ in range(101)] 
        def find(row, col):
            if row == 1 or col == 1:
                return 1
            if dp[row][col]:
                return dp[row][col]
            down = find(row-1, col)
            right = find(row, col-1)
            dp[row][col] = down + right
            return dp[row][col]
        ret = find(m, n)
        return ret
        
        