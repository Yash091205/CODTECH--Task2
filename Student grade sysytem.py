def calculate_letter_grade(average_grade):
    # This function calculates the letter grade based on the average grade.
    if average_grade >= 90:
        return 'A'
    elif average_grade >= 80:
        return 'B'
    elif average_grade >= 70:
        return 'C'
    elif average_grade >= 60:
        return 'D'
    else:
        return 'F'


def calculate_gpa(average_grade):
    # This function calculates the GPA based on the average grade (on a 10.0 scale).
    # GPA is calculated on a 10.0 scale.
    
    if average_grade >= 90:
        return 10.0
    elif average_grade >= 80:
        return 9.0
    elif average_grade >= 70:
        return 8.0
    elif average_grade >= 60:
        return 7.0
    else:
        return 6.0


def get_valid_grade(subject):
    # This function ensures that the grade input is a valid number (int or float) between 0 and 100.
    while True:
        grade = input(f"Enter the grade for {subject}: ")

        # Check if the grade is a valid number
        if grade.replace('.', '', 1).isdigit() and grade.count('.') <= 1:
            grade = float(grade)
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100. Please enter again.")
        else:
            print("Invalid input. Please enter a valid numeric grade.")


def manage_students_grades():
    print("Welcome to the Student Grade Tracker!")

    # List to store all students' data
    students_data = []

    while True:
        student_name = str(input("Enter the student's name : "))

        grades = []  # List to store grades for each subject for the current student
        subjects = []  # List to store subject names

        while True:
            subject = str(input("Enter the subject name : "))

            # Get valid grade for the subject
            grade = get_valid_grade(subject)
            grades.append(grade)
            subjects.append(subject)
            a =input("Do you want to add another subject(y/n):")
            if a == 'y':
                pass
            if a == 'n':
                break
        # Calculate average grade
        if len(grades) == 0:
            print("No grades entered!")
            continue

        average_grade = sum(grades) / len(grades)

        # Calculate letter grade and GPA
        letter_grade = calculate_letter_grade(average_grade)
        gpa = calculate_gpa(average_grade)

        # Store the student's data
        students_data.append({
            'name': student_name,
            'subjects': subjects,
            'grades': grades,
            'average_grade': average_grade,
            'letter_grade': letter_grade,
            'gpa': gpa
        })
        a =input("Do you want to add another student(y/n):")
        if a == 'y':
            pass
        if a == 'n':
            break

    # Display results in tabular format
    print("\n===== Grade Report =====")
    print("Student Name\tSubject\t\tGrade\tAverage Grade\tLetter Grade\tGPA (out of 10.0)")
    print("----------------------------------------------------------------------------------------------")
    
    # Display each student's data
    for student in students_data:
        for i in range(len(student['subjects'])):
            print(f"{student['name']:<15}\t{student['subjects'][i]:<16}{student['grades'][i]:<6}\t{student['average_grade']:.2f}\t\t{student['letter_grade']}\t\t{student['gpa']:.2f}")
    print("===============================================================================================")


# Call the function to start managing student grades
manage_students_grades()
