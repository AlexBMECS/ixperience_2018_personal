# -*- coding: utf-8 -*-
"""

Ejercicio. Tic-tac-toe

We are going to build a program that allows us to play tic-tac-toe on the terminal


In a nutshell, the tic-tac-toe board can be thought of 3 lists inside another one

board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

por ejemplo, si queremos ver cual es el estado de la casilla de arriba a la 
izquerda, podemos acceder haciendo tablero[[0,0]]

We have 2 players, and each player will alternate in choosing a different slot on the board,
and placing either an "X"  (player 1) or "O" (player 2)

The game will have to validate that the new coordinates chosen by the current player 
are valid, i.e., they need to be empty and be inside the board.


Hint: You can use a deque (in the module collections) to rotate between player 1 and 2
"""
import collections
#%%
def check_win(bort):
    won = False
    lst = range(len(bort))
    
    for n in lst:
       if bort[n,0] == ["X","X","X"] or ["O","O","O"]:
           won = True
           
    if bort[0,0] == "X" and bort[1,0] == "X" and bort[2,0] == "X":
           won = True
    if bort[0,1] == "X" and bort[1,1] == "X" and bort[2,1] == "X":
           won = True
    if bort[0,2] == "X" and bort[1,2] == "X" and bort[2,2] == "X":
           won = True
    if bort[0,0] == "O" and bort[1,0] == "O" and bort[2,0] == "O":
           won = True
    if bort[0,1] == "O" and bort[1,1] == "O" and bort[2,1] == "O":
           won = True
    if bort[0,2] == "O" and bort[1,2] == "O" and bort[2,2] == "O":
           won = True
           
    if bort[0,0] == "O" and bort[1,1] == "O" and bort[2,2] == "O":
           won = True   
    if bort[0,0] == "X" and bort[1,1] == "X" and bort[2,2] == "X":
           won = True
    
    if bort[0,2] == "O" and bort[1,1] == "O" and bort[2,0] == "O":
           won = True   
    if bort[0,2] == "X" and bort[1,1] == "X" and bort[2,0] == "X":
           won = True   
           
    return won        
#%%

def game():
    
    over = False
    player1 = True
    piece = ""
    num_moves = 0   
    winnner = "It's a tie"
    
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]
    
    while over != True and num_moves < 9:
        new_instruction = input("Please input the next players coordinates")
        
        coords = new_instruction.split(",")
        coord_int = [0,0]
        counter = 0
        
        for i in coords:
            coord_int[counter] = int(coords)
        
        if player1 == True:
            print("Player 1 is up")
            piece = "X"
            board[coord_int[0], coord_int[1]] = piece
            
            over = check_win(board)
            if over == True:
                winner = "Player 1"
        else:
            print("Player 2 is up")
            piece = "O"
            board[coord_int[0], coord_int[1]] = piece
            
            over = check_win(board)
            if over == True:
                winner = "Player 2"
            
        num_moves = num_moves+1
        player1 = !player1
        print(board)
    


if __name__ == "__main__":
    game()
