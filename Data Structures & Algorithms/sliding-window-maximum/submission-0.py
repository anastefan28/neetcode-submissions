class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []
        for right in range(len(nums)):
            while q and nums[q[-1]] <= nums[right]:
                q.pop()
            q.append(right)
            left = right - k + 1
            if q[0] < left:
                q.popleft()
            if left >= 0:
                result.append(nums[q[0]])
        return result

            
