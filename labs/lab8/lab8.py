"""
Name: Patsy Mejia-Rocha
lab8.py
"""

from secret import encode

def number_words(in_file_name, out_file_name):

    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    acc = 1

    for line in in_file:
        words = line.split()

        for i in words:
            out_file.write(str(acc) + " " + i + " \n")
            acc += 1

    in_file.close()


def hourly_wages(in_file_name, out_file_name):

    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")

    for line in in_file:
        element = line.split()
        hrly_pay = float(1.65 + float(element[2]))
        hrly_pay = hrly_pay * int(element[3])
        out_file.write(element[0] + " " + element[1] + " $" + str(round(hrly_pay, 2)) + " \n")

    in_file.close()


def calc_check_sum(isbn):

    acc = 0

    for i in range(10):
        positional = 10 - i
        acc = acc + (isbn[i] * positional)

    return acc


def send_message(file, friend):

    in_file = open(file, "r")
    friend = friend + ".txt"
    print(friend)
    out_file = open(friend, "w")

    for i in in_file:
        out_file.write(i)

    in_file.close()


def send_safe_message(file, friend, key):
    in_file = open(file, "r")
    friend = friend + ".txt"
    out_file = open(friend, "w")

    for i in in_file:
        encoded_message = encode(i, key)
        out_file.write(encoded_message)

    in_file.close()


def main():
    # number_words('test.txt', 'out.txt')
    hourly_wages('hourly_wages.txt', 'out2.txt')
    pass


main()
