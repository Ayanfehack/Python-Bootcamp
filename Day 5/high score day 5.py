students_scores = input("Input a list of student score ").split()
for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])
print(students_scores)


highest_scores = 0
for score in students_scores:
    if score > highest_scores:
        highest_scores = score
print(f"The highest score in the class is: {highest_scores}")