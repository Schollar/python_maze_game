import gameboard
import player
import monster

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("If you would like to exit the game just type 'quit'")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
board = gameboard.GameBoard()
# Create a new Player called player starting at position 3,2
player = player.Player(6, 2)
monster = monster.Monster(1, 2)


while True:
    board.printBoard(player.rowPosition, player.columnPosition,
                     monster.rowPosition, monster.columnPosition)
    try:
        print('You have ',  player.coinCount, ' coins')
        selection = input("Make a move: ")
        selection = selection.lower()
        # Move the player through the board
        if(selection == 'w' and board.checkMove(player.rowPosition - 1, player.columnPosition) == True):
            player.moveUp()
        elif(selection == 'a' and board.checkMove(player.rowPosition, player.columnPosition - 1) == True):
            player.moveLeft()
        elif(selection == 's' and board.checkMove(player.rowPosition + 1, player.columnPosition) == True):
            player.moveDown()
        elif(selection == 'd' and board.checkMove(player.rowPosition, player.columnPosition + 1) == True):
            player.moveRight()
        elif(selection == 'quit'):
            print('You have quit the game!')
            exit()
        else:
            print('You must input a valid character! "w, a, s, d""')
        if(board.checkMonster(player.rowPosition, player.columnPosition) == True):
            player.coinCount = 0
        # Checking to see if the player lands on a coin after they have moved. If our checkcoin function returns true we add one to the players coin count
        elif(board.checkCoin(player.rowPosition, player.columnPosition) == True):
            player.coinCount = player.coinCount + 1
        # Check if the player has won, if so print a message and break the loop!
        elif(board.checkWin(player.rowPosition, player.columnPosition) == True):
            print('Congragulations you have won the game!')
            print('You collected a total of ', player.coinCount, ' Coins')
            exit()
    except KeyboardInterrupt:
        print('You have quit the game!')
        exit()
    except EOFError:
        print('I think you have a bad input. Try "w, a, s, d"')
