student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest = student_scores[0]
for score in student_scores:
    if score > highest:
        highest = score

print(f"The highest score in the class is: {highest}")
