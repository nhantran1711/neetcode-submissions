class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0

        prevEnd = intervals[0][1]

        for s, e in intervals[1:]:
            if prevEnd > s:
                res += 1
                prevEnd = min(prevEnd, e)
            else:
                prevEnd = e
        return res