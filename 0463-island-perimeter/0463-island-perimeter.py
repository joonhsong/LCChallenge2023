class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:     
                    p += 4
                    if i > 0:
                        p -= grid[i-1][j]
                    if i < len(grid)-1:
                        p -= grid[i+1][j]
                    if j > 0:
                        p -= grid[i][j-1]
                    if j < len(grid[0])-1:
                        p -= grid[i][j+1]

        return p