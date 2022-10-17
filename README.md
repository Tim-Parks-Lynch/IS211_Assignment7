# IS211_Assignment7

Hi Professor,

Make your terminal window bigger when you run my code to help with the output. I tried to make it as clean as possible, but it takes a decent amount of space. Also feel free to ignore the below. I'm trying to get it ready for Assignment 8.

## Dice Class

- Attributes:
  - seed: 0
  - current_dice_roll: int
- Methods:
  - roll_dice:
  - get_seed:
  - set_seed:

## Player Class

- Abstract Base Case
- Attributes:
  - name:
  - total: 0
- Method:
  - show
  - `__str__`
  - turn

## Human Player Class

- Derived Class (Player)
- Derived Attributes:
  - name
  - total
- Derived Methods:
  - show
  - `__str__`
- Class Attributes:
  - dice = Dice class
- Class Methods:
  - turn
