import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_game(self):
        print("Welcome to the Quiz Game!")
        random.shuffle(self.questions)

        for question in self.questions:
            print(question["text"])
            user_answer = input("Your answer: ")

            if user_answer.lower() == question["answer"].lower():
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}")

        print(f"\nGame Over! Your final score is: {self.score}/{len(self.questions)}")


# Example questions
sample_questions = [
    {"text": "What is the capital of France?", "answer": "Paris"},
    {"text": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"text": "What is 2 + 2?", "answer": "4"},
    # Add more questions as needed
]

if __name__ == "__main__":
    game = QuizGame(sample_questions)
    game.start_game()
