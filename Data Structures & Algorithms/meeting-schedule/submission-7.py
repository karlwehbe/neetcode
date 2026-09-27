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

        prev_meeting = inter[0]
        start = prev_meeting[0]
        end = prev_meeting[1]
        for i in range(1, len(inter)):
            curr_meeting = inter[i]
            if curr_meeting[0] >= start and curr_meeting[0] < end:
                return False
            elif curr_meeting[1] < end and curr_meeting[1] >= start:
                return False
            else:
                start = curr_meeting[0]
                end = curr_meeting[1]

        return True
