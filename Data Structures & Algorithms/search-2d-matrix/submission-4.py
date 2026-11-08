class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def access(val):
            row = val//n
            col = val%n
            return matrix[int(row)][int(col)]
        

        low = 0
        mid = m*n//2
        upp = m*n - 1

        while low <= upp:
            if access(mid) == target:
                return True
            if access(mid) > target:
                upp = mid - 1
            else:
                low = mid + 1
            
            mid = (low + upp) // 2

        return False