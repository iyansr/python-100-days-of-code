print("Welcome to roller coaster!")
height = int(input("What's your height in cm ? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("Enter your age : "))
    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    elif age >= 45 and age <= 55:
        bill = 0
    else:
        bill = 12

    want_photos = input("Do you want a photo taken ? Y or N : ")
    if want_photos == "Y":
        bill += 3
    else:
        bill += 0


else:
    print("You have not enough height to ride roller coaster 😢")

print(f"Please pay ${bill}.")
