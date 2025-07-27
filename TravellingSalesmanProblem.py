import math

class Solution:
    def tsp(self, cost):
        n = len(cost)
        totalStates = 1 << n

        dp = [[math.inf] * n for _ in range(totalStates)]
        dp[1][0] = 0  # Starting from city 0

        for mask in range(totalStates):
            for u in range(n):
                if not (mask & (1 << u)):
                    continue
                for v in range(n):
                    if not (mask & (1 << v)):
                        next_mask = mask | (1 << v)
                        dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + cost[u][v])

        lastState = (1 << n) - 1
        ans = math.inf
        for i in range(n):
            ans = min(ans, dp[lastState][i] + cost[i][0])  # returning to starting city

        return ans
