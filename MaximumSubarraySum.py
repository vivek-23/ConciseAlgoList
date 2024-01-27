class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        ss = 0
        for i in range(len(nums)):
            ss += nums[i]
            mx = max(mx, ss)
            ss = max(ss , 0)
        return mx
