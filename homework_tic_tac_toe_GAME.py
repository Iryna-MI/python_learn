# quit game not implemented
# not valid moves not implemented

from tkinter import *
from tkinter import messagebox
import random

root = Tk() #Create the toplevel class for the tk which contains window of the application.
root.title('GAME O---X GAME')
game_run = True
ls = []
field = []
cross_count = 0
cnt = 0
scale_size = int(input("Input the scale size please: "))

#new game
def new_game():
    for row in range(scale_size):
        for col in range(scale_size):
            field[row][col]['text']= ' '
            field[row][col]['background'] = 'lavenderblush'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

#The quitFunc to quit game message - doesn't work
def quitFunc():
   messagebox.Message("Quit the game!")

#invalid move --- not implemented
def invalid_move():
    if field[row][col]['text'] != ' ':
        messagebox.showwarning('Invalid move! try again!')

#click function: write 'X' for player and move computer player
def click(row, col):
    global scale_size
    global cross_count
    global game_run
    if field[row][col]['text'] != ' ':
        messagebox.showwarning('Invalid move! try again!')
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        cross_count += 1
        player = 'X'
        check_win(player)
    if cross_count == scale_size*scale_size:
        game_run = False
    if game_run and cross_count < scale_size*scale_size:
        computer_move()
        cross_count += 1
        player = 'X'
        check_win(player)
    #if field[row][col]['text'] != ' ':
        #messagebox.showwarning('Invalid move! try again!')

#check possible coordinates of winner lines
def check_win(player):
    print('check who win')
    cnt = 0
    # win_rows
    for x in range(scale_size):
        x_coo = []
        y_coo = []
        cnt = 0
        for y in range(scale_size):
            if field[y][x]['text'] == player:
                cnt+=1
                x_coo.append(y)
                y_coo.append(x)
            if cnt == scale_size:
                for i in range(scale_size):
                    field[x_coo[i]][y_coo[i]]['background'] = 'grey'
                messagebox.Message('WInner','Winner player ' + player + ' !!!')
    #win columns
    for x in range(scale_size):
        x_coo = []
        y_coo = []
        cnt = 0
        for y in range(scale_size):
            if field[x][y]['text'] == player:
                cnt+=1
                x_coo.append(x)
                y_coo.append(y)
        if cnt == scale_size:
            for i in range(scale_size):
                field[x_coo[i]][y_coo[i]]['background'] = 'grey'
            messagebox.showinfo('WInner','Winner player:' + player+ ' !!!')
    x_coo = []
    y_coo = []
    cnt = 0
    #win main diagonal
    for x in range(scale_size):
        if field[x][x]['text'] == player:
            cnt+=1
            x_coo.append(x)
            y_coo.append(x)
    if cnt == scale_size:
        for i in range(scale_size):
            field[x_coo[i]][y_coo[i]]['background'] = 'grey'
        messagebox.showinfo('WInner','Winner player:' + player+ ' !!!')
    x_coo = []
    y_coo = []
    cnt = 0
    #win secondary diagonal
    for x in range(scale_size):
        if field[x][scale_size-x-1]['text'] == player:
            cnt+=1
            x_coo.append(x)
            y_coo.append(scale_size-x-1)
            if cnt == scale_size:
                for i in range(scale_size):
                    field[x_coo[i]][y_coo[i]]['background'] = 'grey'
                    messagebox.showinfo('WInner','Winner player:' + player+ ' !!!')

#random coordinates of computer moves
def computer_move():
    while True:
        row = random.randint(0, scale_size-1)
        col = random.randint(0, scale_size-1)
        print (row, ' ', col)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            player = 'O'
            check_win(player)
            return

for row in range(scale_size):
    line = []
    for col in range(scale_size):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lightblue1',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='New Game', command=new_game)
new_button.grid(row=scale_size, column=0, columnspan=scale_size, sticky='se')
quit_button = Button(root, text = 'Quit Game', command = quitFunc)
quit_button.grid(row=scale_size, column=0, columnspan=scale_size, sticky='sw')
root.mainloop()
