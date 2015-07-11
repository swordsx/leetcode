# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if not intervals: return []
        intervals.sort(cmp = lambda a, b: a.start - b.start)

        result = []
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start <= cur.end:
                cur.end = max(cur.end, intervals[i].end)
            else:
                result.append(cur)
                cur = intervals[i]
        result.append(cur)
        return result
