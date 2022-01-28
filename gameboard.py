
class GameBoard:
    # Gameboard initilization
    def __init__(self):
        self.winningRow = 0
        self.winningColumn = 2
        self.board = [
            # ROW 0
            [" * ", " * ", "   ", " * ", " * ", " * "],
            [
                # ROW 1
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [
                # ROW 2
                " * ",
                "   ",
                " * ",
                " * ",
                "   ",
                " * ",
            ],
            [
                # ROW 3
                " * ",
                "   ",
                "   ",
                "   ",
                " * ",
                " * ",
            ],
            [
                # ROW 4
                " * ",
                "   ",
                " * ",
                "   ",
                "   ",
                " * ",
            ],
            [
                # ROW 5
                " * ",
                " * ",
                " * ",
                " * ",
                "   ",
                " * ",
            ],
            [
                # ROW 6
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            # ROW 7
            [" * ", " * ", " * ", " * ", " * ", " * "],
        ]

    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print(" P ", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    # TODO
    # Return True if the player is in the winning column and row
    # Return False otherwise
    def checkWin(self, playerRow, playerColumn):
        if(playerRow == 0 and playerColumn == 2):
            return True
        else:
            return False
