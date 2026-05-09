class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        pairs.sort(reverse=True)
        fleets = 0
        slowest_time_ahead = 0
        for pos, spd in pairs:
            time = (target - pos) / spd
            if time > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time
        return fleets
        