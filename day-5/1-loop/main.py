# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
avg = 0

for height in student_heights:
    avg += height

avg = avg / len(student_heights)
final_avg = round(avg)

print(final_avg)
