"""Student Grade Analyzer CLI program."""

from __future__ import annotations

from typing import Optional, TypedDict


class Student(TypedDict):
    """A student record stored in the `students` list."""
    name: str
    grades: list[int]


def find_student(students: list[Student], name: str) -> Optional[Student]:
    """Find a student by name (case-insensitive).

    Args:
        students: List of student dictionaries.
        name: Name to search for.

    Returns:
        The matching student dictionary, or None if not found.
    """
    normalized = name.strip().lower()
    for student in students:
        if student["name"].lower() == normalized:
            return student
    return None


def add_new_student(students: list[Student]) -> None:
    """Option 1: Add a new student."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    if find_student(students, name) is not None:
        print(f"Student '{name}' already exists.")
        return

    students.append({"name": name, "grades": []})
    print(f"Student '{name}' added.")


def add_grades_for_student(students: list[Student]) -> None:
    """Option 2: Add grades for a student.

    Grades must be integers in [0, 100]. Input 'done' to stop.
    """
    if not students:
        print("No students found. Please add a student first.")
        return

    name = input("Enter student name: ").strip()
    student = find_student(students, name)

    if student is None:
        print(f"Student '{name}' not found.")
        return

    while True:
        grade_str = input("Enter a grade (or 'done' to finish): ").strip()

        if grade_str.lower() == "done":
            break

        try:
            grade = int(grade_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not (0 <= grade <= 100):
            print("Invalid grade. Please enter a value between 0 and 100.")
            continue

        student["grades"].append(grade)

    print(f"Grades updated for '{student['name']}'.")


def show_report(students: list[Student]) -> None:
    """Option 3: Show report (all students).

    Prints each student's average grade or N/A if grades are empty.
    At the end, prints max average, min average, and overall average.
    Overall average is computed as the mean of student averages.
    """
    if not students:
        print("No students to report.")
        return

    print("--- Student Report ---")

    averages: list[float] = []

    for student in students:
        grades = student["grades"]

        try:
            student_sum = sum(grades)
            avg = student_sum / len(grades)
        except ZeroDivisionError:
            avg = None

        if avg is None:
            print(f"{student['name']}'s average grade is N/A.")
        else:
            print(f"{student['name']}'s average grade is {avg:.1f}.")
            averages.append(avg)

    # If no grades were added for any student, summary cannot be computed.
    if not averages:
        print("No grades have been added yet.")
        print("----------------------")
        return

    max_avg = max(averages)
    min_avg = min(averages)
    overall_avg = sum(averages) / len(averages)

    print("----------------------")
    print(f"Max Average: {max_avg:.1f}")
    print(f"Min Average: {min_avg:.1f}")
    print(f"Overall Average: {overall_avg:.1f}")


def find_top_performer(students: list[Student]) -> None:
    """Option 4: Find top performer.

    Uses max() with a lambda key returning the average grade for
    a student dictionary, as required by the task.
    """
    if not students:
        print("No students found.")
        return

    students_with_grades = [s for s in students if s["grades"]]
    if not students_with_grades:
        print("No grades available to determine top performer.")
        return

    top_student = max(
        students_with_grades,
        key=lambda s: sum(s["grades"]) / len(s["grades"]),
    )
    top_avg = sum(top_student["grades"]) / len(top_student["grades"])

    print(
        f"The student with the highest average is {top_student['name']} "
        f"with a grade of {top_avg:.1f}."
    )


def print_menu() -> None:
    """Print the main menu exactly as in the assignment."""
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Show report (all students)")
    print("4. Find top performer")
    print("5. Exit")


def main() -> None:
    """Run the Student Grade Analyzer program."""
    students: list[Student] = []

    try:
        while True:
            print_menu()

            choice_str = input("Enter your choice: ").strip()
            try:
                choice = int(choice_str)
            except ValueError:
                print("Invalid choice. Please enter a number from 1 to 5.")
                continue

            if choice == 1:
                add_new_student(students)
            elif choice == 2:
                add_grades_for_student(students)
            elif choice == 3:
                show_report(students)
            elif choice == 4:
                find_top_performer(students)
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 5.")

    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C.
        print("\nExiting program.")


if __name__ == "__main__":
    main()
