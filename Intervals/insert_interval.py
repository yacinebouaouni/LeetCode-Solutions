class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        if newInterval[1]<intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        
        if newInterval[0]>intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        output = []
        
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1


        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        output.append(newInterval)
        
        while i<len(intervals):
            output.append(intervals[i])
            i+=1

        return output
        