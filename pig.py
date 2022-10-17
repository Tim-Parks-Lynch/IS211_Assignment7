from Player_Class import HumanPlayer
from Game_Class import Game

if __name__ == "__main__":
    print("********************************")
    print("*            Pig               *")
    print("*            Game              *")
    print("********************************\n")
    p1 = HumanPlayer("John")
    p2 = HumanPlayer("Sally")

    pig_game = Game(p1, p2)
    pig_game.play_game()
