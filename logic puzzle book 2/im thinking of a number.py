from random import randint

userguess = 0
playagain = 'y'
while playagain == 'y':
    number = randint(1, 9)
    while userguess != number:
        userguess = int(input("Guess a number 1-9: "))
        if userguess > number:
            print("Too High")
        elif userguess < number:
            print("Too Low")
        else:
            print("You got it!")
    playagain = input("Want to play again? (y/n) : ")
    if playagain == 'n':
        break
