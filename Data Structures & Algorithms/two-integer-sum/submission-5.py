class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = {}
        for index, num in enumerate(nums):
            if target - num in numset:
                return [numset[target - num], index]
            numset[num] = index