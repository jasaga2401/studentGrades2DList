# Create an empty 2D list
grades = []

subjects = ["Maths", "English", "Science", "Computing"]

for student in range(2):
    
    studentRecord = []
    studentName = input('Enter student name: ')
    studentRecord.append(studentName)
    
    for subject in subjects:
        
        grade = int(input(f"Enter {subject} grade (40-100): "))
        
        while grade < 40 or grade > 100:
            grade = int(input(f"Invalid! Enter {subject} grade between 40 and 100: "))
        studentRecord.append(grade)
    
    grades.append(studentRecord)

print("\nGrades for 5 students (Maths, English, Science, Computing):")
for student in grades:
    print(student)

# average grade above 70

# total grades
avgGradeStudents = []

for student in grades:

    sumGrades = sum(student[1:])
    avgGrade = sumGrades / 4
    if (avgGrade > 70):
        avgGradeStudents.append(student[0])
        

print(avgGradeStudents)








