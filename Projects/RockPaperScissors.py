import random
print('=' * 34)
print('Lets play ROCK, PAPER, SCISSORS, LIZARD AND SPOCK!')
print('=' * 34)
while True:
    computer = random.randint(1, 5)
    player = int(input('''1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
6) 🚫 EXIT
Pick a number: '''))
    if player == computer:
        print('Its a tie!')
    elif player == 6:
        break
    elif player == 1 and computer == 2:
        print('You chose ✊')
        print('CPU chose ✋')
        print('The computer won!')
    elif player == 1 and computer == 3:
        print('You chose ✊')
        print('CPU chose ✌️')
        print('The player won!')
    elif player == 2 and computer == 1:
        print('You chose ✋')
        print('CPU chose ✊')
        print('The player won!')
    elif player == 2 and computer == 3:
        print('You chose ✋')
        print('CPU chose ✌️')
        print('The computer won!')
    elif player == 3 and computer == 1:
        print('You chose ✌️')
        print('CPU chose ✊')
        print('The computer won!')
    elif player == 3 and computer == 2:
        print('You chose ✌️')
        print('CPU chose ✋')
        print('The player won!')
    elif player == 1 and computer == 4:
        print('You chose ✊')
        print('CPU chose 🦎')
        print('The player won!')
    elif player == 4 and computer == 1:
        print('You chose 🦎')
        print('CPU chose ✊')
        print('The computer won!')
    elif player == 4 and computer == 5:
        print('You chose 🦎')
        print('CPU chose 🖖')
        print('The player won!')
    elif player == 5 and computer == 4:
        print('You chose 🖖')
        print('CPU chose 🦎')
        print('The computer won!')
    elif player == 5 and computer == 3:
        print('You chose 🖖')
        print('CPU chose ✌️')
        print('The player won!')
    elif player == 3 and computer == 5:
        print('You chose ✌️')
        print('CPU chose 🖖')
        print('The computer won!')
    elif player == 3 and computer == 4:
        print('You chose ✌️')
        print('CPU chose 🦎')
        print('The player won!')
    elif player == 4 and computer == 3:
        print('You chose 🦎')
        print('CPU chose ✌️')
        print('The computer won!')
    elif player == 2 and computer == 4:
        print('You chose ✋')
        print('CPU chose 🦎')
        print('The computer won!')
    elif player == 4 and computer == 2:
        print('You chose 🦎')
        print('CPU chose ✋')
        print('The player won!')
    elif player == 2 and computer == 5:
        print('You chose ✋')
        print('CPU chose 🖖')
        print('The player won!')
    elif player == 5 and computer == 2:
        print('You chose 🖖')
        print('CPU chose ✋')
        print('The computer won!')
    elif player == 5 and computer == 1:
        print('You chose 🖖')
        print('CPU chose ✊')
        print('The player won!')
    elif player == 1 and computer == 5:
        print('You chose ✊')
        print('CPU chose 🖖')
        print('The computer won!')
    else:
        print('Invalid option!')
