class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)

        start = 0

        while start < n and intervals[start][1] < newInterval[0]:
            result.append(intervals[start])
            start += 1

        while start < n and intervals[start][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[start][0])
            newInterval[1] = max(newInterval[1], intervals[start][1])
            start += 1

        result.append(newInterval)

        while start < n:
            result.append(intervals[start])
            start += 1

        return result