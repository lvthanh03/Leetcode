class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for num in nums:
            if num > target:
                return False
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j-num]
            if dp[target]:
                return True
        return False