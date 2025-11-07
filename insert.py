class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            inserted.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        inserted.append(newInterval)

        while i < n:
            inserted.append(intervals[i])
            i += 1
        
        return inserted