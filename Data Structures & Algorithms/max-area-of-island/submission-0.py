class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(row, column):
            if row < 0 or row >= n or column < 0 or column >= m or grid[row][column] != 1:
                return 0
            
            grid[row][column] = -1
            return 1 + dfs(row + 1, column) + dfs(row - 1, column) + dfs(row, column + 1) + dfs(row, column - 1)
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    result = max(result, dfs(i, j))
        return result
        