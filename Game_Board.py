from Player_Class import Player
from Dice_Class import Dice


class GameBoard:
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.dice = Dice()
        self.player_scores = {
            self.player1.name: 0,
            self.player2.name: 0,
        }
        self.current_score = 0
        self.current_roller = self.player1.name

    def __str__(self):
        return f"{self.player_scores}"

    def new_game(self, player1, player2):
        pass

    def get_score(self):
        return self.player_scores[self.current_roller]
        # return self.player_scores[self.current_roller]["score"]

    def hold(self):
        self.player_scores[self.current_roller] += self.current_score
        self.current_score = 0

    def roll(self):
        result = self.dice.roll_dice()
        if result > 1:
            self.update_current_score(result)
        else:
            self.current_score = 0
        return result

    def update_current_score(self, roll_num):
        self.current_score += roll_num

    def switch_players(self):
        # self.current_roller = (
        #     self.player1
        #     if self.current_roller == self.player2
        #     else self.player2
        # )
        if self.current_roller == self.player1.name:
            self.current_roller = self.player2.name
        else:
            self.current_roller = self.player1.name
