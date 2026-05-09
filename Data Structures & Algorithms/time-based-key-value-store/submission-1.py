class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append((value, timestamp)) 
    def binary_search(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][1] > target:
                right = mid - 1
            else:
                if mid == right or arr[mid + 1][1] > target:
                    return arr[mid][0]
                else: 
                    left = mid + 1
        return ""
    def get(self, key: str, timestamp: int) -> str:
        arr = self.timemap.get(key)
        if not arr:
            return ""
        else:
            return self.binary_search(arr, timestamp)


