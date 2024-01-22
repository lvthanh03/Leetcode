class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLen = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    maxLen[i] = max(maxLen[i], maxLen[j] + 1)
        return max(maxLen)