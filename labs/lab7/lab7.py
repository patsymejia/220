"""
Name: Patsy Mejia-Rocha
Partner: <your partner's name goes here – first and last>
lab7.py
"""

def cash_conversion():
    user_input = eval(input("Enter an integer: "))
    print('${}.00'.format(user_input))


def encode():
    message = input("Enter a message to encode: ")
    key = eval(input("Enter an integer key value: "))
    acc = ' '
    for c in message:
        i = ord(c)
        new_char = chr(i + key)
        acc = acc + new_char
    print(acc)


def sphere_area(radius):
    area = 4 * 3.1415 * radius**2

    return area


def sphere_volume(radius):
    volume = (4/3) * 3.1415 * radius**3

    return volume


def sum_n(n):
    total = 0
    for i in range(n):
        total += i

    return total


def sum_n_cubes(n):
    total = 0
    for i in range(n):
        total += i**3

    return total


def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")
    acc = ' '
    for i in range(len(message)):
        c = ord(message[i])
        k = ord(key[i])
        result = c + k - 97
        acc += chr(result)
    print(acc)


def main():
    print(sphere_area(2))
    print(sphere_volume(5))
    print(sum_n(5))
    print(sum_n_cubes(5))
    pass


main()
