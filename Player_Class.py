class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return f"{self.name} has {self.score} points"

    def get_score(self):
        return self.score

    def set_score(self, num):
        if num < 0:
            return "bad number must be 0 or higher"
        else:
            self.score += num

    def get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name
