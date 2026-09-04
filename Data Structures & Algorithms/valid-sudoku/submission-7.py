class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # initalize sets
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # go thr board n check + skip empty space
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if (value == "."):
                    continue

                # if value is alr in set , return false
                if (value in rows[r] or
                    value in cols[c] or
                    value in squares[r // 3, c // 3]):
                    return False

                # if value not in set, add to set n return true

                rows[r].add(value)
                cols[c].add(value)
                squares[r//3, c//3].add(value)

        return True

                


        
        