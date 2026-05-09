class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] += 1000
        freq = Counter(nums)
        for num in range(2001, -1, -1):
            if k > freq[num]:
                k -= freq[num]
            else:
                return num - 1000