class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()
        prevEnd = points[0][1]
        count = 1

        for start, end in points[1:]:
            if start <= prevEnd:
                prevEnd = min(end, prevEnd)
            else:
                count += 1
                prevEnd = end

        return count