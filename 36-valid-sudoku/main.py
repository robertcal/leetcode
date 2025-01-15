class Solution:
    # solved this on my own
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            count = defaultdict(int)

            for j in range(9):
                target = board[i][j]
                if target != ".":
                    if count[target] != 0:
                        return False
                    count[target] = 1

        for i in range(9):
            count = defaultdict(int)

            for j in range(9):
                target = board[j][i]
                if target != ".":
                    if count[target] != 0:
                        return False
                    count[target] = 1

        def isValidBox(x, y):
            count = defaultdict(int)
            for i in range(x, x + 3, 1):
                for j in range(y, y + 3, 1):
                    target = board[i][j]
                    if target != ".":
                        if count[target] != 0:
                            return False
                        count[target] = 1

            return True

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                if not isValidBox(i, j):
                    return False

        return True