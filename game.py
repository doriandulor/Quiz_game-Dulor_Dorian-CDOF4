import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start_game(self):
        print("Welcome to the Quiz Game!") #begining of the game
        random.shuffle(self.questions) #randomise the questions

        for question in self.questions:
            print(question["text"]) # write the questions
            user_answer = input("Your answer: ") #ask for the answer of the question

            if user_answer.lower() == question["answer"].lower(): #check for the answer
                print("Correct!")
                self.score += 1 # increase the score if correct
            else:
                print(f"Wrong! The correct answer is {question['answer']}") #if the anwser is wrong don't increase the score

        print(f"\nGame Over! Your final score is: {self.score}/{len(self.questions)}") #at the end display the score

from questions import sample_questions # get the questions from the questions.py file

if __name__ == "__main__":
    game = QuizGame(sample_questions) 
    game.start_game()
