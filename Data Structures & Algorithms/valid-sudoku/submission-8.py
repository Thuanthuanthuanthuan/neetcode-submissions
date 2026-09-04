class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check: 1, check empty space n skip; check to see for each r, c, s ; 

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue


                if (val in rows[r] or 
                    val in cols[c] or
                    val in squares[r//3, c//3]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[r//3, c//3].add(val)

        return True
        
        