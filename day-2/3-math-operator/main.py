# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

conv_w = float(weight)
conv_h = float(height)

total = conv_w / (conv_h ** 2)

print(int(total))
