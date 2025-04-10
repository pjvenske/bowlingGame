"""
Unit tests for the Bowling Game

This module contains basic unit tests for the BowlingGame class.
Students should expand these tests to cover all functionality and edge cases.
"""

import unittest
from bowling_game import BowlingGame


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


if __name__ == "__main__":
    unittest.main()