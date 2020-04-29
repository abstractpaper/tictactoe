import random
from tictactoe.engine import Board, Player

def play_random():
    board = Board()
    playerX = Player(board, "X")
    playerO = Player(board, "O")

    # first turn player
    player = random.choice([playerX, playerO])

    while not board.player_won:
        if board.empty_cells:
            cell = random.choice(board.empty_cells)
        else:
            # Draw
            break

        player.mark(*cell)
        player = playerX if player == playerO else playerO

    return board

if __name__ == '__main__':
    x_won = o_won = draw = 0
    for _ in range(10000):
        board = play_random()

        if board.player_won:
            if board.player_won.side == "X":
                x_won += 1
            elif board.player_won.side == "O":
                o_won += 1
        else:
            draw += 1

    print("X Won: ", x_won)
    print("O Won: ", o_won)
    print("Draw: ", draw)
