class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None
        self.current_player = self.players[0]

    def check_winner(self):
        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True

        return False

    def play_game(self):
        while not self.check_winner():
            self.current_player.turn()
            self.check_winner()
            self.change_player()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"{self.winner.name} Wins!")
        print(self.winner)  # Fix this
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def change_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]
