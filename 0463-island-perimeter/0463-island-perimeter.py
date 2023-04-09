class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        c = len(grid)
        r = len(grid[0])
        peri = 0
        
        for i in range(c):
            for j in range(r):
                if grid[i][j] == 0:
                    continue
                peri += 4
                if i > 0:
                    peri -= grid[i-1][j]
                if i < c-1:
                    peri -= grid[i+1][j]
                if j > 0:
                    peri -= grid[i][j-1]
                if j < r-1:
                    peri -= grid[i][j+1]

        return peri