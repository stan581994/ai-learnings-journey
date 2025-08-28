student_info = {}

print("File content before: ")
with open("students.txt", "r") as file:
    # Assigning text to dictionary
    lines = file.readlines()
    content = "".join(lines)
    print(content)

    for line in lines:
        name, grade = line.strip().split(":")
        student_info[name] = int(grade)

while True:
    try:
        no_of_studs = int(input("How many students? "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

for i in range(no_of_studs):
    student_name = input("Enter Student name: ").strip().lower()
    while True:
        try:
            student_grade = int(input("Enter Student grade: "))
            break
        except ValueError:
            print("Invalid grade. Please enter a number.")

    # Update existing or add new student
    student_info[student_name] = student_grade

# Save the updated txt
with open("students.txt", "w") as file:
    # Sort the record alphabetically
    for name, grade in sorted(student_info.items()):
        file.write(f"{name}:{grade}\n")

# Print the txt content after update
print("File content after: ")
with open("students.txt", "r") as file:
    content = file.read()
    print(content)
