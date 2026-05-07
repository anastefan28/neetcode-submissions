class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        in_mst = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        total_cost = 0
        for _ in range(n):
            u = -1
            best = float('inf')
            for v in range(n):
                if not in_mst[v] and min_dist[v] < best:
                    u, best = v, min_dist[v]
            in_mst[u] = True
            total_cost += min_dist[u]

            for v in range(n):
                if not in_mst[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    min_dist[v] = min(d, min_dist[v])
        return int(total_cost)