class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i, (curStart, curEnd) in enumerate(intervals):

            # new intervals will appear after this
            if curEnd < newInterval[0]:
                res.append([curStart, curEnd])
            
            # new intervals appear right before this intervals
            elif curStart > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            # require merging (not appear after cur, overlapping before)
            else:
                newInterval = [min(curStart, newInterval[0]), max(curEnd, newInterval[1])]
        res.append(newInterval)
        return res

