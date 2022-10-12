height = int(input("How tall are you in inches?: "))

if 47 < height < 54:
    print("You can ride the green roller coasters!")
elif 54 < height < 61:
    print('You can ride the yellow roller coasters!')
elif 61 < height < 68:
    print('You can ride the red roller coasters!')
elif height > 67:
    print("You can ride all the roller coasters!")
else:
    print("You can't ride any roller coasters or I don't understand!")
