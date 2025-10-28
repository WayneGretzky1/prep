class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        blocks = {i: set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                block_index = (i // 3) * 3 + (j // 3)

                if val in rows[i] or val in cols[j] or val in blocks[block_index]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                blocks[block_index].add(val)

        return True