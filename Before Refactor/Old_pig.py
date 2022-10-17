from Game_Board import GameBoard
import argparse


def main(player1, player2):
    new_game = GameBoard(player1, player2)

    playing = True

    while playing is True:
        roll_amount = new_game.roll()
        new_game.hold()
        new_game.switch_players()

        player1_score, player2_score = new_game.player_scores.values()
        print(player1_score, player2_score, roll_amount)
        if player1_score >= 50 or player2_score >= 50:
            if player1_score > player2_score:
                print("player1 wins", new_game)
                playing = False
            else:
                print("player2 wins", new_game)
                playing = False
        # if count >= 50:
        #     playing = False

        # count += 1


if __name__ == "__main__":

    main("Johnny", "Jan")
