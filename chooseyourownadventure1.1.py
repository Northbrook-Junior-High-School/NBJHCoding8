#from random import randint
import random
exitchoice = ""
while exitchoice != "EXIT":
    print("You are in a dark school hallway.")
    door = input("There are 5 classrooms in front of you. You must choose one. 1/2/3/4/5: ")
    if door == "1":
        print("In this classroom, you find a briefcase full of gold coins!")
        print("Congrats! You won!")
    elif door == "2":
        print("In this classroom, you find a a pit of lava!")
        print("Game Over! You lost! :( ")
    elif door == "3":
        print("In this classroom, you find an angry teacher! She gave you an F-! ")
        print("Game Over! You lost! :( ")
    elif door == "4":
        dragondoor = input("You found a sleeping dragon. You can try to steal its gold (1), or sneak around it (2). 1/2: ")
        randnum = random.randint(1,2)
        if dragondoor == randnum and dragondoor == 1:
            print("You successfully stole the gold!")
            print("Congrats! You won!")
        elif dragondoor == randnum and dragondoor == 2:
            print("You successfully sneaked around the dragon!")
            print("Congrats! You won!")
        elif dragondoor != randnum:
            print("You awoke the dragon! It ate you!")
            print("Game Over! You lost! :( ")
        else:
            print("I don't understand")
    elif door == "5":
        print("You enter a room with a sphinx. It asks you to guess the number its thinking of.")
        number = int(input("Guess the number between 1 and 10: "))
        if number == random.randint(1,10):
            print("The sphinx tells you your guess was correct! She let you go!")
            print("Congrats! You won!")
        else:
            print("The sphinx tells you your guess was incorrect! She told her minions to attack!")
            print("Game Over! You lost! :( ")
    else:
        print("That wasn't an option!")
        print("Re-run the the code to try again!")
    exitchoice = input("Want to play again? Enter 'YES'. If not, enter 'EXIT'. YES/EXIT: ")