import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None # keep track of winner
    
    @staticmethod
    def make_board():
        return[' ' for _ in range(9)]
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc, tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign the sqaure to the letter)
        # then return True. If move is invalid, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row anywhere, row, column, or diagonal
        # first check row
        row_index = math.floor(square / 3)
        row = self.board[row_index*3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonal (ie if sqaure is an even number as al ldiagonal positions are even numbers)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # top left to bottom right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # top right to bottom left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all these checks fail;
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        # return len(self.available_moves())
        # or
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' '] # condenses following for loop into a single line using list comprehension
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)

        # return moves

def play(game, x_player, o_player, print_game=True):
    # return the winner of the game (letter) or return none (tie)
    if print_game:
        game.print_board_nums()

    letter = 'x' # default starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that
    # which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('') # just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after we make our move, we need to alternate letters
            letter = 'o' if letter == 'x' else 'x' 
            # if letter == 'x':
            #     letter = 'o'
            # else:
            #     letter = 'x'
        time.sleep(.8)
            # how do we check to see if someone won?
    if print_game:
        print('It\'s a tie!')

if __name__ == "__main__":
    x_player = SmartComputerPlayer('x')
    o_player = HumanPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
