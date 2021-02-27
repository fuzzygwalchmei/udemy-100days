class Player(object):

    def __init__(self, letter) -> None:
        super().__init__()
        self.letter = letter
        


class human_player(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def move(self, board):
        # input turn
        # is it an available move?
        # set board.location as self.letter



# class random_comp(Player):



# class smart_comp(Player):


