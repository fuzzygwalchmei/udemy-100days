class Gameboard(object):
    def __init__(self) -> None:
        super().__init__()
        self.board = self.make_board()
        self.squares = [str(i) for i in range(9)]
        self.current_winner = None
        self.commands = ['m','a','p','s','q',  *[str(i) for i in range(9)]]


    @staticmethod
    def make_board():
        return [' ' for i in range(9)]


    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']


    def print_board(self, option):
        printable = self.board if option == 'p' else self.squares
        sequence = [printable[i*3:(i+1) *3] for i in range(3)]

        for row in sequence:
            print('| '+ ' | '.join(row)+ ' |')

    def empty_squares(self):
        return self.board.count(' ')

    def make_move(self, move, letter):
        # print(f'Make move: {move}')
        if self.board[move] == ' ':
            self.board[move] = letter
            if self.winning_move(move, letter):
                self.current_winner = letter
            return True
        return False

    def winning_move(self, move, letter):
        # define winning moves
        # check each row
        row_line = move//3
        row = self.board[(row_line)*3:((row_line)+1)*3]
        if all(l == letter for l in row):
            return True
        # check each column
        col_ind = move%3
        col = [self.board[col_ind + i*3] for i in range(3)]
        if all(l==letter for l in col):
            return True

        
        # check diagonals
        if all(self.board[i] == letter for i in [0,4,8]):
            return True

        if all(self.board[i] == letter for i in [2,4,6]):
            return True



    # def check_move():



    # def play_game():
        # game options:
        # p == print board
        # a == available spaces
        # 0-8 == mave move
        # q == quit?
        # m = menu options








