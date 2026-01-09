# Student Marks Calculator

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "D"

print("--- STUDENT MARKS CALCULATOR ---\n")

name = input("Enter Student Name: ")

try:
    math = float(input("Enter Math Marks: "))
    science = float(input("Enter Science Marks: "))
    english = float(input("Enter English Marks: "))
except ValueError:
    print("Invalid input! Please enter numbers only ❌")
    exit()

total = math + science + english
average = total / 3
grade = calculate_grade(average)

print(f"\nStudent: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
print("Calculation completed! Keep studying 📚")