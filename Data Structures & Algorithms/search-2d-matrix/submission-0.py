class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        index_row = None
        while l <= r:

            mid = l + ((r-l) // 2)
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                return True

        index_row = l + ((r - l) // 2)
        l, r = 0, len(matrix[index_row]) - 1

        while l <= r:

            mid = l + ((r - l) // 2)

            if matrix[index_row][mid] > target:
                r = mid - 1
            elif matrix[index_row][mid] < target:
                l = mid + 1
            else:
                return True

        return False