
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals

        result = []
        intervals = sorted(intervals)
        for i in range(1, len(intervals)):
            checkI = intervals[i-1]
            checkII = intervals[i]
            if checkI[1] < checkII[0]:
                result.append(checkI)
            else:
                intervals[i] = [checkI[0], max(checkI[1], checkII[1])]
            
        result.append(intervals[-1])
        return result


