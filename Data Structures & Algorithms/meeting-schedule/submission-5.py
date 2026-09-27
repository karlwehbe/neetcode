"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1:
            return True

        inter = []
        for i in intervals:
           inter.append((i.start, i.end))

        inter.sort()

        start = inter[0][0]
        end = inter[0][1]
        for i in range(1, len(inter)):
            meeting = inter[i]
            if meeting[0] >= start and meeting[0] < end:
                return False
            elif meeting[1] < end and meeting[1] >= start:
                return False
            else:
                start = meeting[0]
                end = meeting[1]

        return True
