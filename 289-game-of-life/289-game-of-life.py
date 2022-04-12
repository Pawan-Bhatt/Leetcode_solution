class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
                # all new 0's denotes as -1, (1 ==> 0)
        ROWS, COLS = len(board), len(board[0])
        def countneg(r,c):
            neig = 0
            #starting from left top corner
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c+ 2):
                    #position out of bounds
                    if ((i == r and j == c) or i < 0 or j < 0  or i == ROWS or j == COLS):
                        continue
                    if board[i][j] in [1,3]:
                        #count the original neighb
                        neig += 1
            return neig
        for r in range(ROWS):
               for c in range(COLS):
                    neig = countneg(r,c)
                    if board[r][c]:
                        if neig in [2,3]:
                            board[r][c] = 3

                    elif neig == 3:
                            board[r][c] = 2
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2,3]:
                    board[r][c] = 1