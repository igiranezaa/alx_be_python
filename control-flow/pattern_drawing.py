# pattern_drawing.py

# Prompt for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw square pattern using nested loops
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to next line
    row += 1
