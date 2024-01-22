class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        r, c = 0, 0
        if startPos[0] < homePos[0]:
            r = sum(rowCosts[startPos[0]+1:homePos[0]+1])
        elif startPos[0] > homePos[0]:
            r = sum(rowCosts[homePos[0]:startPos[0]])
        if startPos[1] < homePos[1]:
            c = sum(colCosts[startPos[1]+1:homePos[1]+1])
        elif startPos[1] > homePos[1]:
            c = sum(colCosts[homePos[1]:startPos[1]])
        return r + c
        