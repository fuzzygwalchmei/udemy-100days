class Gameboard(object):
    def __init__(self) -> None:
        super().__init__()
        self.board = self.make_board()
        self.squares = [i for i in range(9)]
        self.current_winner = None
        self.commands = ['m','a','p','q', *range(9)]


    @staticmethod
    def make_board():
        return [' ' for i in range(9)]


    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']


    def print_board(self, option):
        printable = self.board if option == 'p' else self.squares
        sequence = [printable[i*3:(i+1) *3] for i in range(3)]

        for row in sequence:
            print('| '+ ' | '.join(row + ' |'))

    def empty_squares(self):
        return self.board.count(' ')

    def make_move(self, move, letter):
        if self.board[move] == ' ':
            self.board[move] = letter
            if self.winning_move(move, letter):
                self.current_winner = letter
            return True
        return False

    def winning_move(self, move, letter):
        # define winning moves
        # check each row
        # check each column
        # check diagonals
        pass




    # def check_move():



    # def play_game():
        # game options:
        # p == print board
        # o == available spaces
        # 0-8 == mave move
        # q == quit?
        # m = menu options








