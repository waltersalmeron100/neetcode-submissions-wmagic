class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

# rows = 3 cols = 4
# left = 0 right = 11

# mid = 5
# r = 1
# c = 1

# matrix[1][1] = 11
# right = 4

# mid = 2
# r = 0
# c = 2

# matrix[0][2] = 4
# left =  3

# mid = 3
# r = 0 
# c = 3

# matrix[0][3] = 8
# left = 4

# mid = 4
# r = 1
# c = 0

# matrix[r][c] = 10