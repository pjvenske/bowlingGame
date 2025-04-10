"""
Unit tests for the Bowling Game

This module contains basic unit tests for the BowlingGame class.
Students should expand these tests to cover all functionality and edge cases.
"""

import unittest
from bowling_game.bowling_game import BowlingGame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        """Set up a new game before each test."""
        self.game = BowlingGame()

    def roll_many(self, n, pins):
        """Helper to roll the same number of pins multiple times."""
        for _ in range(n):
            self.game.roll(pins)

    def test_gutter_game(self):
        """Test a game where no pins are knocked down."""
        self.roll_many(20, 0)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        """Test a game where one pin is knocked down on each roll."""
        self.roll_many(20, 1)
        # Expected score: 20 (1 pin × 20 rolls)
        self.assertEqual(20, self.game.score())
    
    def test_all_spares(self):
        """Test a game where every frame is a spare."""
        self.roll_many(21, 5)
        # Expected score: 10 + 5 bonus for each of the 10 frames
        self.assertEqual(150, self.game.score())
    
    def test_perfect_game(self):
        """Test a perfect game (all strikes)."""
        self.roll_many(12, 10)
        # Expected score: 300 (10 frames + 2 bonus rolls of 10 each)
        self.assertEqual(300, self.game.score())
    
    def test_one_spare(self):
        """Test a game with one spare."""
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.roll_many(16, 0)
        # Expected score: 5 + 5 + 3 (spare bonus) + 3 = 16
        self.assertEqual(16, self.game.score())
    
    def test_one_strike(self):
        """Test a game with one strike."""
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        # Expected score: 10 + 3 + 4 + 3 + 4 (strike bonus) = 24
        self.assertEqual(24, self.game.score())
    
    def test_spare_tenth_frame(self):
        """Test a game with a spare in the 10th frame."""
        self.roll_many(18, 0)
        self.game.roll(5)   # First roll of 10th frame
        self.game.roll(5)
        self.game.roll(3)
        # Expected score: 5 + 5 + 3 (spare bonus) = 13
        self.assertEqual(13, self.game.score())

    def test_strike_tenth_frame(self):
        """Test a game with a strike in the 10th frame."""
        self.roll_many(18, 0)
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        # Expected score: 10 + 3 + 4 = 17
        self.assertEqual(17, self.game.score())

    def test_open_mixed_game(self):
        """Test a game with only open frames."""
        self.game.roll(6)
        self.game.roll(3)
        self.game.roll(4)
        self.game.roll(2)
        self.game.roll(5)
        self.game.roll(4)
        self.game.roll(3)
        self.game.roll(6)
        self.game.roll(2)
        self.game.roll(3)
        self.game.roll(4)
        self.game.roll(5)
        self.game.roll(1)
        self.game.roll(2)
        self.game.roll(3)
        self.game.roll(4)
        self.game.roll(5)
        self.game.roll(3)
        self.game.roll(2)
        # Expected score: 6 + 3 + 4 + 2 + 5 + 4 + 3 + 6 + 2 + 3 + 4 + 5 + 1 + 2 + 3 + 4 + 5 + 3 + 2 = 70
        self.assertEqual(70, self.game.score())

        


if __name__ == "__main__":
    unittest.main()