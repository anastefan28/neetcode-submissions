class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        for num in range(1000, -1001, -1):
            if k > freq[num]:
                k -= freq[num]
            else:
                return num 