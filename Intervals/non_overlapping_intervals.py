class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort() 
        overlap = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:

            if start >= prevEnd:
                prevEnd = end
            else:
                overlap += 1
                prevEnd = min(end, prevEnd)

        return overlap