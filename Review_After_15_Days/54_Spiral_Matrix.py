class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        checked = []
        m = len(matrix)
        n = len(matrix[0])
        start_m = 0
        start_n = 0

        dect_list = [(0, 1), (1,0), (0,-1),(-1,0)]

        dect_index = 0

        while len(result) < m * n:
            if (start_m, start_n) not in checked:
                result.append(matrix[start_m][start_n])
                checked.append((start_m, start_n))
                new_m = start_m + dect_list[dect_index][0]
                new_n = start_n + dect_list[dect_index][1]
                if 0<=new_m<m and 0<=new_n<n and (new_m, new_n) not in checked:
                    start_m = new_m
                    start_n = new_n
                else:
                    dect_index = (dect_index + 1) % 4
                    start_m = start_m + dect_list[dect_index][0]
                    start_n = start_n + dect_list[dect_index][1]
        return result

