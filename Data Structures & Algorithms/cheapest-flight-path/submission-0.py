class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        prices = [INF] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices.copy()
            for from_city, to_city, price in flights:
                if prices[from_city] == INF:
                    continue
                new_price = prices[from_city] + price
                if new_price < temp[to_city]:
                    temp[to_city] = new_price
            prices = temp
        return -1 if prices[dst] == INF else prices[dst]
