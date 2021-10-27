"""
Name: Patsy Mejia-Rocha
weighted_average.py

Problem:
This program calculates the weighted average of inputted test grades.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    # open and write in files
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    avg_grades = []

    for line in in_file:
        name, grades = line.split(":")
        values = grades.split(' ')
        weight = []
        scores = []
        acc = 0

        for i in range(1, len(values), 2):
            weights = eval(values[i])
            weight.append(weights)

        for i in range(2, len(values), 2):
            grades = eval(values[i])
            scores.append(grades)

        for i in range(len(scores)):
            acc = ((weight[i]) + (scores[i])) + acc
        individ_weighted_avg = acc / 100
        avg_grades.append(individ_weighted_avg)
        # individual averages
        print(name, "\'s average: ", individ_weighted_avg)

    class_avg = sum(avg_grades) / len(avg_grades)
    # add blank line?
    print("\n")
    print('Class average: ', class_avg)

    # CLOSE FILE!!!!
    in_file.close()
    out_file.close()


def main():
    weighted_average("grades.txt", "avg.txt")


main()

