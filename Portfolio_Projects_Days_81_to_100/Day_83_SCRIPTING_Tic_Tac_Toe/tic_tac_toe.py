# Board
board = [[' ',' ',' '], 
        [' ',' ',' '],
        [' ',' ',' ']]


def print_board():
    for i, row in enumerate(board):
        print(f' {row[0]} | {row[1]} | {row[2]} ')
        if i < 2:
            print('-----------')
        
def check_win():
    # Check Rows

    # Check Columns

    # Diagonals
    pass

def check_turn():
    # Check numeric
    # Check is in 1-3
    # Check not already taken
    pass

def make_turn(player):
    while True:
        row = int(input('Choose a row (1,2,3): '))
        col = int(input('Choose a column (1,2,3): '))

        if row not in range(1,4):
            print('Not a valid row')
        elif col not in range(1,4):
            print("Not a valid column")
        
        elif board[row-1][col-1] != ' ':
            print('That spot is already taken')
        else:
            board[row-1][col-1] = player
            check_win()
            return

playing = True
turn = 0
# Loop for turns
while playing:
    print_board()
    if turn%2 == 0:
        player = 'X'
    else:
        player = 'O'
    make_turn(player)
    turn += 1



print_board()
# win conditions