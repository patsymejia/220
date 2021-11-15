"""
Name: Patsy Mejia-Rocha
lab11.py
"""

from random import *


def words(txt_file):
    infile = open(txt_file, 'r')
    contents = infile.read()
    return contents.split('\n')


def random_word(list):
    return list[randint(0, len(list) - 1)]


def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)


def won(word, letters):
    x = fill(word, letters)
    if x == word:
        return True
    else:
        return False


def play():
    list_of_words = words("wordlist.txt")
    secret = random_word(list_of_words)
    guesses = []
    incorrect = 0
    current = "_" * len(secret)
    while len(guesses) < 7 and won(secret, guesses) is False:
        display = fill(secret, guesses)
        print(display)
        print(guesses)
        print()
        for L in guesses:
            print(L, end=' ')
        letter = input("Guess a letter: ")
        guesses.append(letter)
        display = fill(secret, guesses)
        if letter not in secret:
            incorrect += 1
        else:
            current = display


def main():
    play()
    pass

main()
