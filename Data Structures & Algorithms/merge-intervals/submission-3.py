class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()

        merged_list = [] 
        l, r = 0, 1
        curr_start, curr_end = intervals[l]
        
        while r < len(intervals):
            next_start, next_end = intervals[r]
            if curr_end >= next_start and curr_end <= next_end:
                curr_end = next_end
            elif curr_end < next_start:
                merged_list.append([curr_start, curr_end])
                curr_start = next_start
                curr_end = next_end
                l = r
    
            r += 1

            if r == len(intervals):
                if len(merged_list) == 0:
                    merged_list.append([curr_start, curr_end])
                elif merged_list[-1][1] < curr_start:
                    merged_list.append([curr_start, curr_end])
            
        return merged_list



        # [[1,3],[1,5],[6,7]]
        # [1,5]
        l = 0
        r = 2

        curr_start = 6
        curr_end = 7

        next_start = 6
        next_end = 7

        merged_list = [[1,5]]
        # [1,5][6,7]

    
        

