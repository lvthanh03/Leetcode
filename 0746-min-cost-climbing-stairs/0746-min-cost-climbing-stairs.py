class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        dp = [0] * (n + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        return dp[-1]
            
            
            