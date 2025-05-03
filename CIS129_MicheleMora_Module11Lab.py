#Auther: Michele Mora
#05/02/2025
#CIS129 Lab Module 11
#Exercises 9.1, 9.2, and 9.3 from Deitel & Deitel

# Function to input grades and write them to a file
def input_grades(filename):
    try:
        with open(filename, 'w') as file:
            print("Enter grades (enter 'q' to quit):")
            while True:
                grade = input("Enter a grade: ")
                if grade.lower() == 'q':
                    break
                file.write(grade + '\n')
        print("Grades have been written to", filename)
    except IOError as e:
        print("Error:", e)

#Specify the filename where you want to store the grades
filename = 'grades.txt'

# Call the function to input grades and write them to the file
input_grades(filename)

#This code is to answer 9.2
#This code reads the grades stored in grades.txt
#and displays it in a text file. 

#Store grades.
grades = None 
#Open the file and reads the grades.
with open('grades.txt','r') as file:
    grades = file.readlines()

#Store the sum of grades. 
total = 0

#iterate over the grades and print it
for grade in grades:
    grade = int(grade.strip())
    print(grade)
    total += int(grade)
    
#display the info as mentioned
print(f"Total: {total}")
print(f"Count: {len(grades)}")
print(f"Average: {total/len(grades) : .2f}")

#This code answers 9.3
#This code allows a teacher to enter the full names
#of students and enter their grades from three exams 

import csv

# Open the CSV file in write mode
with open('grades.csv', mode='w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Ask for student information and write it to the CSV file
    while True:
        # Get student details from the instructor
        first_name = input("Enter student's first name (or 'done' to finish): ")
        
        # If the instructor enters 'done', exit the loop
        if first_name.lower() == 'done':
            break
        
        last_name = input("Enter student's last name: ")
        exam1 = int(input("Enter student's exam 1 grade: "))
        exam2 = int(input("Enter student's exam 2 grade: "))
        exam3 = int(input("Enter student's exam 3 grade: "))
        
        # Write the student information to the CSV file
        writer.writerow([first_name, last_name, exam1, exam2, exam3])

print("Student records have been written to grades.csv.")
