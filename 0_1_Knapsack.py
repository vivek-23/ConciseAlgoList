class Solution:
    def knapSack(self,W, wt, val, n):
        dp = [[0 for _ in range(W + 1)] for _ in range(len(wt))]
        maxx = 0
        if wt[0] <= W:
            dp[0][wt[0]] = val[0]
            maxx = val[0]
        for i in range(1, len(wt)):
            for j in range(W + 1):
                dp[i][j] = dp[i - 1][j]
                if j == wt[i] or j > wt[i] and dp[i - 1][j - wt[i]] > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - wt[i]] + val[i])
                maxx = max(maxx, dp[i][j])
        return maxx
