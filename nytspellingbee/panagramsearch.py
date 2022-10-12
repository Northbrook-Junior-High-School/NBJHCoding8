infile = open("words.txt", "r")

candidates = []
for word in infile.readlines():
    word = word[:-1]
    if len(word) < 7:
        continue
    letters = list(word)
    letters = list(dict.fromkeys(letters))
    if len(letters) != 7:
        continue
    candidates.append(word)

outfile = open("candidates.txt", "a")
for word in candidates:
    outfile.write(word + "\n")
outfile.close()
