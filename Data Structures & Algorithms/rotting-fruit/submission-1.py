class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue and fresh > 0:
            level_size = len(queue)
            for _ in range(level_size):
                x,y = queue.popleft()
                for dx, dy in directions:
                    newx = x + dx
                    newy = y + dy
                    if newx >= 0 and newy >= 0 and newx < n and newy < m and grid[newx][newy] == 1:
                        fresh -= 1
                        grid[newx][newy] = 2
                        queue.append((newx, newy))
            minutes += 1
      
        return minutes if fresh == 0 else -1