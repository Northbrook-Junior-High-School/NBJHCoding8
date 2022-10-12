import random

from ansi import Style, Fore

print('\U0001F7E9')
print('\U0001F7E8')
correct = []

def get_wordle_word():
    with open('words.txt', encoding='utf-8') as f:
        file = f.readlines()

        wordle_index = random.randint(0, len(file) - 1)
        # print(file[wordle_index].strip())
        return file[wordle_index].strip()


finalword = get_wordle_word()
guess = ''
guess_count = 0


# def valid_guess(guessa):
# 	with open('words.txt', encoding='utf-8') as f:
# 		file = f.readlines()
#
# 		if guessa in file:
# 			return True
# 	return False


def get_guess():
    guessa = ""
    guessa = input("Enter a guess: ")
    while len(guessa) != 5:
        print('Invalid Guess!')
        guessa = input("Enter a guess: ")

    return guessa


def color_guess(guessa, wordle_word, correct=correct):
    colored_guess = []
    letters = []

    for i in range(len(guessa)):
        if guessa[i] == wordle_word[i]:
            colored_guess.append(f"{Fore.GREEN}{guessa[i]}{Style.RESET_ALL}")
            correct += guessa[i]

        # colored_guess.append('\U0001F7E9')

        elif guessa[i] in wordle_word and guessa[i] not in letters and wordle_word.count(guessa[i]) == 1:
            letters.append(guessa[i])
            colored_guess.append(f'{Fore.YELLOW}{guessa[i]}{Style.RESET_ALL}')
        elif guessa[i] in guess and wordle_word.count(guessa[i]) > 1:
            if guessa.count(guessa[i]) != letters.count(guessa[i]):
                letters.append(guessa[i])
                colored_guess.append(f'{Fore.YELLOW}{guessa[i]}{Style.RESET_ALL}')

        # colored_guess.append('\U0001F7E8')
        else:
            # colored_guess.append('\U0001F7EB')
            colored_guess.append(guessa[i])

    return colored_guess

while guess != finalword and 0 <= guess_count < 6:
    # print(finalword)
    guess = get_guess()
    print(' '.join(color_guess(guess, finalword)))
    guess_count += 1
    guesses_left = 6 - guess_count
    print(f"guesses left: {guesses_left}")
print(f"The word was {finalword}")
print("Done!")
