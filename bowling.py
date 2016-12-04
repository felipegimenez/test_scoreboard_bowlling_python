class Game(object):

    def __init__(self):
        self.score = 0
        self.rolls = [0] * 21
        self.current_roll = 0

    def roll(self, pins):
        self.rolls[self.current_roll] = pins
        self.current_roll += 1

    def show_score(self):
        self.score = 0
        self.frame_index = 0
        for frame in range(10):
            if self.is_strike(self.frame_index):
                    self.score += 10 + self.strike_bonus(self.frame_index)
                    self.frame_index += 1
            elif self.is_spare(self.frame_index):
                self.score += 10 + self.spare_bonus(self.frame_index)
                self.frame_index += 2
            else:
                self.score += self.sum_of_balls_in_frame(self.frame_index)
                self.frame_index += 2
        return self.score

    def strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def sum_of_balls_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10
