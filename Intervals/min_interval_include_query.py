class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        q = sorted([q,i] for i, q in enumerate(queries))
        intervals.sort(key = lambda x: x[1]-x[0])

        output = [-1] * len(queries)

        for start, end in intervals:
            ind = bisect.bisect(q, [start])
            while ind < len(q) and q[ind][0]<=end:
                output[q.pop(ind)[1]] = end-start+1

        return output
