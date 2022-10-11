import unittest
from Player_Class import Player
from Dice_Class import Dice
from random import randint, seed


class TestUser(unittest.TestCase):
    def setUp(self):
        self.test_user = Player("Glynn")

    def test_a_player_creation(self):
        test_name = self.test_user.get_name()
        test_score = self.test_user.get_score()

        self.assertEqual(test_name, "Glynn")
        self.assertEqual(test_score, 0)
        self.assertEqual(self.test_user.__str__(), "Glynn has 0 points")

    def test_b_user_update_score(self):
        self.test_user.set_score(10)

        self.assertEqual(self.test_user.get_score(), 10)

    def test_c_user_update_name(self):
        self.test_user.change_name("Jamie")

        self.assertEqual(self.test_user.get_name(), "Jamie")


class TestDice(unittest.TestCase):
    def setUp(self):
        self.test_dice = Dice()

    def test_a_roll_dice(self):
        seed(self.test_dice.seed)
        test_dice_roll = randint(1, 6)
        result = self.test_dice.roll_dice()

        self.assertEqual(result, test_dice_roll)

    def test_b_set_seed(self):
        seed(2)
        self.test_dice.set_seed(2)

        self.assertEqual(self.test_dice.get_seed(), 2)

        test_dice_roll = randint(1, 6)
        result = self.test_dice.roll_dice()

        self.assertEqual(test_dice_roll, result)


if __name__ == "__main__":
    unittest.main()
