# Tic Tac Toe Game
# Tsion fixed 4 errors to make this game playable.

def draw_line(width, edge, filling): # Draws a horizontal line in the game grid.
    print(filling.join([edge] * (width + 1)))


def display_winner(player): # Displays the winner or tie message.
    if player == 0:
        print("Tie")
    else:
        print("Player " + str(player) + " wins!")

def check_row_winner(row):
    """
    Return the player number that wins for that row.
    If there is no winner, return 0.
    """
    if row[0] == row[1] and row[1] == row[2] and row[0] != 0:  # Tsion fixed this: must check row[0] != 0 to avoid false win
        return row[0]
    return 0


def get_col(game, col_number): # Extracts a column from the game board as a list.
    return [game[x][col_number] for x in range(3)]


def get_row(game, row_number): # Extracts a raw from the game board 
    return game[row_number]


def check_winner(game): # Checks if there is a winner in rows, columns, or diagonals.
    game_slices = []
    for index in range(3):
        game_slices.append(get_row(game, index))
        game_slices.append(get_col(game, index))

    down_diagonal = [game[x][x] for x in range(3)]
    up_diagonal = [game[0][2], game[1][1], game[2][0]]
    game_slices.append(down_diagonal)
    game_slices.append(up_diagonal)

    for game_slice in game_slices:
        winner = check_row_winner(game_slice)
        if winner != 0:
            return winner

    return 0  # Tsion fixed this: should return 0 if there's no winner (not return last winner)

def start_game(): # Initializes a 3x3 board filled with zeros (0 represents an empty space).
    return [[0, 0, 0] for x in range(3)]


def display_game(game): # Displays the Tic-Tac-Toe board.
    d = {2: "O", 1: "X", 0: "_"}
    draw_line(3, " ", "_")
    for row_num in range(3):
        new_row = []
        for col_num in range(3):
            new_row.append(d[game[row_num][col_num]])
        print("|" + "|".join(new_row) + "|")


def add_piece(game, player, row, column): # Adds the player's move to the board.
    """
    game: game state
    player: player number
    row: 0-index row
    column: 0-index column
    """
    game[row][column] = player  # Tsion fixed this: it was column+1 which causes index error
    return game


def check_space_empty(game, row, column): # Checks if a given space on the board is empty

    return game[row][column] == 0


def convert_input_to_coordinate(user_input): # Converts 1-based user input to a 0-based index.
    return user_input - 1


def switch_player(player): # Switches the current playe
    if player == 1:  # Tsion fixed this: it was '=' instead of '=='
        return 2
    else:
        return 1


def moves_exist(game): # Checks if there are any empty spaces left on the board.
    for row_num in range(3):
        for col_num in range(3):
            if game[row_num][col_num] == 0:
                return True
    return False


if __name__ == '__main__':
    game = start_game() # Initialize the game
    display_game(game) # Display the empty board
    player = 1  # Set first player
    winner = 0 # The winner is not yet defined
    
      # Run the loop while there are moves left & no winner
    while winner == 0 and moves_exist(game):
        print("Currently player: " + str(player))
        available = False
        while not available:
            row = convert_input_to_coordinate(int(input("Which row? (start with 1) ")))
            column = convert_input_to_coordinate(int(input("Which column? (start with 1) ")))
            available = check_space_empty(game, row, column)  # Tsion fixed this: forgot to pass column to the function
        game = add_piece(game, player, row, column)
        display_game(game)
        winner = check_winner(game)  # Tsion re-enabled winner check (was commented out)
        if winner == 0:
            player = switch_player(player) # Switch to the other player

    display_winner(winner) # Display the winner or tie message
