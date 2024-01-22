class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        score = 0
        while k:
            num = heapq.heappop(nums)
            score += (-num)
            heapq.heappush(nums, -ceil((-num) / 3))
            k -= 1
        return score