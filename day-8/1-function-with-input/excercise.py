# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5
# square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

import math


def calculate_number_of_cans(wall_height, wall_width, coverage):
    number_of_cans = (wall_height * wall_width) / coverage
    final_number = math.ceil(number_of_cans)
    print(f"You'll need {final_number} cans of paint.")


coverage = 5
test_h = int(input("Enter wall height : "))
test_w = int(input("Enter wall width : "))

calculate_number_of_cans(test_h, test_w, coverage)