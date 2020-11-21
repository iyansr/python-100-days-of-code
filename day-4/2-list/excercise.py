# You are going to write a program which will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.

import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

random_index = random.randint(0, len(names) - 1)
person = names[random_index]
message = f"{person} is going to buy the meal today!"
print(message)
