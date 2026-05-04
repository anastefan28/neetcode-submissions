class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            current_time, node = heapq.heappop(heap)
            if current_time > dist[node]:
                continue

            for neighbor, travel_time in graph[node]:
                new_time = current_time + travel_time
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))
        answer = max(dist[1:])
        return answer if answer != float("inf") else -1      
