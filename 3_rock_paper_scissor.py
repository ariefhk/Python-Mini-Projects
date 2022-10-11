import random

computer_wins = 0
your_wins = 0
options = ['rock', 'paper', 'scissor']

while True:
    your_answer = input("Select Rock/Paper/Scissor or Q/q for Quit: ")

    if your_answer.lower() == 'q':
        break

    if your_answer not in options:
        continue

    computer_options = random.randint(0, 2)
    computer_answer = options[computer_options]
    print(f'You Pick: {your_answer}')
    print(f'Computer Pick: {computer_answer}')

    if your_answer.lower() == 'scissor' and computer_answer == 'paper':
        print('You Win!')
        your_wins += 1
        continue
    elif your_answer.lower() == 'rock' and computer_answer == 'scissor':
        print('You Win!')
        your_wins += 1
        continue
    elif your_answer.lower() == 'paper' and computer_answer == 'rock':
        print('You Win!')
        your_wins += 1
        continue
    else:
        print('Computer Win!')
        computer_wins += 1
        continue

print(f'Computer Wins: {computer_wins}')
print(f'Your Wins: {your_wins}')
