class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        

        m = len(matrix)
        n = len(matrix[0])

        # m first
        l, r = 0, m - 1
        while l <= r:
            m = (l + r) // 2
            
            if matrix[m][0] == target:
                return True

            if target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        row = l - 1

        if l < 0:
            return False

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] == target:
                return True
            
            if target > matrix[row][m]:
                l = m + 1
            else:
                r = m - 1
        
        return False
            
        