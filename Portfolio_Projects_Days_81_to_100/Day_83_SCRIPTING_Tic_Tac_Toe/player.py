from random import choice
from abc import ABC
from sys import exit

class Player(ABC):
 
    def get_move(self, board):
        # Set up as a base method, built up in the below classes
        pass
       


class Humanplayer(Player):
    def __init__(self, letter) -> None:
        self.letter = letter

    def get_move(self, board):
        move = None
        valid = False

        while not valid:
            option = input('Its your turn - Make a move or pick a menu option: ').lower()
            if option not in board.commands:
                print('That is not a valid menu option (m for menu options)')
            elif option == 'p':
                board.print_board(board.board)
            elif option == 'a':
                board.print_board(board.squares)
            elif option == 'm':
                print("""
                Game Options:
                press p to print the board
                press a to show available squares
                press q to forfeit and quit
                press a number between 0 and 8 to take your turn
                press m to show this menu
                """)
            elif option == 'q':
                print('Thanks for playing')
                exit()
            elif option not in board.available_moves():
                print('That square is not available')
            else:
                move = int(option)
        return move



class Randomcomp(Player):
    def __init__(self, letter) -> None:
        self.letter = letter

    def get_move(self, board):
        return choice(board.available_moves)



class Smartcomp(Player):
    def __init__(self, letter) -> None:
        self.letter = letter

    def get_move(self, board):
        if len(board.avialable_moves()) == 9:
            move = choice(board.available_moves())
        else:
            move = self.minmax(board, self.letter)['position']
        return move

    @staticmethod
    def minmax(self, board, player):
        maximiser = self.letter
        opponent = 'O' if player == 'X' else 'X'

        if board.current_winner == opponent:
            modifier = 1 if opponent == maximiser else -1
            multiplier = board.empty_squares() + 1

            return {'position': None, 'score': modifier * multiplier}
        elif len(board.available_moves()) ==0:
            return {'position': None, 'score':0}

        elif player == maximiser:
            best = {'position': None, 'score': 99}

        else:
            best = {'position': None, 'score': -99}

        for possible_move in board.available_moves():
            board.make_move(possible_move, player)
            sim_score = self.minmax(board, opponent)

        # reset the temporary board
            board.board[possible_move]
            board.current_winner = None
            sim_score = self.minmax(board, opponent)


        # if player is max see if the simulated score is better than the previously best score
            if player == maximiser:
                if sim_score['score'] > best['score']:
                    best = sim_score

        # if the player is other see if the simulated score is lower than the previous best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        # return the best score
        return best