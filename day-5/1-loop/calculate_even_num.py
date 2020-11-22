result = 0

for number in range(0, 101):
    if number % 2 == 0:
        result += number

print(result)

# OR :

total = 0

for number in range(2, 101, 2):
    total += number

print(total)
