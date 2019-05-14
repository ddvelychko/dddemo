def game(player_1, player_2):

    if player_1 == player_2:
        return 'tie'
    elif str(player_1) == "rock" and str(player_2) == "scissors" or str(player_1) == "scissors" and str(player_2) == "paper" or str(player_1) == "paper" and str(player_2) == "rock":
        return "player_1"
    else:
        return "player_2"
