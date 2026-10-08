"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        sorted_intervals = sorted(intervals, key=lambda l:l.start)

        prevEnd = intervals[0].end

        for interval in sorted_intervals[1:]:
            if prevEnd > interval.start:
                return False
            prevEnd = interval.end
        return True