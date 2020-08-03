last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

#Question 1 
subjects = ["physics", "calculus", "poetry", "history"]
print(subjects)

#Question 2
grades = [98, 97, 85, 88]
print(grades)

#Question 5
subjects.append("computer science")

grades.append(100)

#Question 3 and 4
gradebook = list(zip(subjects, grades))
print(gradebook)

#Question 6
gradebook.append(("visual arts", 93))
print(gradebook)

#Question 7
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

