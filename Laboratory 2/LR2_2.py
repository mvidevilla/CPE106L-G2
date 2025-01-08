"""
Filename: LR2_2.py

Allows users to navigate and view lines from a file
"""

filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        no_of_lines = len(lines)
    print(f"There are '{no_of_lines}' lines in the file...")

except FileNotFoundError:
    print("File cannot be found")

except Exception as e:
    print(f"Error: {e}")
    
while True:
    try:
       target_line = int(input("Enter a line number to read, enter 0 to exit the program: "))
       
    except ValueError:
        print(f"Please enter an integer\n")
        continue
    
    if target_line < 0:
        print("Please input a positive integer\n")
        continue
    
    elif target_line > no_of_lines:
        print(f"Please try a number below '{no_of_lines}'\n")
        continue
        
    elif target_line == 0:
        print("Leaving the program")
        break
    
    else:
        print(lines[target_line-1])
        continue
        
