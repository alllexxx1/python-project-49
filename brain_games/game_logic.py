from prompt import string


ROUND_COUNT = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    for round in range(ROUND_COUNT):
        question, correct_answer = game.create_game_data()
        print(f'Question: {question}')
        user_answer = string('You answer: ')
        if user_answer != correct_answer:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".\n'
                  f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')
