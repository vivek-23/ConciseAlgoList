class Solution:
    def LCSof3(self, A, B, C, n1, n2, n3):
        dp = [[[0 for _ in range(n3 + 1)] for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(n1):
            for j in range(n2):
                for k in range(n3):
                    if A[i] == B[j] and B[j] == C[k]:
                        dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1
                    else:
                        dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j + 1][k], dp[i][j + 1][k + 1], dp[i + 1][j][k + 1])
        return dp[n1][n2][n3]
