class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        height = len(matrix)
        width = len(matrix[0])
        checked = set()
        result = []

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        direction_index = 0

        i = 0
        j = 0

        while len(result) < height * width :
            checked.add((i,j))
            result.append(matrix[i][j])
            next_i = i + directions[direction_index][0]
            next_j = j + directions[direction_index][1]

            if 0 <= next_i <height and 0<=next_j<width and (next_i, next_j)not in checked:
                i, j = next_i, next_j
            else:
                direction_index = (direction_index + 1 )%4
                i += directions[direction_index][0]
                j += directions[direction_index][1]

        return result


