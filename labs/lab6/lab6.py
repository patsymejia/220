"""
Name: Patsy Mejia-Rocha
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input('Enter a full name: ').split(' ')
    reversed_name = name[0] + ', ' + name[1]
    print(reversed_name)


def company_name():
    domain = input('Enter a three-part internet domain: ').split('.')
    print(domain[1])


def initials():
    amt_names = eval(input('How many names will be input? '))
    for i in range(1, amt_names + 1):
        name = input('Enter the name of student ' + str(i) + ": ")
        last_name = input('Enter ' + name + "\'s last name: ")
        print(name + "\'s initials are " + name[0] + last_name[0] + '.')


def names():
    name_list = input('Enter a list of names, first and last only, separated by commas: ').split(", ")
    print('The initials are', end=" ")
    for name in name_list:
        name = name.split(' ')
        first = name[0]
        last = name[1]
        initials = first[0] + last[0]
        print(initials, end=' ')


def thirds():
    sentences_amt = eval(input('How many sentences will be input? '))
    for i in range(sentences_amt):
        sentence = input('Enter a sentence: ')
        print(sentence[2::3])


def word_average():
    acc = 0
    sentence = input('Enter a sentence: ')
    sentence = sentence.split(' ')
    for word in sentence:
        acc += len(word)


def pig_latin():
    sentence = input('Enter a sentence for translation: ')
    sentence = sentence.lower()
    sentence = sentence.split(' ')
    for word in sentence:
        x = word[1:]
        x = x + word[0] + "ay"
        print(x, end=' ')


def main():
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()


main()
