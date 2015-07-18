# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        if newInterval.end < intervals[0].start: return [newInterval] + intervals
        if newInterval.start > intervals[-1].end: return intervals + [newInterval]
        
        low, high = 0, len(intervals)
        while low < high:
            mid = (low + high) / 2
            if mid == -1: high = -1; break
            if intervals[mid].end < newInterval.start: low = mid + 1
            else: high = mid
        i = high

        low, high = 0, len(intervals)
        while low < high:
            mid = (low + high + 1) / 2
            if mid == len(intervals): low = len(intervals); break
            if intervals[mid].start > newInterval.end: high = mid - 1
            else: low = mid
        j = low
        if i <= j:
            i, j = max(i, 0), min(j, len(intervals) - 1)
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[j].end)
        return intervals[:i] + [newInterval] + intervals[j + 1:]
