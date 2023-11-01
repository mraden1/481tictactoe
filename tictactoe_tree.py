# Mark Raden
# CWID: 886286863
# CPSC-481
# Tic-Tac-Toe AI
# Part of group with Aniket and Ashish

def PlayTicTacToe(board, player): #Computer side plays. Computer is always 'O' for  this program
    nextPlay = CheckForTwo(board, 'X')
    if CheckForWin(board):
        return print('game finished')
        
    elif CheckForTie(board):
        return print('Game is a tie')
        
    elif ((nextPlay < 9) and (board[nextPlay] == '-')): #finds open strategic spot
        print('AI\'s turn')
        board[nextPlay] = player
        PrintBoard(board)
        return HumanPlayer(board, 'X')
    else:
        for i in range(len(board)): #takes any spot if a strategic one isnt required
            if board[i] == '-': 
                print('AI\'s turn')
                board[i] = player
                PrintBoard(board)
                return HumanPlayer(board, 'X')

def CheckForTwo(board, player): #checks for opponent about to get 3 in a row
    i = [1, 2, 0]
    j = [2, 0, 1]
    l = [3, 6]
    for k in range(2):
        if ((board[i[k]] == board[j[k]]) and (board[i[k]] == player)):
            return k
        else:
            for each in l:
                if ((board[i[k] + each] == board[j[k] + each]) and (board[i[k] + each] == player)):
                    return k + each
    
    if ((board[0] == board[4]) and (board[0] == player)):
        return 8
    elif ((board[2] == board[4]) and (board[2] == player)):
        return 6
    elif ((board[4] == board[6]) and (board[4] == player)):
        return 2
    elif ((board[4] == board[8]) and (board[4] == player)):
        return 0
    elif (((board[0] == board[8]) and (board[0] == player)) or
        ((board[2] == board[6]) and (board[2] == player))):
        return 4
    else:
        return 9

def HumanPlayer(board, player): # Allows human player to make a move
    if CheckForWin(board):
        print('game finished')
        return
    elif CheckForTie(board):
        print('Game is a tie')
        return
    try:
        i = abs(1-int(input('Your turn! press numbers 1-9 to select a cell: ')))
        if ((board[i] == '-') and (i < 10) and (i > 0)):
            board[i] = player
            PrintBoard(board)
            return PlayTicTacToe(board, 'O')
        else:
            print('that spot is unavailable')
            return HumanPlayer(board, player)
    except:
        print('invalid input, try again')
        return HumanPLayer(board, player)

def CheckForTie(board): #checks the board for a tie game
    for each in board:
        if each == '-':
            return False
    return True

def HorizontalWin(board): #checks for a horizontal win
    if ((board[0] != '-' and board[0] == board[1] == board[2]) or
        (board[3] != '-' and board[3] == board[4] == board[5]) or
        (board[6] != '-' and board[6] == board[7] == board[8])):
        print('Horizontal Win')
        return True
    else:
        return False

def VerticalWin(board): #checks for a vertical win
    if ((board[0] != '-' and board[0] == board[3] == board[6]) or
        (board[1] != '-' and board[1] == board[4] == board[7]) or
        (board[2] != '-' and board[2] == board[5] == board[8])):
        print('Vertical win')
        return True
    else:
        return False

def CrossWin(board): #checks for a cross win
    if ((board[0] != '-' and board[0] == board[4] == board[8]) or
        (board[6] != '-' and board[6] == board[4] == board[2])):
        print('Cross win')
        return True
    else:
        return False

def CheckForWin(board): #uses the 3 win checks to decide whether a win has occurred
    if HorizontalWin(board) or VerticalWin(board) or CrossWin(board):
        return True
    else:
        return False

def PrintBoard(board): #prints the tic-tac-toe board in a readable fashion
    index = 0
    while index < 7:
        print('|' + str(board[index]) +
              '|' + str(board[index+1]) +
              '|' + str(board[index+2] +
              '|'))
        index += 3

board = ['-']*9
PlayTicTacToe(board, 'O') #start the game
