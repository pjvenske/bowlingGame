import time
import unittest
from bowling_game.bowling_game import BowlingGame  # Assuming the BowlingGame class is in a file named bowling.py

class TestBowlingGamePerformance(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    def test_performance_all_strikes(self):
        """Measure time for scoring a perfect game (12 strikes)."""
        for _ in range(12):
            self.game.roll(10)
        
        start = time.perf_counter()
        score = self.game.score()
        end = time.perf_counter()
        duration_ms = (end - start) * 1000

        self.assertEqual(score, 300)
        print(f"[PERF] Perfect game scored in {duration_ms:.3f} ms")
    
    def test_performance_all_zeros(self):
        """Score an all-gutter game (0 pins)."""
        for _ in range(20):
            self.game.roll(0)

        start = time.perf_counter()
        score = self.game.score()
        end = time.perf_counter()
        duration_ms = (end - start) * 1000

        self.assertEqual(score, 0)
        print(f"[PERF] All-gutter game scored in {duration_ms:.3f} ms")
    
    def test_performance_large_input_noise(self):
        """Stress test: simulate thousands of extra rolls (e.g., a loop bug or external input attack)."""
        for _ in range(10000):
            self.game.roll(0)

        start = time.perf_counter()
        score = self.game.score()
        end = time.perf_counter()
        duration_ms = (end - start) * 1000

        self.assertEqual(score, 0)
        print(f"[PERF] 10,000 rolls scored in {duration_ms:.3f} ms")

   
    

if __name__ == "__main__":
    unittest.main()