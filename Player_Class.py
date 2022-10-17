from abc import ABC
from Dice_Class import Dice


class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.total = 0

    def __str__(self):
        return f"{self.name}'s Total = {self.total}"

    def show(self):
        print(f"{self}")

    def turn(self):
        pass


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.dice = Dice()

    def turn(self):
        turn_total = 0
        roll_or_hold = "r"

        while roll_or_hold != "h":
            roll = self.dice.roll_dice()

            if roll > 1:
                turn_total += roll
                print(
                    f"Role = {roll},\nPlayer total = {self.total}, \nPossible total if held = {self.total + turn_total} ",
                )
                roll_or_hold = input("Roll(r) or Hold(h) ? ").lower()
            else:
                turn_total = 0
                print("Scratched -- Switching Users")
                break

        if roll_or_hold == "h":
            print("\nPlayer Held")

            self.total += turn_total

        self.show()
