import random

boolean_expressions = [
    'not False',
    'not True',
    'True or False',
    'True or True',
    'False or True',
    'False or False',
    'True and False',
    'True and True',
    'False and True',
    'False and False',
    'not (True or False)',
    'not (True or True)',
    'not (False or True)',
    'not (False or False)',
    'not (True and False)',
    'not (True and True)',
    'not (False and True)',
    'not (False and False)',
    '1 != 0',
    '1 != 1',
    '0 != 1',
    '0 != 0',
    '1 == 0',
    '1 == 1',
    '0 == 1',
    '0 == 0'
]


class ExpressionGame():
    def __init__(self, expression_list):
        self.expression_list = expression_list
        self.player_score = 0

    def get_random_question(self):
        index = random.randint(0, len(self.expression_list)-1)
        question = self.expression_list[index]
        answer = eval(question)
        return index, question, answer

    def play(self):
        print('''
            Welcome to the boolean value game!
            For each question type spell out the whole answer (without quotes).
            The answer will be either "True" or "False".
        ''')
        length = len(boolean_expressions)

        while len(boolean_expressions) > 0:
            remaining = len(boolean_expressions)
            print(
                "{0} of {1} answered correctly.".format(self.player_score, length),
                "{0} remain.".format(remaining)
            )
            index, question, answer = self.get_random_question()
            player_answer = input("What is the value of the following expression?\n\n\t{0}\n".format(question))

            if player_answer == str(answer):
                print("\nThat is correct!\n")
                del self.expression_list[index]
                self.player_score += 1
            else:
                print('Incorrect. The correct answer is: ' + str(answer))
        print("FINAL SCORE: {0} of {1} questions".format(self.player_score, length))


g = ExpressionGame(boolean_expressions)
g.play()