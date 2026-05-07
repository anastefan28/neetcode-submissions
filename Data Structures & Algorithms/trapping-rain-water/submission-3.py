class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:
            # Left side is the limiting side
            if height[left] < height[right]:
                # Current bar becomes a new left wall
                if height[left] >= left_max:
                    left_max = height[left]
                # Current bar is below left wall, so it traps water
                else:
                    water += left_max - height[left]

                left += 1

            # Right side is the limiting side
            else:
                # Current bar becomes a new right wall
                if height[right] >= right_max:
                    right_max = height[right]
                # Current bar is below right wall, so it traps water
                else:
                    water += right_max - height[right]

                right -= 1

        return water