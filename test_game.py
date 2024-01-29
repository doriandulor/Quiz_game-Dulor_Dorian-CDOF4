import unittest
from quiz_game.game import QuizGame
from quiz_game.questions import sample_questions

class TestQuizGame(unittest.TestCase):
    def test_start_game(self):
        game = QuizGame(sample_questions)
        game.start_game()

if __name__ == "__main__":
    unittest.main()
