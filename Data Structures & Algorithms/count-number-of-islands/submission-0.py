class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(row, column):
            if row < 0 or row >= n or column < 0 or column >= m:
                return
            if grid[row][column] == "1":
                grid[row][column] = "-1"
                dfs(row + 1, column)
                dfs(row - 1, column)
                dfs(row, column + 1)
                dfs(row, column - 1)
        
        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands