print("Welcome to roller coaster!")
height = int(input("What's your height in cm ? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    want_photos = input("Do you want a photo taken ? Y or N : ")
    if want_photos == "Y":
        bill += 3
        print(f"Please pay ${bill}.")
    else:
        print(f"Please pay ${bill}.")

else:
    print("You have not enough height to ride roller coaster 😢")
