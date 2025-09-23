class Solution(object):
    def maxOverlap(self, intervals):
        """
        :type intervals: nested list of ints
        :rtype: int
        """
        events = []
        for i in range(len(intervals)):
            start = (intervals[i][0], 1)
            end = (intervals[i][1], -1)
            event = [start, end]
            events += event
        
        sorted_events = sorted(events, key=lambda x: (x[0], -x[1]))
        max_overlap = 0
        curr_overlap = 0
        for i in range(len(sorted_events)):
            curr_overlap += sorted_events[i][1]
            if max_overlap < curr_overlap:
                max_overlap = curr_overlap
        
        
        return max_overlap
    
if __name__ == "__main__":
    test = Solution()
    test1 = [[1, 4], [2, 5], [7, 9], [3, 6]]
    assert(test.maxOverlap(test1) == 3)
