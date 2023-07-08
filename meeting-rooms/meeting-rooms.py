class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        # print(intervals)
        previous_x = 0
        previous_y = 0
        for x, y in intervals:
            if previous_y <= x:
                previous_x = x
                previous_y = y
            else:
                return False
        return True