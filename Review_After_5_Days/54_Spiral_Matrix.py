class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        h = len(matrix)
        w = len(matrix[0])
        result = []
        directions = [(0, 1), (1,0),(0, -1), (-1,0)]
        index = 0
        i, j = 0, 0
        checked_list = [[False] * w for _ in range(h)]

        while len(result) < h * w :
            checked_list[i][j] = True
            result.append(matrix[i][j])
            next_i = i + directions[index][0]
            next_j = j + directions[index][1]
            if (0 <= next_i < h and 0 <= next_j < w and not checked_list[next_i][next_j]):
                i, j = next_i, next_j
            else:
                index = (index+1)%4
                i += directions[index][0]
                j += directions[index][1]
            
        return result