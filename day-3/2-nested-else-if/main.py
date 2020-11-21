print("Welcome to roller coaster!")
height = int(input("What's your height in cm ?"))

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("Enter your age : "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")

else:
    print("You have not enough height to ride roller coaster 😢")
