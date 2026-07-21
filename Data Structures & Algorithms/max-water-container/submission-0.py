class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWidth = len(heights)
        bestArea = 0
        for p1 in range(0, maxWidth):
            p2 = p1 + 1
            while p2 < maxWidth:
                if heights[p2] > heights[p1]:
                    lowestHeight = heights[p1]
                else:
                    lowestHeight = heights[p2]
                currentArea = lowestHeight * (p2 - p1)
                if bestArea < currentArea:
                    bestArea = currentArea
                p2 += 1
        return bestArea

            

        