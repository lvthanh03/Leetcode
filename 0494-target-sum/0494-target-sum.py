class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target) > s:
            return 0
        if (s + target) % 2 == 1:
            return 0
        target = (s + target) // 2
        dp = [1] + [0] * target
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] += dp[i-num]
        return dp[target]