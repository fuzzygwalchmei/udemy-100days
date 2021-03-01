# Many thanks and credit to Kylie Ying who was the basis for much of this code as I learned
# to solve the AI component with recursion.
# Kylies githut for reference: https://github.com/kying18/tic-tac-toe


from gameboard import Gameboard
from player import Humanplayer, Randomcomp, Smartcomp
from random import choice, randint

human_player = None

quotes = ['How exciting....', 'oooo... what a choice...', 'Not sure I would have done that...',
            'Interesting...', 'Are we there yet?', 'Are you even trying?...']

def tic_tac_toe(board, x_player, o_player):

    board.print_board('o')
    print('')
    print('#'*15)
    print('')
    player_turn = 'X'

    while board.empty_squares() > 0:
        if player_turn == 'X':
            move = x_player.get_move(board)
        else:
            move = o_player.get_move(board)

        if board.make_move(move, player_turn):
            
            if board.current_winner:
                print(f'{board.current_winner} has made a winning move!')
                board.print_board('p')
                print('End Game')
                return True

            else:
                print(f'{player_turn} has made a move...')
                if player_turn == human_player:
                    print(choice(quotes))
            player_turn = 'X' if player_turn == 'O' else 'O'
    print('Its a tie!')


    # Define gameloop

if __name__ == '__main__':
    if randint(0,1) == 0:
        x_player = Smartcomp('X')
        o_player = Humanplayer('O')
        human_player = 'O'
        print("You are O's")
    else:
        o_player = Smartcomp('O')
        x_player = Humanplayer('X')
        human_player = 'X'
        print("You are X's")
    b = Gameboard()

    tic_tac_toe(b, x_player, o_player)