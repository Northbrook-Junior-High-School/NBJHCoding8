import random
import tkinter

game_over = False
score = 0
squares_remaining = 0
bombfield = []


def play_bomb_dodger():
    create_bombfield(bombfield)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()


def create_bombfield(bombs):
    global squares_remaining
    for row in range(0, 10):
        row_list = []
        for column in range(0, 10):
            if random.randint(1, 100) < 20:
                row_list.append(1)
            else:
                row_list.append(0)
                squares_remaining += 1
        bombs.append(row_list)
    print_field(bombs)


def print_field(bombs):
    for row_list in bombs:
        print(row_list)


def layout_window(window):
    for rowNumber, row_list in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(row_list):
            if random.randint(1, 100) < 25:
                square = tkinter.Label(window, text="    ", font=("Arial", 40), bg='dark green', relief='raised')
            elif random.randint(1, 100) > 75:
                square = tkinter.Label(window, text="    ", font=("Arial", 40), bg='sea green', relief='raised')
            else:
                square = tkinter.Label(window, text="    ", font=("Arial", 40), bg='wheat', relief='raised')
            square.grid(row=rowNumber, column=columnNumber)
            square.bind("<Button-1>", on_click)


def on_click(event):
    global score
    global game_over
    global squares_remaining
    square = event.widget
    row = int(square.grid_info()['row'])
    column = int(square.grid_info()['column'])
    currentText = square.cget('text')
    if not game_over:
        if bombfield[row][column] == 1:
            game_over = True
            square.config(bg='red')
            print('Game Over! You hit a bomb!')
            print('Your score was: ', score)

        elif currentText == "    ":
            square.config(bg='brown')
            total_bombs = 0

            if row < 9:
                if bombfield[row + 1][column] == 1:
                    total_bombs += 1

            if row > 0:
                if bombfield[row - 1][column] == 1:
                    total_bombs += 1

            if column > 0:
                if bombfield[row][column - 1] == 1:
                    total_bombs += 1

            if column < 9:
                if bombfield[row][column + 1] == 1:
                    total_bombs += 1

            if row > 0 and column > 0:
                if bombfield[row - 1][column - 1] == 1:
                    total_bombs += 1

            if row < 9 and column > 0:
                if bombfield[row + 1][column - 1] == 1:
                    total_bombs += 1

            if row > 0 and column < 9:
                if bombfield[row - 1][column + 1] == 1:
                    total_bombs += 1

            if row < 9 and column < 9:
                if bombfield[row - 1][column - 1] == 1:
                    total_bombs += 1

            square.config(text=' ' + str(total_bombs) + ' ')
            squares_remaining -= 1
            score += 1
            if squares_remaining == 0:
                game_over == True
                print("Well done! You found all the safe squares!")
                print('Your score was: ', score)


play_bomb_dodger()
