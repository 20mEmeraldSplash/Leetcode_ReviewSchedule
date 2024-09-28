class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        h = len(matrix)
        w = len(matrix[0])
        result = []
        dir_list = [(0, 1), (1, 0), (0,-1), (-1, 0)]
        dir_index = 0
        checked = []

        i = 0
        j = 0
        while len(result) < h * w :

            result.append(matrix[i][j])
            checked.append((i,j))

            next_i = i + dir_list[dir_index][0]
            next_j = j + dir_list[dir_index][1]

            if 0 <= next_i < h and 0 <= next_j < w and (next_i, next_j) not in checked:
                i = next_i
                j = next_j
            else:
                dir_index = (dir_index + 1) % 4
                i += dir_list[dir_index][0]
                j += dir_list[dir_index][1]

        return result 