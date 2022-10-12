import random

choices = ['rock', 'paper', 'scissors']
playing = ''
while playing != 'q':
    compchoice = random.choice(choices)
    p1choice = input("rock, paper or scissors: ").lower()
    print(p1choice, compchoice)
    if compchoice == p1choice:
        print("Draw")
    elif compchoice == 'rock' and p1choice == 'scissors':
        print("Computer Wins!")
    elif compchoice == 'rock' and p1choice == 'paper':
        print('User Wins!')
    elif compchoice == 'scissors' and p1choice == 'paper':
        print("Computer Wins!")
    elif compchoice == 'scissors' and p1choice == 'rock':
        print('User Wins!')
    elif compchoice == 'paper' and p1choice == 'scissors':
        print('User Wins!')
    elif compchoice == 'paper' and p1choice == 'rock':
        print("Computer Wins!")
    keepPlaying = (input("Type 'Q' to quit: "))
