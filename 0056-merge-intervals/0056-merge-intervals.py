class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return ret
        ret = []
        intervals.sort()
        temp = intervals[0]
        for i in intervals:
            if i[0] <= temp[1]:
                temp[1] = max(i[1], temp[1])
            else:
                ret.append(temp)
                temp = i
        ret.append(temp)
        return ret
        