class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [math.inf for _ in range(len(nums))]
        ans, currHigh = 0, 0
        for i in range(len(nums)):
            low,high = 0, currHigh
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if dp[mid] >= nums[i]:
                    idx = mid
                    high = mid - 1
                else:
                    low = mid + 1
            if idx == -1: idx = currHigh + 1
            currHigh = max(idx, currHigh)
            dp[idx] = nums[i]
            ans = max(ans, idx + 1)
        return ans
