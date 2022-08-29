print("You are in a dark school hallway.")
door = input("There are 3 classrooms in front of you. You must choose one. 1/2/3: ")
if door == "1":
    print("In this classroom, you find a briefcase full of gold coins!")
    print("Congrats! You won!")
elif door == "2":
    print("In this classroom, you find a a pit of lava!")
    print("Game Over! You lost! :( ")
elif door == "3":
    print("In this classroom, you find an angry teacher! She gave you an F-! ")
    print("Game Over! You lost! :( ")
else:
    print("That wasn't an option!")
    print("Re-run the the code to try again!")