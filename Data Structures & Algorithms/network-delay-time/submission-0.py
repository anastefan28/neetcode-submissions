class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        heap = [(0, k)]
        shortest = {}
        while heap:
            current_time, node = heapq.heappop(heap)
            if node in shortest:
                continue
            shortest[node] = current_time
            for neighbor, travel_time in graph[node]:
                if neighbor not in shortest:
                    new_time = current_time + travel_time
                    heapq.heappush(heap, (new_time, neighbor))
        if len(shortest) != n:
            return -1
        return max(shortest.values())        
