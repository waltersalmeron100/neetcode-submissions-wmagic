import numpy

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]

                if cell == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if cell in rows[r] or cell in cols[c] or cell in boxes[box_index]:
                    return False
                else:
                    rows[r].add(cell)
                    cols[c].add(cell)
                    boxes[int(box_index)].add(cell)
        return True

                


