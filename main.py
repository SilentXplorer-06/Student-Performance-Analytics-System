"""Student Performance Analytics System - beginner-friendly version."""

from pathlib import Path

import numpy as np
import pandas as pd

SUBJECTS = ["Python", "Mathematics", "Data_Analysis", "AI_Fundamentals"]


def calculate_grade(average):
    """Choose a grade based on the student's average mark."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def analyze_students(data):
    """Calculate total, average, grade, and pass/fail for each student."""
    results = data.copy()
    results["Total"] = results[SUBJECTS].sum(axis=1)
    results["Average"] = results[SUBJECTS].mean(axis=1).round(2)
    results["Grade"] = results["Average"].apply(calculate_grade)

    # NumPy checks that a student has at least 35 marks in every subject.
    passed_all_subjects = (results[SUBJECTS].to_numpy() >= 35).all(axis=1)
    results["Result"] = np.where(passed_all_subjects, "Pass", "Fail")
    return results


def main():
    """Read the data, show the analysis, and save the results."""
    folder = Path(__file__).resolve().parent
    input_file = folder / "students.csv"
    output_file = folder / "student_results.csv"

    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Could not find students.csv. Keep it in the same folder as main.py.")
        return

    required_columns = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance_Percent"]
    missing = [column for column in required_columns if column not in data.columns]
    if missing:
        print("The dataset is missing these columns:", ", ".join(missing))
        return

    results = analyze_students(data)

    print("\n" + "=" * 68)
    print("             STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 68)
    print(f"Number of students: {len(results)}")

    print("\nSTUDENT RESULTS")
    print("-" * 68)
    shown_columns = ["Student_ID", "Name", "Total", "Average", "Grade", "Result"]
    print(results[shown_columns].to_string(index=False))

    # NumPy handles class-level statistics and counts.
    averages = results["Average"].to_numpy(dtype=float)
    pass_results = results["Result"].to_numpy()
    passed_count = int(np.count_nonzero(pass_results == "Pass"))
    failed_count = int(np.count_nonzero(pass_results == "Fail"))

    print("\nCLASS SUMMARY")
    print("-" * 68)
    print(f"Students passed : {passed_count}")
    print(f"Students failed : {failed_count}")
    print(f"Class average   : {np.mean(averages):.2f}")
    print(f"Highest average : {np.max(averages):.2f}")
    print(f"Lowest average  : {np.min(averages):.2f}")

    print("\nSUBJECT ANALYSIS")
    print("-" * 68)
    subject_averages = np.mean(data[SUBJECTS].to_numpy(dtype=float), axis=0)
    for subject, average in zip(SUBJECTS, subject_averages):
        print(f"{subject.replace('_', ' '):20}: {average:.2f}")

    print("\nTOP 3 STUDENTS")
    print("-" * 68)
    for _, student in results.nlargest(3, "Average").iterrows():
        print(f"{student['Name']:20} Average: {student['Average']:.2f}  Grade: {student['Grade']}")

    results.to_csv(output_file, index=False)
    print(f"\nFull results saved to: {output_file.name}")


if __name__ == "__main__":
    main()
