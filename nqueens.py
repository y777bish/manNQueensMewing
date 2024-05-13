class Solution:

    def solveNQueens(self, n: int):
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]
        def backtrack(r):
            if r == n:
                copy = [ "".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "0"
        backtrack(0)
        return res, board





n = int(input("podaj n"))
solution = Solution()
result = solution.solveNQueens(n)
for solution in result:
    for row in solution:
        print(row)
    print()