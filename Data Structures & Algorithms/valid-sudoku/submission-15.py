class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        digits_store_row = set()
        for row in board:
            digits_store_row.clear()
            for i in range(len(row)):
                if row[i] != ".":
                    if row[i] not in digits_store_row:
                        digits_store_row.add(row[i])
                    else:
                        return False
        
        # check columns
        digits_store_col =  set()
        for i in range(len(row)):
            digits_store_col.clear()
            for row in board:
                if row[i] != ".":
                    if row[i] not in digits_store_col:
                        digits_store_col.add(row[i])
                    else:
                        return False
        
        # check 3x3 sub-boxes
        sub_boxes = [[],[],[],[],[],[],[],[],[]]
        box = 0
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for col in range(0+j, 3+j):
                    for row in range(0+i,3+i):
                        if board[row][col] != ".":
                            if board[row][col] not in sub_boxes[box]:
                                sub_boxes[box].append(board[row][col])
                            else:
                                return False
                if box not in [2,5]:
                    box += 1
            box += 1
        
        return True
