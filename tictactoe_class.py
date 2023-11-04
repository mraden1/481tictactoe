# Mark Raden
# CWID: 886286863
# CPSC-481
# Tic-Tac-Toe AI
# Part of group with Aniket and Ashish

import tkinter as tk
from tkinter import messagebox


class TicTacToe: #tic tac toe close. Make an instance of this class to start and play a game
    def __init__(self):
        #initializes a backend board to keep track of the game on the model side
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        #creates a human player
        self.human = ''
        #creates a computer player
        self.computer = ''
        #keeps track of human points/plays same for computer
        self.humanPoints = 0
        self.computerPoints = 0
        #initializes a button object
        self.button = None
        #initializes a tk object
        self.root = None
        #runs the game
        self.Run()

    def Run(self):#starts the game
        
        #sets the root as a tk object
        self.root = tk.Tk()
        #creates the buttons and adds them to the tk object
        self.CreateBoard()
        #lets the human player choose X or O
        self.SetPlayers()
        #triggers the computer to play first
        self.root.bind(self.PlayTicTacToe())
        #keeps the tk object running for the duration of the game
        self.root.mainloop()


    def CreateBoard(self):#creates the buttons and adds them to the board
        for i in range(3):#creates rows
            for j in range(3):#creates columns
                self.button = tk.Button(
                                        self.root,
                                        text='-',
                                        font=('Arial', 50),
                                        height=1,
                                        width=3,
                                        command=lambda #attaches HandleClick and passes values
                                        row=i, 
                                        col=j:
                                        self.HandleClick(row, col)
                                        )
                self.button.grid(row=i, column=j, sticky="nsew")

    def HandleClick(self, row, col):#Handles the players clicking
        self.board[row][col] = self.human #alters the backend board to keep track of the game
        self.button = self.root.grid_slaves(row=row, column=col)[0]
        self.button.config(text=self.human, command=None)#changes button text to players character
        self.humanPoints += 1 #increases the humans points or plays
        self.PlayTicTacToe() #runs the AI after the human turn is over

    def SetPlayers(self): #Lets the human player choose their symbol
        answer = messagebox.askquestion('Pick Player', 'Would you like to play as X? ')
        if answer == 'yes':
            self.human = 'X'
            self.computer = 'O'
        else:
            self.human = 'O'
            self.computer = 'X'

    def PlayTicTacToe(self): #Computer side plays
        if self.GameFinished():#checks for a win
            return self.root.quit()
        else:
            nextPlay = list() #calculates a strategic next play
            nextPlay = self.CheckForTwo()
        if (len(nextPlay) > 0): #if there is a win or a block the computer will take it
            row = nextPlay.pop(0)
            col = nextPlay.pop(0)
            print('AI\'s turn')
            self.computerPoints += 1 #increments the computers plays/points
            self.board[row][col] = self.computer #updates the backend board
            self.button = self.root.grid_slaves(row=row, column=col)[0]
            self.button.config(text=self.board[row][col], command=None) #changes button text to computers symbol
            if self.GameFinished(): #checks for win
                return
            return
        for i in range(3): #if no blocks or wins available then standard play is chosen
            find = False #breaks loop later
            for j in range(3):
                if self.board[i][j] == '-': 
                    print('AI\'s turn')
                    self.computerPoints += 1 #adds points/plays to computer
                    self.board[i][j] = self.computer #updates backend board
                    self.button = self.root.grid_slaves(row=i, column=j)[0]
                    self.button.config(text=self.board[i][j], command=None) #changes button symbol
                    find = True
                    break
            if find:
                break
        if self.GameFinished(): #checks for win again
            return

    def CheckForTwo(self): #checks for 2 in a row that could result in win or block
        tempList = []
        for i in range(3): #3 layers of confusing stuff that checks for 2 in a row
            for j in range(3):
                for k in range(3):
                    if (i != j) and (i != k) and (j != k) and (self.board[i][i] != '-'):#diagonal
                        if self.board[i][i] == self.board[j][j]:
                            
                            if self.board[k][k] == '-':
                                for each in [k, k]:
                                    tempList.append(each)
                                return tempList

                        elif self.board[i][i] == self.board[k][k]: #diagonal
                            
                            if self.board[j][j] == '-':
                                for each in [j, j]:
                                    tempList.append(each)
                                return tempList
                            
                        elif (self.board[j][j] == self.board[k][k]) and (self.board[j][j] != '-'): #diagonal
                            
                            if self.board[i][i] == '-':
                                for each in [i, i]:
                                    tempList.append(each)
                                return tempList
                            
                    elif (i != j) and (self.board[k][i] != '-'): #rows
                        if self.board[k][i] == self.board[k][j]:

                            if self.board[k][(3-(i+j))] == '-':
                                for each in [k, (3-(i+j))]:
                                    tempList.append(each)
                                return tempList
                            
                    elif (i != j) and (self.board[i][k] != '-'): #columns
                        if self.board[i][k] == self.board[j][k]:
                            
                            if self.board[(3-(i+j))][k] == '-':
                                for each in [(3-(i+j)), k]:
                                    tempList.append(each)
                                return tempList

        if (self.board[1][1] != '-') and (self.board[0][2] == self.board[1][1]): #other overly complicated diagonal
            
            if self.board[2][0] == '-':
                for each in [2, 0]:
                    tempList.append(each)
                return tempList

        elif (self.board[1][1] != '-') and (self.board[2][0] == self.board[1][1]): #other overly complicated diagonal
            
            if self.board[0][2] == '-':
                for each in [0, 2]:
                    tempList.append(each)
                return tempList

        if (self.board[2][0] != '-') and (self.board[0][2] == self.board[2][0]): #other overly complicated diagonal
            
            if self.board[1][1] == '-':
                for each in [1, 1]:
                    tempList.append(each)
                return tempList

        return tempList

    def CheckForTie(self): #checks the self.board for a tie game
        for i in self.board:
            for each in i:
                if each == '-':
                    return False
        return True

    def HorizontalWin(self): #checks for a horizontal win
        if ((self.board[0][0] != '-' and self.board[0][0] == self.board[0][1] == self.board[0][2]) or
            (self.board[1][0] != '-' and self.board[1][0] == self.board[1][1] == self.board[1][2]) or
            (self.board[2][0] != '-' and self.board[2][0] == self.board[2][1] == self.board[2][2])):
            print('Horizontal Win')
            return True
        else:
            return False

    def VerticalWin(self): #checks for a vertical win
        if ((self.board[0][0] != '-' and self.board[0][0] == self.board[1][0] == self.board[2][0]) or
            (self.board[0][1] != '-' and self.board[0][1] == self.board[1][1] == self.board[2][1]) or
            (self.board[0][2] != '-' and self.board[0][2] == self.board[1][2] == self.board[2][2])):
            print('Vertical Win')
            return True
        else:
            return False

    def CrossWin(self): #checks for a cross win
        if ((self.board[0][0] != '-' and self.board[0][0] == self.board[1][1] == self.board[2][2]) or
            (self.board[0][2] != '-' and self.board[0][2] == self.board[1][1] == self.board[2][0])):
            print('Cross win')
            return True
        else:
            return False

    def CheckForWin(self): #uses the 3 win checks to decide whether a win has occurred
        if self.HorizontalWin() or self.VerticalWin() or self.CrossWin():
            return True
        else:
            return False

    def GameFinished(self):
        if self.CheckForWin():
            self.root.quit()
            if self.humanPoints < self.computerPoints:
                messagebox.showinfo("Game Complete", 'Game finished! AI have won!')
            else:
                messagebox.showinfo("Game Complete", 'Game finished! You has won!')
            return True
        elif self.CheckForTie():
            self.root.quit()
            messagebox.showinfo("Game Complete", 'Game finished! It was a tie')
            return True
        else:
            return False


P = TicTacToe()