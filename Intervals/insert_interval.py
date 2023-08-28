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
        start, end = newInterval
        startInterval = endInterval = None
        i = 0
        while i < len(intervals):
            if intervals[i][1] < start:
                output.append(intervals[i])
                i += 1

            elif intervals[i][1] > start and intervals[i][0] > start:
                startInterval = start
                break

            elif intervals[i][1] >= start >= intervals[i][0]:
                startInterval = intervals[i][0]
                break


        while i < len(intervals):
            if end > intervals[i][1] and i < len(intervals)-1:
                i += 1

            elif end > intervals[i][1] and i == len(intervals)-1:
                endInterval = end
                i += 1
                break

            
            elif intervals[i][0] <= end <= intervals[i][1]:
                endInterval = intervals[i][1]
                i += 1
                break
            else:
                endInterval = end
                break

        output.append([startInterval, endInterval])

        while i<len(intervals):
            output.append(intervals[i])
            i+=1

        return output
        