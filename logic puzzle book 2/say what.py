phrase = input("Enter a string with many words separated by spaces: ")
print(phrase)
print(' '.join((phrase.split())[::-1]))
