# Assignment 5 - Module 6: Data Structures and Strings in Python
'''
Task 1: Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:
1. Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student’s name is not found, display an appropriate message.
'''

student_record={
    "Prashant":{"Marks":
                    {"Physics":91.3,
                    "Maths":90.2,
                    "Chemistry":95.1,
                    "Biology":88.8,
                    "Hindi":87,
                    "English":89.1,
                    }},
"Rupali":{"Marks":
                    {"Physics":93.3,
                    "Maths":94.2,
                    "Chemistry":90.6,
                    "Biology":91.8,
                    "Hindi":99,
                    "English":96.1,
                    }},
"Saisha":{"Marks":
                    {"Physics":92.3,
                    "Maths":97.2,
                    "Chemistry":93.8,
                    "Biology":92.4,
                    "Hindi":90,
                    "English":93.7,
                    }},
"Amit":{"Marks":
                    {"Physics":98.3,
                     "Maths":95.9,
                    "Chemistry":91.2,
                    "Biology":78.5,
                    "Hindi":97.3,
                    "English":94.3,
                    }},
    }
student_name=input("Enter The Student's Name:")
name=student_name.capitalize()
if name in student_record:
    try:
        for i in student_record[name]:
            print(f"{name} Marks: {student_record[name]["Marks"]}")
            break
    except:
        print("Try Again!")
else:
    print(f"Student Name: {name} Not Found")
