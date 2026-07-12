class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We previously ran binary search on just a single array (just columns)
        # Now we do it for both rows and columns (we start with rows and then columns)
        # First we find the row where the target could potentialy be present
        # Second, we search the row to see if actually present
        # Both using binary so we get O(log(m)) + O(log(n)) = O(log n * m)
        
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False

        row = (top + bot) // 2      
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        

