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
        roll_or_hold = ""

        while roll_or_hold != "h":
            roll = self.dice.roll_dice()

            if roll > 1:
                turn_total += roll
                print(f"\n{self.name}'s Turn")
                print("----------------------------------")
                print(
                    f"Role = {roll}",
                    f"\nTurn Total = {turn_total}"
                    f"\nPossible total if held = {self.total + turn_total}",
                    f"\nPlayer total = {self.total}\n",
                )
                roll_or_hold = input("Roll(r) or Hold(h) ? ").lower()

                print("----------------------------------\n\n")
            else:
                turn_total = 0
                print("----------------------------------")
                print(f"{self.name} rolled a 1:                 ")
                print(f"{self.name} Scratched -- Switching Users")
                print("----------------------------------\n")
                break

        if roll_or_hold == "h":
            print("********************************")
            print(f"{self.name} Held")
            print("********************************\n")

            self.total += turn_total
