class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        for i in range(n):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        while k:
            pile = -heappop(piles)
            pile -= floor(pile / 2)
            heappush(piles, -pile)
            k -= 1
        return -sum(piles)