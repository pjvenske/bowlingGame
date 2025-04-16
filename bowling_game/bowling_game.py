"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    def __init__(self):
        # Initialize a new game
        self.rolls = []

    def roll(self, pins):
        # Records a roll in the game.
        self.rolls.append(pins)

    def score(self):
        # Calculate the score for the current game.
        score = 0
        frame_index = 0
        for _ in range(10):
            if self._is_strike(frame_index):
                # Strike
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame
                score += self._sum_of_balls_in_frame(frame_index)
                frame_index += 2

        return score

    def _is_strike(self, frame_index):
        # Check if the roll at frame_index is a strike.
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        # Check if the rolls at frame_index and frame_index + 1 are a spare.
        return frame_index + 1 < len(self.rolls) and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _strike_bonus(self, frame_index):
        # Calculate the bonus for a strike.
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        # Calculate the bonus for a spare.
        if frame_index + 2 < len(self.rolls):
            return self.rolls[frame_index + 2]
        return 0
    
    def _sum_of_balls_in_frame(self, frame_index):
        # Sum the balls in a frame, ensuring no out-of-bounds access.
        if frame_index + 1 >= len(self.rolls):
            return self.rolls[frame_index]  # Only one roll available
        return self.rolls[frame_index] + self.rolls[frame_index + 1]