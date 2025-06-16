class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        queens = [-1] * n
        used_columns = set()
        used_diagonals = set()
        used_antidiagonals = set()

        def backtrack(r: int):
            if r == n:
                board = []
                for row in range(n):
                    row_list = ["."] * n
                    col_q = queens[row]
                    row_list[col_q] = "Q"
                    board.append("".join(row_list))
                ans.append(board)
                return
            for c in range(n):
                diag = r - c
                anti = r + c
                if (
                    c in used_columns
                    or diag in used_diagonals
                    or anti in used_antidiagonals
                ):
                    continue
                queens[r] = c
                used_columns.add(c)
                used_diagonals.add(diag)
                used_antidiagonals.add(anti)
                backtrack(r + 1)
                used_columns.remove(c)
                used_diagonals.remove(diag)
                used_antidiagonals.remove(anti)

        backtrack(0)

        return ans
