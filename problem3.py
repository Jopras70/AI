import math

class TicTacToe():
    # Initialize tic-tac-toe board
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None
        
	# Function to print current board
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
	# Function to print board input guide
    def print_board_nums(self):
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

	# Function to print guide the board input
    def mark_board(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.is_game_over(letter):
                self.winner = letter
            return True
        return False

    def is_game_over(self, letter):
        win_conditions = [
			[self.board[0], self.board[1], self.board[2]],
			[self.board[3], self.board[4], self.board[5]],
			[self.board[6], self.board[7], self.board[8]],
			[self.board[0], self.board[3], self.board[6]],
			[self.board[1], self.board[4], self.board[7]],
			[self.board[2], self.board[5], self.board[8]],
			[self.board[0], self.board[4], self.board[8]],
			[self.board[2], self.board[4], self.board[6]],
    	]
        #Check is current player is fulfil win condition or not
        if [letter, letter, letter] in win_conditions:
            return True
        else:
            return False
	#Function to check is there any empty square in board
    def empty_squares(self):
        return ' ' in self.board
    
	#Function to get board total empty squares
    def num_empty_squares(self):
        return self.board.count(' ')
    
	#Function to check is players mark valid
    def is_mark_valid(self):
        return [i for i, x in enumerate(self.board) if x == " "]

# Function to help execute tic-tac-toe
def play(game, x_player, o_player, print_game=True):
	
    if print_game:
        game.print_board_nums()
    letter = 'X'
    player=""
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if (letter == "O"):
            player="You"
        else:
            player="Computer"
        if game.mark_board(square, letter):
            
            if print_game:
                print(player + ' marks {}'.format(square))
                game.print_board()
                print('')

            if game.winner:
                if print_game:
                    print(player + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player


    if print_game:
        print('Its a tie!')
        
class Human():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input('Your turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.is_mark_valid():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
    
class Computer():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        return self.minimax(game, self.letter)['position']

	# Function to get best move for computer using minimax algorithm
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # Check if the previous move is a winner
        if state.winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # Each score should minimize
        for possible_move in state.is_mark_valid():
            state.mark_board(possible_move, player)
            sim_score = self.minimax(state, other_player)  # Simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.winner = None
            sim_score['position'] = possible_move  # Represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
    
if __name__ == '__main__':
    x_player = Computer('X')
    o_player = Human('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)