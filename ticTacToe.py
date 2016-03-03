
def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-----')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    
    return ((board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) # down left
	(board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) #down middle
	(board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) # down right
	(board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) # across top
	(board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) # across middle
	(board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) # across the bottom
	(board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player)
	(board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))
    
    
    
def startGame(startingPlayer, board):

    turn = startingPlayer
    for i in range(9):
        printBoard(board) # prints the board
        print('Turn for ' + turn + '. Move on which space?')
        move = input() # prompts user for their turn
        board[move] = turn # applies players input to the correspondig space on the board
        if( checkWinner(board, 'X') ): # running through checkWinner to see if player X has won
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ): # checking if player 0 has won
            print('O wins!')
            break
    
        if turn == 'X': # this assigns the other player X or 0 depending what what is chosen first
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board) # prints the updated board
    