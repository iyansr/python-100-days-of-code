# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: You might need to do some research in Google to figure out how to do this.


print("Welcome to the tip calulcator\n")

bill_str = input("What was the total bill ? $")
percentage_str = input(
    "How much percentage tip would you like to give ? 10, 12 or 15 ? ")
people_str = input("How many people to split the bill ? ")

bill = float(bill_str)
percentage = float(percentage_str)
people = int(people_str)

percentage_total = bill * (percentage / 100)
bill_total = bill + percentage_total


total = bill_total / people
result = format(total, '.2f')

message = f"Each person should pay ${result}"
print(message)
