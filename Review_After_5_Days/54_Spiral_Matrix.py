class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        height = len(matrix)
        width = len(matrix[0])
        result = []
        checked_index = set()
        need_check = []

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        direction_index = 0

        i,j = 0,0
        while len(result) < height * width:
            result.append(matrix[i][j])
            checked_index.add((i,j))

            next_i = i + directions[direction_index][0]
            next_j = j + directions[direction_index][1]

            if 0 <= next_i < height and 0 <=next_j < width and (next_i, next_j)not in checked_index:
                i,j = next_i, next_j
            else:
                direction_index = (direction_index + 1) %4
                i += directions[direction_index][0]
                j += directions[direction_index][1]
        
        return result

