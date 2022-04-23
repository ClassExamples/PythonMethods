from random import random

game_board_snakes = [
    [99, 41],
    [89, 53],
    [76, 58],
    [66, 45],
    [54, 31],
    [43, 18],
    [40, 3],
    [27, 5],
]
game_board_ladders = [
    [4, 25],
    [13, 46],
    [33, 49],
    [42, 63],
    [50, 69],
    [62, 81],
    [74, 92],
]
def calc_player_pos(current_pos, player_id):
    r = round(random() * 100) % 6
    dice_value = r + 1
    next_player_id = "p1" if player_id == "p2" else "p2"
    next_pos = current_pos + dice_value
    for snake_pos in game_board_snakes:
        pos1 = snake_pos[0]
        pos2 = snake_pos[1]
        if pos1 == next_pos:
            next_pos = pos2
            break    
    for ladder_pos in game_board_ladders:
        pos1 = ladder_pos[0]
        pos2 = ladder_pos[1]
        if pos1 == next_pos:
            next_pos = pos2
            break
    if next_pos > 100:
        next_pos = 100
    return next_pos, next_player_id


def game_loop():
    player_one_pos = 0
    player_two_pos = 0
    next_player = "p1"  #p2
    winner_is = None
    end_condition = False
    while True:
        if next_player == "p1":
            player_one_pos, next_player = calc_player_pos(
                player_one_pos, next_player)
        elif next_player == "p2":
            player_two_pos, next_player = calc_player_pos(
                player_two_pos, next_player)

        ## Check game end condition
        if player_one_pos == 100:
            winner_is = "p1"
            end_condition = True
        elif player_two_pos == 100:
            winner_is = "p2"
            end_condition = True

        # End game
        if end_condition:
            print("Player 1 pos ", player_one_pos)
            print("Player 2 pos ", player_two_pos)
            print("Winner is ", winner_is)
            break


if __name__ == "__main__":
    game_loop()