class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = (dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0) + 1
                else:
                    dp[i][j] = max(dp[i - 1][j] if i - 1 >= 0 else 0, dp[i][j - 1] if j - 1 >= 0 else 0)
        return dp[len(text1) - 1][len(text2) - 1]
