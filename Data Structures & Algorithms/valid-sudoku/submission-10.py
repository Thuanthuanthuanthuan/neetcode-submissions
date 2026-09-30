class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #initalize variables 
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) 

        #skip empty spaces
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # check for dup
                value = board[r][c]
                if (value in rows[r] or
                    value in cols[c] or
                    value in squares[(r//3,c//3)]):
                    return False

                # else, add value to said variables
                cols[c].add(value)
                rows[r].add(value)
                squares[(r//3,c//3)].add(value)

        return True


        