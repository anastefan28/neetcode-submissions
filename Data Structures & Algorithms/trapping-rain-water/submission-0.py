class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                left_boundary = stack[-1]
                right_boundary = i
                width = right_boundary - left_boundary - 1
                bounded_height = min(height[left_boundary], height[right_boundary]) -  height[bottom]
                water += width * bounded_height
            stack.append(i)
        return water