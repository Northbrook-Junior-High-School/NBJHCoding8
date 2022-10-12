playagain = 'y'
while playagain == 'y':
    string = input("Enter a string: ")
    print(string.replace(' ','') == string[::-1].replace(' ',''))
    playagain = input("Want to play again? (y/n): ")
    if playagain == 'n':
        break
