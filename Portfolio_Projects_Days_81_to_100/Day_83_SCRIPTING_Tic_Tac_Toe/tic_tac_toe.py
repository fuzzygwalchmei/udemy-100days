# Board
board = [[' ',' ',' '], 
        [' ',' ',' '],
        [' ',' ',' ']]


def print_board():
    for i, row in enumerate(board):
        print(f' {row[0]} | {row[1]} | {row[2]} ')
        if i < 2:
            print('-----------')
        
def check_win(row, col, player):
    # Check Rows
    if all([s == player for s in board[row]]):
        return True

    # Check Columns
    column  = [r[col] for r in board]
    if all([s == player for s in column]):
        return True

    # Diagonals
    d1 = [board[0][0],board[1][1], board[2][2]]
    d2 = [board[0][2], board[1][1], board[2][0]]

    if all([s == player for s in d1]):
        return True
    if all([s == player for s in d2]):
        return True
    
    return False

def check_turn():
    # Check numeric
    # Check is in 1-3
    # Check not already taken
    pass

def make_turn(player):
    while True:
        row = input('Choose a row (1,2,3): ')
        col = input('Choose a column (1,2,3): ')

        if row not in ['1','2','3']:
            print('Not a valid row')
        elif col not in ['1','2','3']:
            print("Not a valid column")
        
        elif board[int(row)-1][int(col)-1] != ' ':
            print('That spot is already taken')
        else:
            board[int(row)-1][int(col)-1] = player
            if check_win(int(row)-1, int(col)-1, player):
                # define win
                pass
            break
            

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