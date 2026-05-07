class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxfreq = max(freq.values())
        count = 0
        for (key, value) in freq.items():
            if value == maxfreq:
                count += 1
        intervals = (maxfreq - 1) * (n + 1) + count
        return max(intervals, len(tasks))