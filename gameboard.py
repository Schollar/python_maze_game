
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
                " * "
            ],
            [
                # ROW 2
                " * ",
                "   ",
                " * ",
                " * ",
                " c ",
                " * "
            ],
            [
                # ROW 3
                " * ",
                "   ",
                "   ",
                "   ",
                " * ",
                " * "
            ],
            [
                # ROW 4
                " * ",
                " c ",
                " * ",
                "   ",
                "   ",
                " * "
            ],
            [
                # ROW 5
                " * ",
                " * ",
                " * ",
                " * ",
                "   ",
                " * "
            ],
            [
                # ROW 6
                " * ",
                " c ",
                "   ",
                "   ",
                "   ",
                " * "
            ],
            # ROW 7
            [" * ", " * ", " * ", " * ", " * ", " * "],
        ]

    def printBoard(self, playerRow, playerColumn, monsterRow, monsterColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print(" P ", end="")
                elif i == monsterRow and j == monsterColumn:
                    print(" M ", end="")
                else:
                    print(self.board[i][j], end="")

            print("")

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True
# Checking to see if user has landed on a coin, if so we change the index value to a space to take the coin away and return true

    def checkCoin(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("c") != -1:
            self.board[testRow][testColumn] = "   "
            print("You have found a coin!")
            return True
        return False

    def checkMonster(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("M") != -1:
            print("The Monster ate your coins!")
            return True
        return False
    # TODO
    # Return True if the player is in the winning column and row
    # Return False otherwise

    def checkWin(self, playerRow, playerColumn):
        if(playerRow == 0 and playerColumn == 2):
            return True
        else:
            return False
