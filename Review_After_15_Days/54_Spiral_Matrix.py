class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        checked = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dIndex = 0

        m = len(matrix)
        n = len(matrix[0])

        startM = 0
        startN = 0

        while len(result) < m * n:
            checked.append([startM, startN])
            result.append(matrix[startM][startN])
            newM = startM + directions[dIndex][0]
            newN = startN + directions[dIndex][1]
            if 0 <= newM < m and 0 <= newN < n and [newM, newN] not in checked:
                startM = newM
                startN = newN
            else:
                dIndex = (dIndex + 1) % 4
                startM += directions[dIndex][0]
                startN += directions[dIndex][1]
        return result
