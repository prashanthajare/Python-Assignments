# Task 1: Read a File and Handle Errors
'''
Problem Statement:  Write a Python program that:
1. Opens and reads a text file named sample.txt.
2. Prints its content line by line.
3. Handles errors gracefully if the file does not exist.
'''
import os
print("********* Task 1 ******************")
print()
filename = open("sample.txt","wt")

filename.write("Reading File contents: \n")
filename.write("This is a sample text file.\n")
filename.write("It contains multiple lines. \n")

filename.close()

fname=os.path.basename("sample.txt")

try:
    with open("sample.txt","rt") as sample:
        for line_num, line_content in enumerate(sample,start=1):
            print(f"Line {line_num}: {line_content.strip()}")
except FileNotFoundError:
        print(f"Error: The File {fname} was not found.")

#Task 2: Write and Append Data to a File
'''
Problem Statement: Write a Python program that:
1. Takes user input and writes it to a file named output.txt.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.
'''
print()
print("********* Task 2 ******************")
print()
with open("output.txt","at") as output:
    out_file = os.path.basename("output.txt")
    try:
        if os.path.getsize(out_file) == 0:
            with open("output.txt", "wt") as output:
                write_text = input("Enter text to write to the file:")
                output.write(write_text+"\n")
                print(f"Data successfully written to {out_file}.")
        else:
            with open("output.txt", "at") as output:
                write_text = input("Enter additional text to append:")
                output.write(write_text+"\n")
                print("Data successfully appended.")
    except FileNotFoundError:
        print(f"Error: The File {out_file} was not found.")
print()
print(f"Final content of {out_file}:")
with open("output.txt","rt") as final_output:
    for line in final_output:
        print(line.strip())
