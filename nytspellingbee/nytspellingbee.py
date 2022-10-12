import random
import string

score = 0
found = []
good_letter_count = 0

vowels = ['a', 'e', 'i', 'o', 'u']
nouseletters = ['x', 'z', 'q', 'v']
consonants = []
for c in string.ascii_lowercase:
    if c not in vowels and c not in nouseletters:
        consonants.append(c)
print(consonants)

letters = (random.sample(vowels, k=2)) + (random.sample(consonants, k=5))
with open("/Volumes/STEM 9/pythonProject9/nytspellingbee/words.txt", "r") as f:
    word_list = f.readlines()

    # trim whitespace and remove short words
    word_list = [w.strip() for w in word_list]
    word_list = [w[:-2] for w in word_list]


# print(word_list)
def valid_check(worda, center, word_lista, founda, letter_list, good_letter_count):
    if len(worda) >= 4:
        if center in worda:
            if worda in word_lista:
                if worda not in founda:
                    for letter in worda:
                        if letter in letter_list:
                            good_letter_count += 1
                    if good_letter_count == len(worda):
                        return True
                    else:
                        print("Invalid Letters!")
                        return
                else:
                    print("Already Found!")
                    return
            else:
                print("Not Valid Word!")
                return
        else:
            print("Must Use Center Letter!")
            return
    else:
        print("Must Be 4 Letters Or More!")
        return


def panagram_seach():
    infile = open("/Volumes/STEM 9/pythonProject9/nytspellingbee/words.txt", "r")

    candidates = []
    for words in infile.readlines():
        words = words[:-1]
        if len(words) < 7:
            continue
        letters = list(words)
        letters = list(dict.fromkeys(letters))
        if len(letters) != 7:
            continue
        candidates.append(words)

    outfile = open("/Volumes/STEM 9/pythonProject9/nytspellingbee/candidates.txt", "a")
    for words in candidates:
        outfile.write(words + "\n")
    outfile.close()
    return candidates


def scorer(worda, letter_lista):
    if len(worda) == 4:
        return 1
    elif all([item in worda for item in letter_lista]):
        print("PANAGRAM!! \n\n")
        return len(worda) + 7
    else:
        return len(worda)


try:
    panagrams = open("candidates.txt", "r")
except:
    panagrams = panagram_seach()
random.shuffle(letters)
center_letter = letters[0]
letters = '  '.join(letters)

while score <= 100:
    print(f"Center Letter is: {center_letter.upper()}")
    print(f"Other Letters are:{letters[2:]}")
    word = input("Enter a word: ").lower()
    if valid_check(word, center_letter, word_list, found, letters, good_letter_count):
        score += scorer(word, letters)
        found.append(word)
    print("Score: " + str(score))
    print("Found Words: " + str(found))
print(f"Your final score is: {score}")
