# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 08:30:15 2022

@author: Satya
"""

# Tic-Tac-Toe Program using
# random number in Python
  
# importing all necessary libraries
import numpy as np
import random
from time import sleep
  
# Creates an empty board
def create_board():
    return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
  
# Check for empty places on board
def possibilities(board):
    l = []
      
    for i in range(len(board)):
        for j in range(len(board)):
              
            if board[i][j] == 0:
                l.append((i, j))
    return(l)
  
# Select a random place for the player
def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return(board)
  
# Checks whether the player has three 
# of their marks in a horizontal row
def row_win(board, player):
    for x in range(len(board)):
        win = True
          
        for y in range(len(board)):
            if board[x, y] != player:
                win = False
                continue
                  
        if win == True:
            return(win)
    return(win)
  
# Checks whether the player has three
# of their marks in a vertical row
def col_win(board, player):
    for x in range(len(board)):
        win = True
          
        for y in range(len(board)):
            if board[y][x] != player:
                win = False
                continue
                  
        if win == True:
            return(win)
    return(win)
  
# Checks whether the player has three
# of their marks in a diagonal row
def diag_win(board, player):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != player:
                win = False
    return win
  
# Evaluates whether there is
# a winner or a tie 
def evaluate(board):
    winner = 0
      
    for player in [1, 2]:
        if (row_win(board, player) or
            col_win(board,player) or 
            diag_win(board,player)):
                 
            winner = player
              
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
  
# Main function to start the game
def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)
      
    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break
    return(winner)
  
# Driver Code
print("Winner is: " + str(play_game()))






#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
































class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()



















pip install tkinter

from tkinter import *
import tkinter.messagebox as msg

root= Tk()
root.title('TIC-TAC-TOE---DataFlair')


digits = [1,2,3,4,5,6,7,8,9]
mark = '' “
count = 0
panels = ["panel"]*10

def win(panels,sign):
    return ((panels[1] == panels[2] == panels [3] == sign)
            or (panels[1] == panels[4] == panels [7] == sign)
            or (panels[1] == panels[5] == panels [9] == sign)
            or (panels[2] == panels[5] == panels [8] == sign)
            or (panels[3] == panels[6] == panels [9] == sign)
            or (panels[3] == panels[5] == panels [7] == sign)
            or (panels[4] == panels[5] == panels [6] == sign) 
            or (panels[7] == panels[8] == panels [9] == sign))

def checker(digit):
    global count, mark, digits
    if digit==1 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mar
        button1.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==2 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button2.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==3 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button3.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==4 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button4.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==5 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button5.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==6 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button6.config(text = mark)
        count = count+1
        sign 
if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==7 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button7.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==8 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button8.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()

    if digit==9 and digit in digits:
        digits.remove(digit)
        if count%2==0:
            mark ='X'
            panels[digit]=mark
        elif count%2!=0:
            mark = 'O'
            panels[digit]=mark
        button9.config(text = mark)
        count = count+1
        sign = mark
        if(win(panels,sign) and sign=='X'):
            msg.showinfo("Result","Player1 wins")
            root.destroy()
        elif(win(panels,sign) and sign=='O'):
            msg.showinfo("Result","Player2 wins")
            root.destroy()
  
    if(count>8 and win(panels,'X')==False and win(panels,'O')==False):
        msg.showinfo("Result","Match Tied")
        root.destroy()
        
Label(root,text="player1 : X",font="times 15").grid(row=0,column=1)
Label(root,text="player2 : O",font="times 15").grid(row=0,column=2)

button1=Button(root,width=15,font=('Times 16 bold'),height=7,command=lambda:checker(1))
button1.grid(row=1,column=1)
button2=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda:checker(2))
button2.grid(row=1,column=2)

button3=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(3))
button3.grid(row=1,column=3)
button4=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(4))
button4.grid(row=2,column=1)

button5=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(5))
button5.grid(row=2,column=2)
button6=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(6))
button6.grid(row=2,column=3)

button7=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(7))
button7.grid(row=3,column=1)
button8=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(8))
button8.grid(row=3,column=2)

button9=Button(root,width=15,height=7,font=('Times 16 bold'),command=lambda: checker(9))
button9.grid(row=3,column=3)


root.mainloop()