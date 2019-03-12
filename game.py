#game.py
import random

class Game():

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.score = 0

    def ask_question(self):
        if self.difficulty == 1:
            self.easy_questions()
        elif self.difficulty == 2:
            pass
        else:
            pass


    def easy_questions(self):

        for question in range(10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            print("*" * 20, "\n")
            user_answer = int(input("What is {} + {}?\n".format(num1, num2)))
            print("*" * 20, "\n")
            correct_answer = num1 + num2
            if user_answer == correct_answer:
                print("Correct!\n")
                self.score += 1

            else:
                print("Wrong Answer! Correct answer is {}\n".format(correct_answer))

        print("Your score is: {}/10, you got {}% correct!".format(self.score, self.score / 10 * 100))




#Test
game_test = Game(1)

game_test.ask_question()
