class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R <= 2 or C <= 2:
            return

        for r in range(R):
            self.dfs(board, r, 0, R, C)
            self.dfs(board, r, C - 1, R, C)

        for c in range(C):
            self.dfs(board, 0, c, R, C)
            self.dfs(board, R - 1, c, R, C)

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"

    def dfs(self, board, r, c, R, C):
        if 0 <= r < R and 0 <= c < C and board[r][c] == "O":
            board[r][c] = "N"
            self.dfs(board, r, c + 1, R, C)
            self.dfs(board, r, c - 1, R, C)
            self.dfs(board, r - 1, c, R, C)
            self.dfs(board, r + 1, c, R, C)
