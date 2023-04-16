'''Tic-tac-toe module containing state checking function'''


def check_state(game_state):
    '''Check the state of a game of Tic-tac-toe.

    :param list[list[int]] game_state: The state of the game.
    :returns: 0 if game is tied, 1 if 'X' won, 2 if 'O' won, -1 if game is ongoing
    :rtype: int
    '''

    # Check if either player won
    for player in (1, 2):

        # Check top-left to bottom-right diagonal
        if len([i for i in [game_state[0][0], game_state[1][1], game_state[2][2]]
               if i == player]) == 3:

            return player

        # Check top-right to bottom-left diagonal
        if len([i for i in [game_state[0][2], game_state[1][1], game_state[2][0]]
               if i == player]) == 3:

            return player

        # Check rows
        for row in game_state:
            if len([i for i in row if i == player]) == 3:
                return player

        # Check columns
        for col in range(3):
            if len([row[col] for row in game_state if row[col] == player]) == 3:
                return player

    # Check if game is tied
    if len([i for i in row for row in game_state if i != 0]) == 9:
        return 0

    return -1

