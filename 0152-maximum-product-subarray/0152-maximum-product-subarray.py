class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        min_prod = 1
        max_prod = 1
        for value in nums:
            old_min, old_max = min_prod, max_prod
            min_prod = min(value, value * old_min, value * old_max)
            max_prod = max(value, value * old_min, value * old_max)
            ans = max(ans, max_prod)
        return ans