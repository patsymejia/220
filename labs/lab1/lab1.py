"""
Name: Patsy Mejia-Rocha
lab1.py

Problem: This function calculates the area of a rectangle.
"""

def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)

calc_area()



def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

calc_rec_area()



def calc_volume():
    length = eval(input("Enter the length of the rectangular solid: "))
    width = eval(input("Enter the width of the rectangular solid: "))
    height = eval(input("Enter the height of the rectangular solid: "))
    volume = length * width * height
    print("Volume =", volume)

calc_volume()



def shooting_percentage():
    total_shots = eval(input("Enter the total shots: "))
    shots_made = eval(input("Enter amount of shots made: "))
    percentage = shots_made / total_shots * 100
    print("Your shooting percentage is:", percentage, "%")

shooting_percentage()



def coffee():
    coffee_lbs = eval(input("How many pounds of coffee are you purchasing?"))
    total_cost = (coffee_lbs * 10.50) + (coffee_lbs * 0.86) + 1.50
    print("The total cost is: $", total_cost)


coffee()



def kilometers_to_miles():
    km_total = eval(input("Enter kilometers:"))
    miles = km_total * 0.62
    print(miles, "miles")

kilometers_to_miles()
