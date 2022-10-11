from Game_Board import GameBoard
import argparse


def main(player1, player2):
    new_game = GameBoard(player1, player2)

    playing = True
    count = 0

    while playing:
        rolling = new_game.roll()

        print("current roller", new_game.current_roller)
        print("role", rolling)
        holding = new_game.hold()
        print(
            "after role and hold",
            new_game.current_roller,
            rolling,
            holding,
            count,
        )

        if count >= 50:
            playing = False

        count += 1


if __name__ == "__main__":

    main("Johnny", "Jan")
